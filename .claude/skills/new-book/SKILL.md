---
name: new-book
description: "Startet ein neues Lehrbuch in learn-anything. Führt ein Interview zu Zielen, Vorwissen und Vorlieben, legt das Buch an, macht einen Einstufungstest und stößt die Recherche an. Verwenden, wenn der Nutzer ein neues Thema lernen möchte („Ich möchte X lernen“, „/new-book X“)."
argument-hint: "<Thema>"
---

# /new-book: ein neues Buch beginnen

Thema: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (Abschnitte B, D, E, F). Das private Repo muss unter
`../learn-anything-private` ausgecheckt sein, sonst zuerst einbinden.

## 1. Interview

Ziel: genug verstehen, um ein Buch genau für diesen Lerner zu schreiben. Führe ein Gespräch, kein
Formular: **höchstens drei, vier Fragen pro Nachricht**, auf Antworten eingehen, nachhaken. Was
aus dem Gespräch schon klar ist, nicht erneut fragen. Nach zwei, höchstens drei Runden
zusammenfassen und bestätigen lassen.

Zu klären:

1. **Genaues Thema und Variante.** Viele Themen haben Varianten, die didaktisch verschiedene
   Bücher ergeben (Neu- vs. Altgriechisch, Lineare Algebra für Physiker vs. für Informatiker,
   Python für Datenanalyse vs. Webentwicklung). Nachfragen, wenn es nicht eindeutig ist.
2. **Ziel.** Warum lernt er das? Was will er am Ende können (konkrete Situation: „im Urlaub
   einkaufen und Smalltalk“, „Polchinski lesen können“)?
3. **Vorwissen** in diesem Thema und in angrenzenden Gebieten; Muttersprache, andere Sprachen.
4. **Zeitbudget und Lesesituation:** wie viel Zeit pro Woche, wie lange am Stück, auf welchem
   Gerät (Handy?), Zieltermin?
5. **Buchsprache:** In welcher Sprache soll das Buch erklären? (Bei Sprachbüchern: soll die
   Erklärsprache schrittweise zur Zielsprache wechseln? Das wird später im Immersionsplan
   festgelegt.)
6. **Stil und Vorlieben:** Tonfall (locker/sachlich), Humor, Geschichten, Tiefe vs. Tempo,
   Theorie vs. Praxis, Menge und Art der Übungen. Frag nach Büchern oder Kursen, die er mochte oder
   nicht mochte, und warum.
7. **Interessen**, aus denen Beispiele kommen können (Beruf, Hobbys).
8. **Umfang:** kompakter Kurs oder ausführliches Lehrbuch?

## 2. Buch anlegen

- **Archetyp** bestimmen: `languages`, `formal-sciences`, `natural-sciences`, `programming`,
  `humanities` oder `practical`. Passt keiner genau, den nächstliegenden nehmen und das in
  `DOMAIN.md` festhalten.
- **Slug** wählen: kurz, kleingeschrieben, Bindestriche, lateinische Buchstaben (z.B.
  `neugriechisch`, `galois-theorie`).
- Anlegen:
  ```bash
  python3 scripts/new_book.py <slug> --title "…" --subtitle "…" --topic "…" \
      --lang <buchsprache> [--target-lang <zielsprache>] --archetype <archetyp>
  ```
  Titel und Untertitel in der Buchsprache, einladend, nicht generisch.
- `../learn-anything-private/books/<slug>/LEARNER.md` aus dem Interview füllen (alles
  Persönliche gehört hierhin).
- `books/<slug>/STYLE.md`: erste Fassung aus den Stilvorlieben, konkret und prüfbar formuliert,
  mit dem Vermerk „vorläufig, wird mit dem Probekapitel abgestimmt“. Nichts Persönliches (nicht
  „weil er Physiker ist“, sondern „Beispiele gern aus der Physik“).

## 3. Recherche anstoßen

Starte den `researcher` **im Hintergrund** für die Vollrecherche (Slug, Auftrag „Vollrecherche nach
dem Interview“). Er arbeitet, während der Einstufungstest läuft. Status in `book.yml`: `research`.

## 4. Einstufungstest

- Lass den `exercise-designer` einen Einstufungstest erstellen (6–10 Fragen, von leicht bis schwer,
  im Chat schnell beantwortbar) und in `placement.md` speichern.
- Stelle die Fragen im Chat, gern in zwei Portionen. Sag dazu, dass „weiß ich nicht“ eine gute
  Antwort ist und niemand eine Note bekommt. Wer ausdrücklich keinen Test will, überspringt ihn.
- Werte aus: Antworten und Auswertung in `placement.md`, Konsequenzen (was sitzt, was fehlt, welches
  Einstiegsniveau) in `LEARNER.md`. Kurzes, ermutigendes, ehrliches Feedback an den Lerner.

## 5. Abschluss

- Auf den Researcher warten, seine Ergebnisse lesen. Offene Entscheidungen aus der Recherche
  (z.B. Transliterationskonvention, Notation) dem Lerner kurz vorlegen, wenn sie ihn betreffen;
  sonst sinnvoll entscheiden und in `DOMAIN.md` festhalten.
- Status `outline`. Beide Repos committen und pushen (workflow.md, E). Das Buch bleibt
  `published: false`.
- Dem Lerner in wenigen Sätzen sagen, was du über das Thema und seinen Stand gelernt hast, und
  vorschlagen, direkt mit der Outline weiterzumachen (`/outline`).
