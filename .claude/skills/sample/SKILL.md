---
name: sample
description: "Schreibt und veröffentlicht das Probekapitel eines learn-anything-Buchs, anhand dessen Stil und Ansatz mit dem Lerner abgestimmt werden. Optional mit einer zweiten Stilvariante zum Vergleich. Verwenden nach /outline."
argument-hint: "[slug] [kapitelnummer] [varianten]"
---

# /sample: das Probekapitel

Argumente: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, C, E, F), `.claude/docs/book-format.md`.

## Kapitel wählen

Das in `/outline` vorgewählte Kapitel, oder das im Argument genannte. Es soll typisch für das Buch
sein: echter Stoff, Beispiele, Übungen. Nicht Kapitel 1, denn Einstiegskapitel sind untypisch.
Setzt es Stoff aus früheren Kapiteln voraus, der noch nicht geschrieben ist, darf es auf diese
Kapitel verweisen, als gäbe es sie („wie in Kapitel 2“), und am Anfang in einem kurzen Callout
zusammenfassen, was dort behandelt wird.

## Schreiben

Das Kapitel durchläuft die volle Pipeline (workflow.md, C), denn es ist das Aushängeschild: An
seiner Qualität entscheidet der Lerner, ob ihm das Buch gefällt.

**Zweite Stilvariante:** Sind die Stilvorlieben aus dem Interview vage oder widersprüchlich, oder
bittet der Lerner darum (Argument `varianten`), zusätzlich eine Variante B desselben Kapitels in
einem deutlich anderen Stil schreiben (z.B. „erzählend, mit durchgehender Geschichte“ vs.
„kompakt, Regel–Beispiel–Übung“). Datei `chapters/NN-kurzname-b.qmd`, Titel mit Zusatz
„(Variante B)“, in `_quarto.yml` direkt hinter Variante A. Variante B braucht nur den Author und
den Technical Reviewer.

## Veröffentlichen

- Auch das Vorwort `index.qmd` in einer ersten kurzen Fassung schreiben (worum es geht, für wen,
  wie man das Buch liest, Hinweis auf das ¶ zum Fragenstellen), damit das Buch nicht leer wirkt.
- In `book.yml`: `published: true`, Status `sample`.
- Veröffentlichen (workflow.md, E), `progress.md` aktualisieren.

## Dem Lerner vorlegen

Link zum Kapitel (und zur Variante) nennen. Bitte ihn, beim Lesen auf konkrete Dinge zu achten, und
nenne zwei, drei davon passend zu den offenen Stilfragen: Tonfall, Tempo, Menge und Art der
Beispiele, Übungen, Länge. Er kann einfach frei antworten oder einzelne Stellen per ¶ zitieren.
Hinweis: Rückmeldungen gehen mit `/feedback` oder einfach als Nachricht.
