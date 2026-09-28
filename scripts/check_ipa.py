#!/usr/bin/env python3
"""Compare the IPA given in a Modern Greek chapter with a rule-based transcription.

    python3 scripts/check_ipa.py books/neugriechisch/chapters/02-aorist.qmd [more files …]

Looks for pairs like `[το σπίτι]{lang="el"} | [to ˈspiti]` (vocabulary tables) or
`[λέξη]{lang="el"} [ˈleksi]` (running text) and prints every pair where the book's IPA differs from
the automatic one in sounds or stress position. The rules are deliberately simple (no synizesis
ια → [ʝa], no sandhi across words, no loanword exceptions), so every hit is a hint for a human or
the technical reviewer, not necessarily an error. Typical real finds: missing palatals
([c ç ʝ] before e/i), stress on the wrong syllable, ει/οι/αι read as diphthongs.
"""

import re
import sys
import unicodedata

VOICED_CONS = set("βγδζλμνρ")
VOICELESS = set("θκξπστφχψ")
FRONT = set("ei")
LETTERS = {
    "α": "a", "β": "v", "γ": "ɣ", "δ": "ð", "ε": "e", "ζ": "z", "η": "i", "θ": "θ", "ι": "i",
    "κ": "k", "λ": "l", "μ": "m", "ν": "n", "ξ": "ks", "ο": "o", "π": "p", "ρ": "r", "σ": "s",
    "τ": "t", "υ": "i", "φ": "f", "χ": "x", "ψ": "ps", "ω": "o",
}


def g2p(word: str) -> str:
    """Rule-based broad IPA for one Modern Greek word; stress marked with ˈ before the vowel."""
    letters = []
    for ch in word.lower().replace("ς", "σ"):
        d = unicodedata.normalize("NFD", ch)
        base = d[0]
        if "α" <= base <= "ω":
            letters.append((base, "́" in d, "̈" in d))
    out, i, n = [], 0, len(letters)
    while i < n:
        c, stressed, _ = letters[i]
        c2, st2, di2 = letters[i + 1] if i + 1 < n else ("", False, False)
        pair = c + c2
        if not stressed and not di2:
            if pair == "ου":
                out.append(("u", st2)); i += 2; continue
            if pair == "αι":
                out.append(("e", st2)); i += 2; continue
            if pair in ("ει", "οι", "υι"):
                out.append(("i", st2)); i += 2; continue
            if pair in ("αυ", "ευ", "ηυ"):
                c3 = letters[i + 2][0] if i + 2 < n else ""
                out.append(({"α": "a", "ε": "e", "η": "i"}[c], st2))
                out.append(("f" if c3 in VOICELESS or c3 == "" else "v", False)); i += 2; continue
        if pair == "μπ":
            out.append(("b", False)); i += 2; continue
        if pair == "ντ":
            out.append(("d", False)); i += 2; continue
        if pair == "γκ":
            out.append(("G", False)); i += 2; continue
        if pair == "γγ":
            out += [("ŋ", False), ("G", False)]; i += 2; continue
        if pair in ("γχ", "γξ"):
            out.append(("ŋ", False)); i += 1; continue
        if pair == "τσ":
            out.append(("ts", False)); i += 2; continue
        if pair == "τζ":
            out.append(("dz", False)); i += 2; continue
        if c == c2 and c not in "αεηιουω":
            i += 1; continue
        sound = LETTERS[c]
        if c == "σ" and (c2 in VOICED_CONS):
            sound = "z"
        out.append((sound, stressed if sound in "aeiou" else False)); i += 1

    ipa = ""
    for k, (sound, stressed) in enumerate(out):
        following = out[k + 1][0][:1] if k + 1 < len(out) else ""
        front = following in FRONT
        if sound == "k" and front:
            sound = "c"
        elif sound == "ɣ" and front:
            sound = "ʝ"
        elif sound == "x" and front:
            sound = "ç"
        elif sound == "G":
            sound = "ɟ" if front else "g"
        ipa += ("ˈ" + sound) if stressed else sound
    return ipa


def skeleton(ipa: str):
    """Sounds without spaces/punctuation, plus the index of the stressed vowel."""
    ipa = ipa.replace("ɡ", "g")
    flat, stress, count, pending = "", None, 0, False
    for ch in ipa:
        if ch == "ˈ":
            pending = True
            continue
        if ch in " ,.;!?-–—‿()":
            continue
        if ch in "aeiou":
            if pending and stress is None:
                stress = count
            count += 1
            pending = False if stress is not None else pending
        flat += ch
    return flat, stress


PAIR = re.compile(r'\[([^\]]+)\]\{lang="el"\}\s*\|?\s*\[([^\]\{]+)\](?!\{)')


def check(path: str) -> int:
    text = open(path, encoding="utf-8").read()
    hits, seen = 0, set()
    for greek, ipa in PAIR.findall(text):
        if (greek, ipa) in seen:
            continue
        seen.add((greek, ipa))
        # Only the first form of entries like "γράφω, έγραψα" / "[ˈɣrafo], [ˈeɣrapsa]"
        first_greek = re.sub(r"[;.!?«»]", "", greek.split(",")[0]).strip()
        first_ipa = ipa.split("],")[0].split(",")[0]
        if not first_greek or not re.search(r"[α-ωά-ώ]", first_greek.lower()):
            continue
        auto = " ".join(g2p(w) for w in first_greek.split())
        if skeleton(auto) != skeleton(first_ipa):
            hits += 1
            print(f"{path}: {first_greek}  book=[{first_ipa}]  rule=[{auto}]")
    return hits


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    total = sum(check(p) for p in sys.argv[1:])
    print(f"{total} difference(s) to review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
