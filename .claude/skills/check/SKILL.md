---
name: check
description: "Korrigiert die Lösung des Lerners zu einer Übung aus einem learn-anything-Buch (oder eine freie Übungsantwort), erklärt Fehler und merkt sich Fehlermuster im privaten Lernerprofil, damit das Buch adaptiv wird. Verwenden, wenn der Lerner eine Übungslösung schickt („Übung 3.2: …“)."
argument-hint: "[slug] <Übungsnummer>: <Lösung>"
---

# /check: Übungen korrigieren

Lösung: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, D, E).

## Übung finden

Übungsnummer `N.M` → Kapitel `N` in `books/<slug>/chapters/`, Callout mit Titel „Übung N.M“ (bzw.
in der Buchsprache). Lies Aufgabe, Hinweise und Musterlösung. Ohne Nummer aus dem Kontext
erschließen oder kurz nachfragen.

## Korrigieren

- **Genau prüfen, nicht nur mit der Musterlösung vergleichen.** Andere richtige Lösungen sind
  richtig. Bei Rechnungen und Code selbst nachrechnen bzw. ausführen; bei Sprachen auf Grammatik,
  Rechtschreibung, Akzente und Natürlichkeit achten.
- Rückmeldung: erst was richtig ist, dann jeder Fehler mit Erklärung, **warum** es falsch ist und
  wie es richtig geht. Bei mehreren Fehlern gleicher Ursache die Ursache benennen, nicht jeden
  Fehler einzeln. Ehrlich, freundlich, ohne Übertreibung.
- Liegt der Fehler an einer unklaren Aufgabe oder Musterlösung, das offen sagen und die Übung per
  `/revise`-Vorgehen korrigieren.
- Bei deutlichen Schwierigkeiten eine kurze Zusatzaufgabe im Chat anbieten.

## Merken (privat)

- `../learn-anything-private/books/<slug>/exercises.md`: Datum, Übung, Ergebnis (richtig /
  teilweise / falsch), Fehler, Ursache.
- **Fehlermuster** erkennen: Taucht dieselbe Ursache zum zweiten Mal auf, in `LEARNER.md` unter
  „Schwächen und wiederkehrende Fehler“ eintragen, mit Konsequenz fürs Buch (z.B.
  „Wiederholungsbox in Kapitel 6, zusätzliche Übung zu X“). Diese Einträge lesen Author und
  Exercise Designer bei späteren Kapiteln.
- Ist ein Muster so deutlich, dass schon veröffentlichte Kapitel helfen sollten, dem Lerner eine
  Ergänzung vorschlagen (Wiederholungsbox oder Zusatzübung, allgemein formuliert).
- Fortschritt (welche Übungen gemacht) in `LEARNER.md` aktualisieren. Privates Repo committen und
  pushen.
