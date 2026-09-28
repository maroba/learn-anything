#!/usr/bin/env python3
"""Generate audio (MP3) for the target-language text of a book.

What gets voiced:
  * the first column of every `.vocab` table (core vocabulary),
  * every paragraph inside a block in the target language (`::: {lang="el"}`),
    unless the block has the class `.no-audio`.

Each text is voiced once; files are named by a hash of provider, voice and text, so
unchanged texts are never paid for twice. `books/<slug>/audio/manifest.json` maps the
text as it appears on the page to its file; learn-anything.js adds a ▶ button for it.

    python3 scripts/make_audio.py neugriechisch --dry-run       # what would be voiced, and cost
    python3 scripts/make_audio.py neugriechisch                 # voice everything missing
    python3 scripts/make_audio.py neugriechisch --chapter 02    # only one chapter
    python3 scripts/make_audio.py neugriechisch --prune         # drop recordings of removed texts
    python3 scripts/make_audio.py --list-voices --lang el       # LuvVoice voices for a language
    python3 scripts/make_audio.py --sample out/ --lang el       # blind test of providers/voices

Configuration in book.yml:

    audio:
      provider: luvvoice        # or: openai
      voice: voice-XXX          # LuvVoice voice id, or an OpenAI voice name
      instructions: "..."       # optional, OpenAI only

API keys come from the environment (LUVVOICE_API_KEY, OPENAI_API_KEY) and are never written
anywhere.
"""

import argparse
import base64
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "books"

LUVVOICE_URL = "https://luvvoice.com/api/v1/text-to-speech"
LUVVOICE_MIN_INTERVAL = 6.5  # seconds; the API allows 10 requests per minute
OPENAI_URL = "https://api.openai.com/v1/audio/speech"
OPENAI_MODEL = "gpt-4o-mini-tts"
USER_AGENT = "learn-anything/1.0 (+https://github.com/maroba/learn-anything)"

SAMPLE_TEXTS = {
    "el": [
        "Καλημέρα. Είσαι χάλια. Τι έγινε;",
        "Χθες το βράδυ, κατά τις δέκα, άνοιξα ένα βιβλίο για τον Σλήμαν.",
        "Λοιπόν, άκου να δεις τι έγινε με τον θείο μου.",
        "Έλα ρε, μισή ωρίτσα μόνο!",
        "το σπίτι, οι ντομάτες, η Θεσσαλονίκη, ευχαριστώ πολύ",
    ],
}


# --- Extracting the texts ---------------------------------------------------------------------

def normalize(text: str) -> str:
    """The key under which a text is looked up; must match `normalize` in learn-anything.js."""
    return re.sub(r"\s+", " ", text).strip()


def speech_text(text: str) -> str:
    """What is actually sent to the TTS: without dialogue dashes and exercise gap markers."""
    text = re.sub(r"^[—–-]\s*", "", text)
    text = re.sub(r"\(\d+\)\s*…", "…", text)
    return text.strip()


def stringify(inlines) -> str:
    out = []
    for el in inlines:
        t, c = el["t"], el.get("c")
        if t == "Str":
            out.append(c)
        elif t in ("Space", "SoftBreak", "LineBreak"):
            out.append(" ")
        elif t in ("Emph", "Strong", "Underline", "Strikeout", "SmallCaps", "Superscript", "Subscript"):
            out.append(stringify(c))
        elif t == "Span":
            out.append(stringify(c[1]))
        elif t in ("Link", "Image"):
            out.append(stringify(c[1]))
        elif t == "Quoted":
            left, right = ("“", "”") if c[0]["t"] == "DoubleQuote" else ("‘", "’")
            out.append(left + stringify(c[1]) + right)
        elif t == "Code":
            out.append(c[1])
        elif t == "Math":
            out.append(c[1])
        # Note, Cite, RawInline: not visible as plain text, ignored
    return "".join(out)


def block_text(block) -> str:
    if block["t"] in ("Plain", "Para"):
        return stringify(block["c"])
    return ""


def cell_blocks(cell):
    # pandoc >= 2.10: Cell = [attr, alignment, rowspan, colspan, blocks]
    return cell[4]


def table_first_column(table):
    texts = []
    _attr, _caption, _colspecs, _head, bodies, _foot = table["c"]
    for body in bodies:
        # TableBody = [attr, row_head_columns, head_rows, body_rows]
        for row in body[3]:
            cells = row[1]
            if cells:
                texts.append(" ".join(block_text(b) for b in cell_blocks(cells[0])))
    return texts


def attr_of(block):
    _ident, classes, kvs = block["c"][0]
    return classes, dict(kvs)


