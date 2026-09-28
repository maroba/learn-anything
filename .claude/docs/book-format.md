# Buchformat: Konventionen für Kapiteltexte

Verbindlich für alle Commands und Agents, die Buchtext schreiben oder ändern. Der Stil eines
konkreten Buchs steht in dessen `STYLE.md` und hat bei Stilfragen Vorrang. Dieses Dokument regelt
das technische Format.

## Dateien

- Kapitel: `books/<slug>/chapters/NN-kurzname.qmd`, z.B. `03-verben-praesens.qmd`. `NN` ist
  zweistellig.
- Jedes neue Kapitel wird in `books/<slug>/_quarto.yml` unter `book.chapters` eingetragen, in der
  Reihenfolge der Outline.
- Größere Bücher können Teile bekommen (`- part: "Teil I: Grundlagen"` mit `chapters:` darunter).
- Selbst erzeugte Grafiken liegen unter `books/<slug>/images/`.

## Front Matter

```yaml
---
title: "Das Präsens"
changes:                       # erst ab der ersten Überarbeitung nach Veröffentlichung
  - date: 2026-10-02
    note: "Beispiel zu unregelmäßigen Verben ergänzt (Abschnitt 3.2)"
---
```

- Beim Erstveröffentlichen **kein** `changes`-Eintrag. Jede spätere inhaltliche Änderung bekommt
  einen Eintrag (Datum, kurze Beschreibung mit Abschnittsnummer, in der Buchsprache). Tippfehler
  brauchen keinen Eintrag. Das Probekapitel gilt erst ab der Einigung auf den Stil als
  veröffentlicht; Änderungen während der Stilrunde bekommen keinen Eintrag.

## Überschriften und Anker

- Die Kapitelüberschrift kommt aus `title`. Im Text beginnen Abschnitte mit `##`.
- **Jeder Abschnitt bekommt eine explizite, sprechende ID** mit `sec-`-Präfix, lateinisch
  transliteriert: `## Der Aorist {#sec-aorist}`. Die ID bleibt stabil, auch wenn die Überschrift
  umformuliert wird, denn ¶-Referenzen und Links hängen daran. IDs sind buchweit eindeutig.
- Querverweise: `@sec-aorist`, `@eq-basel`, `@tbl-endungen`, `@fig-alphabet`.
- Überschriften ohne Nummer: `{.unnumbered}`.

## Callouts

Titel immer in der Buchsprache. Diese Typen haben eine feste Bedeutung:

| Zweck | Markup |
|---|---|
| Merksatz, Kernregel | `::: {.callout-important}` + `## Merke` |
| Hintergrund, Exkurs (überspringbar) | `::: {.callout-note collapse="true"}` + `## Exkurs: …` |
| Typischer Fehler | `::: {.callout-warning}` + `## Achtung` |
| Tipp, Eselsbrücke | `::: {.callout-tip}` + `## Tipp` |
| Übung | `::: {.callout-note .exercise}` + `## Übung N.M` |
| Hinweis zu einer Übung (eingeklappt) | `::: {.callout-tip collapse="true" .hint}` + `## Hinweis 1` |
| Lösung (eingeklappt) | `::: {.callout-tip collapse="true" .solution}` + `## Lösung` |
| Übersetzung eines Textes (eingeklappt) | `::: {.callout-note collapse="true" .translation}` + `## Übersetzung` |
| Leserfrage | `::: {.callout-note .reader-question}` + `## Leserfrage: …` |
| Wiederholung früheren Stoffs | `::: {.callout-note .review}` + `## Zur Wiederholung` |
| Unsichere Aussage | `::: {.callout-caution .uncertain}` + `## Vorsicht` |

- **Übungen:** gestufte Hinweise und die Lösung jeweils als eigene, eingeklappte Callouts
  direkt unter der Übung. Nummerierung `Kapitelnummer.laufendeNummer`. Jede Übung ist so
  formuliert, dass der Lerner seine Lösung im Chat abgeben kann (`/check`).
- **Leserfragen:** entstehen aus Fragen des Lerners (`/ask`). Die Frage steht allgemein und
  anonym formuliert im Titel, darunter die Antwort. Nie persönliche Details.
- **Wiederholung:** greift Stoff früherer Kapitel auf, besonders solchen, mit dem der Lerner
  Schwierigkeiten hatte. Allgemein formulieren („Viele verwechseln …“), nicht persönlich.
- **Unsicherheit:** Ist eine Aussage umstritten, stark vereinfacht oder nicht sicher verifiziert,
  wird das offen gesagt, mit Verweis auf eine Quelle zum Nachlesen. Nicht souverän behaupten.

## Sprache im Text

- Text in einer anderen Sprache als der Buchsprache wird mit ihrem Sprachcode ausgezeichnet:
  `[καλημέρα]{lang="el"}` inline, `::: {lang="el"}` für Blöcke. Das verbessert Schriftwahl und
  Silbentrennung und ist die Grundlage für die Audio-Wiedergabe (Phase 3). In Tabellen die
  einzelnen Zellinhalte auszeichnen.
- Transliteration und Aussprache in einer einheitlichen Schreibweise, festgelegt in
  `glossary.md` bzw. `DOMAIN.md`.

## Mathematik, Code, Diagramme

- Mathematik in LaTeX: `$…$` inline, `$$…$$ {#eq-name}` abgesetzt.
- Code in Fenced Blocks mit Sprache. Jeder Code, der als lauffähig präsentiert wird, muss vom
  Technical Reviewer tatsächlich ausgeführt worden sein.
- Diagramme mit Mermaid (` ```{mermaid} `) oder als selbst erzeugte Grafik. Keine fremden Bilder
  ohne freie Lizenz; Quelle und Lizenz angeben.

## Länge

Richtwert, falls `STYLE.md` nichts sagt: ein Kapitel ist in 20 bis 40 Minuten lesbar, ein
Abschnitt behandelt eine Idee. Lieber mehr kurze Kapitel als wenige lange.
