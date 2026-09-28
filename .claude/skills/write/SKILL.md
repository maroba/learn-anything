---
name: write
description: "Schreibt Kapitel eines learn-anything-Buchs nach Outline und STYLE.md und veröffentlicht sie einzeln, sobald sie fertig sind. Einzelne Kapitel, das nächste offene oder alle restlichen. Über mehrere Sessions fortsetzbar. Verwenden nach der Stilabstimmung (Status writing)."
argument-hint: "[slug] [kapitelnummer(n) | next | all]"
---

# /write: Kapitel schreiben

Argumente: $ARGUMENTS (ohne Angabe: `next`)

Grundlagen: `.claude/docs/workflow.md` (A–F), `.claude/docs/book-format.md`.

## Voraussetzungen prüfen

- Status muss `writing` sein. Steht er noch auf `sample`, ist der Stil nicht abgestimmt: kurz
  nachfragen, ob trotzdem geschrieben werden soll.
- `progress.md` lesen: Was ist fertig, was halb, welche TODOs sind offen? Halb fertige Kapitel aus
  einer abgebrochenen Session zuerst fertigstellen.

## Planen

- Kapitel bestimmen: `next` = das erste noch nicht veröffentlichte Kapitel der Outline, dessen
  Voraussetzungen erfüllt sind; `all` = alle restlichen.
- Wellen bilden: Kapitel, deren Voraussetzungen fertig (mindestens im Entwurf) sind, können
  parallel laufen. Höchstens drei Kapitel gleichzeitig, damit Reviews sorgfältig bleiben.
- Bei `all` dem Lerner kurz den Plan nennen (Anzahl Kapitel, Wellen, dass jedes Kapitel sofort
  veröffentlicht wird, sobald es fertig ist) und dann ohne weitere Rückfrage loslegen.

## Schreiben

Pro Kapitel die Pipeline (workflow.md, C). Das veröffentlichte Probekapitel und die schon fertigen
Kapitel sind die Stilreferenz; der Author soll sie lesen.

- Vor dem Start eines Kapitels `progress.md`: Status „Entwurf“, damit eine spätere Session weiß,
  wo es weitergeht. Nach jedem Pipeline-Schritt aktualisieren.
- Jedes fertige Kapitel **sofort veröffentlichen** (workflow.md, E), nicht erst am Ende. So kann
  der Lerner lesen, während die nächsten entstehen.
- Nach jedem veröffentlichten Kapitel eine Zeile an den Lerner: Titel, Link, ein Satz Inhalt.
- Beim Schreiben späterer Kapitel `LEARNER.md`, `questions.md` und `exercises.md` erneut lesen:
  Fragen und Fehler aus der Zwischenzeit sollen einfließen (Wiederholungsboxen, Beispiele).
- Das Vorwort `index.qmd` aktualisieren, wenn sich der Charakter des Buchs geändert hat.

## Abschluss

- Wenn alle Kapitel der Outline veröffentlicht sind: Status `complete`, Vorwort final.
- Kurze Zusammenfassung an den Lerner: welche Kapitel neu sind, was als nächstes kommt, offene
  Punkte aus `progress.md`.
- Bei einem fertigen Buch vorschlagen, die gewonnene Didaktik als Skill festzuhalten
  (`distill-domain-skill`).