def collect(blocks, lang, found, in_vocab=False):
    for b in blocks:
        t = b["t"]
        if t == "Div":
            classes, kvs = attr_of(b)
            if "no-audio" in classes:
                continue
            if "vocab" in classes:
                collect(b["c"][1], lang, found, in_vocab=True)
            elif kvs.get("lang", "").split("-")[0] == lang:
                # Dialogue lines ("— …") alternate between two speakers within a block.
                turn = 0
                for inner in b["c"][1]:
                    text = block_text(inner)
                    if not text:
                        continue
                    if re.match(r"\s*[—–]", text):
                        found.append((text, turn % 2))
                        turn += 1
                    else:
                        found.append((text, 0))
            else:
                collect(b["c"][1], lang, found, in_vocab)
        elif t == "Table" and in_vocab:
            found.extend((text, 0) for text in table_first_column(b))
        elif t in ("BlockQuote",):
            collect(b["c"], lang, found, in_vocab)
        elif t in ("BulletList", "OrderedList"):
            items = b["c"] if t == "BulletList" else b["c"][1]
            for item in items:
                collect(item, lang, found, in_vocab)


def texts_of_chapter(path: Path, lang: str) -> list[tuple[str, int]]:
    """(text, speaker) pairs; speaker 1 is the second voice in dialogues."""
    ast = json.loads(subprocess.run(
        ["quarto", "pandoc", str(path), "-f", "markdown", "-t", "json"],
        check=True, capture_output=True, text=True).stdout)
    found = []
    collect(ast["blocks"], lang, found)
    return [(normalize(t), s) for t, s in found if normalize(t)]


# --- Providers --------------------------------------------------------------------------------

def http_json(url, payload=None, headers=None, method=None):
    data = json.dumps(payload).encode() if payload is not None else None
    # Cloudflare in front of some APIs rejects Python's default user agent (error 1010).
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json", **(headers or {})}
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def require_env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(f"{name} is not set. Add it to the environment's settings and start a new session.")
    return value


_last_luvvoice_call = 0.0


