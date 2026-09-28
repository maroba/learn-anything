---
name: feedback
description: "Verarbeitet die Rückmeldung des Lerners zum Probekapitel eines learn-anything-Buchs. Hält Einigungen in STYLE.md fest, überarbeitet das Probekapitel und wiederholt das, bis der Stil passt. Verwenden während der Probekapitel-Runde (Status sample)."
argument-hint: "[slug] <Rückmeldung>"
---

# /feedback: Stil abstimmen

Rückmeldung: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, C, E, F).

## Verstehen

- Enthält die Rückmeldung ¶-Referenzen, die Stellen im Quelltext über den Textausschnitt finden.
- Übersetze jede Rückmeldung in eine **konkrete, prüfbare Stilregel**. „Zu trocken“ ist keine
  Regel; „jeder Abschnitt beginnt mit einer Alltagssituation“ schon. Ist unklar, was gemeint ist,
  frag nach, am besten mit zwei konkreten Alternativen zur Auswahl.
- Unterscheide: Stil (gilt fürs ganze Buch → STYLE.md), Inhalt dieses Kapitels (nur hier ändern),
  Aufbau des Buchs (→ outline.md).
- Bei zwei Varianten: welche Elemente welcher Variante gefallen? Oft ist die Antwort eine
  Mischung.

## Festhalten

`books/<slug>/STYLE.md`: Regeln in die passenden Abschnitte einarbeiten und unter „Vereinbarungen
im Verlauf“ mit Datum protokollieren. Widerspricht eine neue Regel einer alten, die alte ersetzen
und das im Protokoll vermerken. Persönliches (warum der Lerner etwas mag) gehört in `LEARNER.md`
(Abschnitt Vorlieben), nicht in STYLE.md.

## Überarbeiten

Das Probekapitel mit dem `author` nach der neuen STYLE.md überarbeiten. Bei größeren inhaltlichen
Änderungen danach den `technical-reviewer`, bei geändertem Aufbau auch den `didactics-reviewer`.
Keine `changes`-Einträge während dieser Runde. Veröffentlichen (workflow.md, E) und dem Lerner in
wenigen Punkten sagen, was sich geändert hat, mit Link.

## Einigung

Sobald der Lerner zufrieden ist („passt“, „so schreiben“):

- STYLE.md: Vermerk „vorläufig“ entfernen, Datum der Einigung eintragen.
- Nicht gewählte Variante löschen (Datei und Eintrag in `_quarto.yml`), ggf. Titelzusatz entfernen.
- Status `writing`, `progress.md`: Probekapitel „veröffentlicht“.
- Beide Repos committen und pushen.
- Vorschlagen, wie es weitergeht: alle Kapitel am Stück (`/write all`) oder kapitelweise, und wie
  er beim Lesen Fragen stellen kann (¶ kopieren, im Chat einfügen, oder `/ask`).
