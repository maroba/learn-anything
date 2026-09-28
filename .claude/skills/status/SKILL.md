---
name: status
description: "Zeigt den Stand aller learn-anything-Bücher oder eines einzelnen Buchs, mit Kapiteln, offenen Punkten und dem sinnvollen nächsten Schritt. Verwenden bei „Wo stehen wir?“, zu Beginn einer neuen Session oder mit /status."
argument-hint: "[slug]"
---

# /status: Überblick

Argument: $ARGUMENTS

## Ohne Slug: alle Bücher

Für jedes Buch unter `books/`: Titel, Status aus `book.yml`, veröffentlichte Kapitel / Kapitel laut
Outline, Link. Kompakt als Tabelle.

## Mit Slug: ein Buch

Aus `book.yml`, `outline.md`, `progress.md`, `_quarto.yml` und dem privaten Repo
(`questions.md`, `exercises.md`, `LEARNER.md`):

- Status und Phase, Link zum Buch
- Kapitel: veröffentlicht, im Entwurf, geplant (mit Nummer und Titel)
- offene TODOs und ungeklärte Punkte aus `progress.md`
- letzte Aktivität, Anzahl Fragen und Übungen, erkannte Schwerpunkte aus dem
  Lernerprofil (nur im Chat, das Profil ist privat)
- **ein** konkreter Vorschlag für den nächsten Schritt (z.B. „/write next: Kapitel 5, Der Aorist“)

Prüfe nebenbei die Umgebung: ist das private Repo unter `../learn-anything-private` ausgecheckt,
ist Quarto verfügbar (`quarto --version`)? Probleme melden.

Nichts ändern, nichts committen.
