---
name: revise
description: "Setzt einen Änderungswunsch an einem veröffentlichten learn-anything-Buch um, von der Tippfehlerkorrektur bis zur Neufassung eines Abschnitts oder einer Änderung am Aufbau. Mit Änderungsvermerk und sofortiger Veröffentlichung. Verwenden, wenn der Lerner beim Lesen etwas geändert haben möchte."
argument-hint: "[¶-Referenz] <Änderungswunsch>"
---

# /revise: Änderungen am Buch

Wunsch: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, C, D, E), `.claude/docs/book-format.md`.

## Einordnen

Stelle finden wie in `/ask` beschrieben (¶-Referenz → Datei, Textausschnitt → genaue Stelle).
Dann einordnen:

| Art | Beispiel | Vorgehen |
|---|---|---|
| Korrektur | Tippfehler, falsches Wort | direkt ändern, kein `changes`-Eintrag |
| Lokale Änderung | Beispiel ergänzen, Erklärung umformulieren | direkt oder über `author`; `changes`-Eintrag |
| Fachliche Änderung | Aussage ist falsch oder unpräzise | `author` + `technical-reviewer`; `changes`-Eintrag |
| Stiländerung | „bitte generell weniger Fachbegriffe“ | STYLE.md ergänzen, betroffene Kapitel überarbeiten (vorher fragen, ob alle oder nur künftige) |
| Aufbau | Kapitel teilen, Reihenfolge ändern | outline.md, betroffene Kapitel, `_quarto.yml`; vorher den Plan bestätigen lassen |

Ist der Wunsch mehrdeutig, kurz mit einem konkreten Vorschlag nachfragen statt zu raten.

## Umsetzen

- Beim Ändern auf Folgen achten: Verweise anderer Kapitel auf die Stelle, Glossar, Übungen, die
  sich auf den geänderten Stoff beziehen. Bei mehr als lokalen Änderungen den
  `consistency-editor` über die betroffenen Kapitel laufen lassen.
- Abschnitts-IDs nicht ändern, auch wenn die Überschrift sich ändert.
- `changes`-Eintrag in der Buchsprache mit Abschnittsnummer, allgemein formuliert.
- Veröffentlichen (workflow.md, E). Dem Lerner in einem Satz sagen, was geändert ist, mit Link
  auf die Stelle (Anker-URL).

## Merken (privat)

Sagt der Wunsch etwas über den Lerner (Vorlieben, Schwierigkeiten), in `LEARNER.md` festhalten,
privates Repo committen und pushen.