def tts_luvvoice(text, voice, **_):
    global _last_luvvoice_call
    key = require_env("LUVVOICE_API_KEY")
    wait = LUVVOICE_MIN_INTERVAL - (time.time() - _last_luvvoice_call)
    if wait > 0:
        time.sleep(wait)
    for attempt in range(3):
        _last_luvvoice_call = time.time()
        status, body = http_json(LUVVOICE_URL, {"text": text, "voice_id": voice},
                                 {"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        if status == 429 or status >= 500:
            time.sleep(30 * (attempt + 1))
            continue
        break
    if status != 200:
        raise RuntimeError(f"LuvVoice {status}: {body[:300]!r}")
    result = json.loads(body)
    if result.get("audio_data"):
        return base64.b64decode(result["audio_data"])
    if result.get("audio_url"):
        req = urllib.request.Request(result["audio_url"], headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.read()
    raise RuntimeError(f"LuvVoice returned no audio: {result}")


def tts_openai(text, voice, instructions=None, **_):
    key = require_env("OPENAI_API_KEY")
    payload = {"model": OPENAI_MODEL, "voice": voice, "input": text, "response_format": "mp3"}
    if instructions:
        payload["instructions"] = instructions
    status, body = http_json(OPENAI_URL, payload,
                             {"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    if status != 200:
        raise RuntimeError(f"OpenAI {status}: {body[:300]!r}")
    return body


PROVIDERS = {"luvvoice": tts_luvvoice, "openai": tts_openai}


def list_luvvoice_voices(lang):
    key = require_env("LUVVOICE_API_KEY")
    status, body = http_json(f"{LUVVOICE_URL}?action=voices", headers={"Authorization": f"Bearer {key}"})
    if status != 200:
        sys.exit(f"LuvVoice {status}: {body[:300]!r}")
    voices = json.loads(body).get("voices", [])
    return [v for v in voices if not lang or v.get("language", "").lower().startswith(lang.lower())]


# --- Commands ---------------------------------------------------------------------------------

def file_name(provider, voice, instructions, text):
    digest = hashlib.sha1(f"{provider}|{voice}|{instructions or ''}|{text}".encode()).hexdigest()
    return digest[:16] + ".mp3"


def voice_book(args):
    book = BOOKS / args.slug
    meta = yaml.safe_load((book / "book.yml").read_text(encoding="utf-8"))
    lang = (meta.get("target-language") or "").split("-")[0]
    if not lang:
        sys.exit("book.yml has no target-language; nothing to voice.")
    cfg = meta.get("audio") or {}
    provider, voice, instructions = cfg.get("provider"), cfg.get("voice"), cfg.get("instructions")
    voices = [voice, cfg.get("dialogue-voice") or voice]
    if not args.dry_run and not args.fake and (provider not in PROVIDERS or not voice):
        sys.exit("Set audio.provider (luvvoice|openai) and audio.voice in book.yml first.")

    chapters = sorted((book / "chapters").glob("*.qmd"))
    if args.chapter:
        chapters = [c for c in chapters if c.name.startswith(args.chapter)]

    audio_dir = book / "audio"
    manifest_path = audio_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    if args.prune:
        if args.chapter:
            sys.exit("--prune needs all chapters; run it without --chapter.")
        current = {t for chapter in chapters for t, _ in texts_of_chapter(chapter, lang)}
        stale = [t for t in manifest if t not in current]
        for t in stale:
            del manifest[t]
        used = set(manifest.values())
        removed = [f for f in audio_dir.glob("*.mp3") if f.name not in used]
        for f in removed:
            f.unlink()
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        print(f"pruned {len(stale)} manifest entries and {len(removed)} unused files")
        return 0

    todo, chars = [], 0
    for chapter in chapters:
        for text, speaker in texts_of_chapter(chapter, lang):
            name = file_name(provider, voices[speaker], instructions, text)
            if manifest.get(text) == name and (audio_dir / name).exists():
                continue
            if not re.search(r"\w", speech_text(text)):
                continue  # nothing speakable, e.g. an exercise gap "(4) …"
            if all(t != text for t, _, _ in todo):
                todo.append((text, name, voices[speaker]))
                chars += len(speech_text(text))

    print(f"{len(todo)} text(s) to voice, {chars} characters, provider={provider}, voices={voices}")
    if args.dry_run:
        for text, _, v in todo[: args.show]:
            print(f"  · [{v}]", text)
        if len(todo) > args.show:
            print(f"  … and {len(todo) - args.show} more")
        return 0

    audio_dir.mkdir(exist_ok=True)
    tts = PROVIDERS.get(provider)
    for i, (text, name, v) in enumerate(todo, 1):
        if args.fake:
            (audio_dir / name).write_bytes(b"")
        else:
            (audio_dir / name).write_bytes(tts(speech_text(text), v, instructions=instructions))
        manifest[text] = name
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        print(f"[{i}/{len(todo)}] {name}  {text[:70]}")
    return 0


def voice_samples(args):
    out = Path(args.sample)
    out.mkdir(parents=True, exist_ok=True)
    texts = SAMPLE_TEXTS.get(args.lang)
    if not texts:
        sys.exit(f"No sample texts for language {args.lang!r}.")
    candidates = []
    if os.environ.get("LUVVOICE_API_KEY"):
        for v in list_luvvoice_voices(args.lang):
            candidates.append(("luvvoice", v["voice_id"], None))
    if os.environ.get("OPENAI_API_KEY"):
        instructions = "Speak natural, conversational Modern Greek with a native Athenian accent."
        for v in ("coral", "ash"):
            candidates.append(("openai", v, instructions))
    if not candidates:
        sys.exit("Neither LUVVOICE_API_KEY nor OPENAI_API_KEY is set.")

    # Anonymous, shuffled labels, so the listener cannot tell which provider is which.
    random.shuffle(candidates)
    key_lines = []
    for n, (provider, voice, instructions) in enumerate(candidates, 1):
        label = f"stimme-{n}"
        audio = b"".join(PROVIDERS[provider](t, voice, instructions=instructions) for t in texts)
        (out / f"{label}.mp3").write_bytes(audio)
        key_lines.append(f"{label}: {provider} {voice}")
        print(f"{label}.mp3 written")
    (out / "AUFLOESUNG.txt").write_text("\n".join(key_lines) + "\n", encoding="utf-8")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", nargs="?")
    parser.add_argument("--chapter", help="only chapters whose file name starts with this, e.g. 02")
    parser.add_argument("--dry-run", action="store_true", help="only list what would be voiced")
    parser.add_argument("--show", type=int, default=20, help="how many texts --dry-run prints")
    parser.add_argument("--fake", action="store_true", help="write empty files (for testing the site)")
    parser.add_argument("--prune", action="store_true",
                        help="drop recordings of texts that no longer exist (use without --chapter)")
    parser.add_argument("--list-voices", action="store_true", help="list LuvVoice voices")
    parser.add_argument("--lang", default="el", help="language for --list-voices / --sample")
    parser.add_argument("--sample", metavar="DIR", help="write anonymous voice samples for a blind test")
    args = parser.parse_args()

    if args.list_voices:
        for v in list_luvvoice_voices(args.lang):
            print(f"{v['voice_id']}\t{v.get('name')}\t{v.get('gender')}\t{v.get('language')}")
        return 0
    if args.sample:
        return voice_samples(args)
    if not args.slug:
        parser.error("slug required")
    return voice_book(args)


if __name__ == "__main__":
    sys.exit(main())
