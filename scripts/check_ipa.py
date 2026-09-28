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


def g2p(word: str, synizesis: bool = False) -> str:
    """Rule-based broad IPA for one Modern Greek word; stress marked with ˈ before the vowel.

    With synizesis=True, an unstressed [i] between a consonant and a vowel becomes a glide
    (διαβάζω [ðʝaˈvazo], μάτια [ˈmatça], χωριό [xoˈrʝo], σπηλιά [spiˈʎa]).
    """
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

    if synizesis:
        glided = []
        for k, (sound, stressed) in enumerate(out):
            prev = glided[-1][0] if glided else ""
            nxt = out[k + 1][0][:1] if k + 1 < len(out) else ""
            if sound == "i" and not stressed and prev and prev[-1] not in "aeiou" and nxt in "aeiou" and nxt:
                if prev in ("l", "n"):
                    glided[-1] = ({"l": "ʎ", "n": "ɲ"}[prev], False)
                elif prev == "m":
                    glided.append(("ɲ", False))  # μια [mɲa], μπάμιες [ˈbamɲes]
                elif prev in ("k", "ɣ", "x", "G"):
                    glided.append(("J", False))  # palatalizes the consonant, then disappears
                elif prev[-1] in "ptfθs" or prev in ("ts", "ks", "ps"):
                    glided.append(("ç", False))
                else:
                    glided.append(("ʝ", False))
                continue
            glided.append((sound, stressed))
        out = glided

    ipa = ""
    for k, (sound, stressed) in enumerate(out):
        following = out[k + 1][0][:1] if k + 1 < len(out) else ""
        front = following in FRONT or following == "J"
        if sound == "k" and front:
            sound = "c"
        elif sound == "ɣ" and front:
            sound = "ʝ"
        elif sound == "x" and front:
            sound = "ç"
        elif sound == "G":
            sound = "ɟ" if front else "g"
        if following == "J":
            sound = {"k": "c", "ɣ": "ʝ", "x": "ç", "G": "ɟ"}.get(sound, sound)
        if sound == "J":
            continue
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


def _stress_last_vowel(word: str) -> str:
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in "αεηιουω":
            return unicodedata.normalize("NFC", word[: i + 1] + "́" + word[i + 1 :])
    return word


def join_elisions(greek: str) -> str:
    """Merge elided forms into one phonological word.
    θ’ ανέβω → θανέβω (stress stays on the verb);
    να ’σαι → νάσαι, σ’ το ’πα → στόπα (the lost stressed vowel passes its stress to the small word)."""
    greek = greek.replace("'", "’").replace("…", " ")
    greek = re.sub(r"(\w)’\s+(?=\w)", r"\1", greek)  # final-vowel elision: θ’ ανέβω
    return re.sub(r"(\w+)\s+’(\w+)", lambda m: _stress_last_vowel(m.group(1)) + m.group(2), greek)


def matches(greek: str, ipa: str) -> bool:
    """True if the book's IPA fits the rules, word by word (as many words as the IPA gives)."""
    words = [w for w in re.split(r"\s+", join_elisions(greek).replace("’", "")) if w]
    ipa = ipa.replace("…", " ")
    ipa_words = [w for w in ipa.split() if w]
    if len(ipa_words) == 1 and len(words) > 1:
        # IPA for a single word of a phrase: accept if it fits any of the words
        return any(matches(w, ipa) for w in words)
    if len(ipa_words) < len(words):
        words = words[: len(ipa_words)]
    elif len(ipa_words) > len(words) > 1:
        # IPA covers more than the first comma-part (e.g. a whole saying): compare the prefix
        ipa = " ".join(ipa_words[: len(words)])
    auto_variants = [" ".join(g2p(w, syn) for w in words) for syn in (False, True)]
    book_flat, book_stress = skeleton(ipa)
    for auto in auto_variants:
        auto_flat, auto_stress = skeleton(auto)
        if auto_flat != book_flat:
            continue
        accented = any(unicodedata.normalize("NFD", c)[1:2] == "\u0301" for c in greek)
        if auto_stress == book_stress or not accented or len(words) > 1:
            return True
    return False


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
        if not matches(first_greek, first_ipa):
            hits += 1
            auto = " ".join(g2p(w) for w in join_elisions(first_greek).replace("’", "").split())
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
