# Arbeitsabläufe: gemeinsame Bausteine der Commands

Die Commands in `.claude/skills/` verweisen auf die Abschnitte hier. Pfade relativ zum
öffentlichen Repo; das private Repo liegt unter `../learn-anything-private`.

## A. Welches Buch?

Commands nehmen den Slug als erstes Argument. Fehlt er:

1. Gibt es genau ein Buch unter `books/`, dieses nehmen.
2. Sonst das Buch, um das es im bisherigen Gespräch ging.
3. Sonst kurz nachfragen (Liste der Bücher mit Titel und Status aus `book.yml`).

## B. Kontext eines Buchs laden

Vor jeder inhaltlichen Arbeit lesen (was es schon gibt):

| Datei | Wofür |
|---|---|
| `books/<slug>/book.yml` | Thema, Buchsprache, Zielsprache, Archetyp, Status |
| `books/<slug>/STYLE.md` | verbindlicher Stil |
| `books/<slug>/DOMAIN.md` | Didaktik des Themas |
| `books/<slug>/outline.md` | Kapitelplan |
| `books/<slug>/glossary.md` | Begriffe, Notation, Schreibweisen |
| `books/<slug>/progress.md` | Stand der Kapitel |
| `../learn-anything-private/books/<slug>/LEARNER.md` | Lernerprofil (privat!) |
| `.claude/skills/archetype-<archetyp>/SKILL.md` | allgemeine Didaktik des Archetyps, falls vorhanden |

Fehlt das private Repo, zuerst mit `add_repo` (`maroba/learn-anything-private`) einbinden und nach
`../learn-anything-private` klonen. Ohne Lernerprofil wird kein Kapitel geschrieben.

Subagents bekommen im Prompt: Slug, Pfade dieser Dateien und die konkrete Aufgabe. Sie lesen die
Dateien selbst; nicht den Inhalt in den Prompt kopieren.

## C. Kapitel-Pipeline

Für jedes zu schreibende Kapitel:

1. **Entwurf:** `author` schreibt `books/<slug>/chapters/NN-name.qmd` nach `STYLE.md`,
   `.claude/docs/book-format.md`, Outline, Glossar und Lernerprofil. Wo Übungen hingehören,
   setzt er Platzhalter: `<!-- EXERCISE: Lernziel, Art, Schwierigkeit -->`.
2. **Übungen:** `exercise-designer` ersetzt die Platzhalter durch fertige Übungen mit
   Hinweisen und Lösungen.
3. **Review, parallel:** `didactics-reviewer` und `technical-reviewer` prüfen den Entwurf und
   liefern je eine priorisierte Mängelliste (blockierend / sollte / kann). Sie ändern nichts.
4. **Überarbeitung:** `author` (bei Übungsmängeln `exercise-designer`) arbeitet alle blockierenden und sinnvollen weiteren Punkte ein.
   Bei Widerspruch zwischen den Reviewern entscheidet der Command und notiert es in
   `progress.md`. Bei blockierenden Fachfehlern: nach der Überarbeitung erneut
   `technical-reviewer` (höchstens zwei Runden, danach offene Punkte als `.uncertain`-Callout
   markieren und in `progress.md` notieren).
5. **Konsistenz:** `consistency-editor` gleicht Begriffe, Notation, Anker und Querverweise mit
   Glossar und übrigen Kapiteln ab, korrigiert direkt und ergänzt `glossary.md`.
6. **Eintragen:** Kapitel in `_quarto.yml` eintragen, `progress.md` aktualisieren.
7. **Veröffentlichen:** siehe E.

Mehrere Kapitel dürfen parallel durch die Pipeline laufen, wenn Glossar und Notation für ihre
Begriffe feststehen und sie nicht aufeinander aufbauen (Voraussetzungen in `outline.md`).
Ein Kapitel, das auf ein anderes aufbaut, wird erst begonnen, wenn dessen Entwurf fertig ist.

## D. Lernerprofil pflegen (privat)

Alles, was man über den Lerner erfährt, geht ins private Repo unter
`../learn-anything-private/books/<slug>/`:

- `LEARNER.md`: Ziele, Vorwissen, Vorlieben, Stärken, Schwächen (mit Datum und Quelle)
- `placement.md`: Einstufung
- `questions.md`: jede Frage aus `/ask` mit Stelle und Behandlung
- `exercises.md`: Lösungsversuche aus `/check`, Korrekturen, Fehlermuster

Konsequenzen fürs Buch (Wiederholungsbox, neues Beispiel, Überarbeitung) werden im öffentlichen
Repo nur allgemein formuliert: „Beispiel zu X ergänzt“, nie „weil der Lerner X nicht verstand“.
Das gilt auch für Commit-Messages und `progress.md`.

## E. Veröffentlichen

1. `python3 scripts/build.py --book <slug>`: muss fehlerfrei und ohne neue Warnungen laufen.
   Bei Fehlern beheben, nicht veröffentlichen.
2. **Audio** (nur Bücher mit `audio:` in `book.yml`): nach der letzten inhaltlichen Änderung
   `python3 scripts/make_audio.py <slug> --chapter NN` ausführen. Vertont werden nur neue oder
   geänderte Texte. Fehlen die API-Schlüssel (`LUVVOICE_API_KEY`, `OPENAI_API_KEY`), trotzdem
   veröffentlichen (der Browser liest dann selbst vor) und in `progress.md` „Audio fehlt“ notieren.
   Dialogzeilen mit Lücken oder Texte, die nicht vorgelesen werden sollen, bekommen `.no-audio`.
3. Öffentliches Repo: committen, `git push origin HEAD:main`. Auch auf den aktuellen
   Arbeitsbranch pushen, falls die Session einen vorgibt.
4. Privates Repo, falls geändert: in `../learn-anything-private` committen und `git push origin main`.
5. Dem Lerner den Link nennen:
   `https://maroba.github.io/learn-anything/<slug>/chapters/NN-name.html`
   (live ca. eine Minute nach dem Push). Bei `published: false` erscheint das Buch nicht in
   der Bibliothek; `scripts/build.py` baut dann nur lokal. Deshalb spätestens beim Probekapitel
   `published: true` setzen.

Commit-Messages auf Englisch, knapp, ohne persönliche Details über den Lerner.

## F. Status-Übergänge in `book.yml`

`interview` → `research` → `outline` → `sample` → `writing` → `complete`

Jeder Command setzt den Status, wenn er eine Phase abschließt. Ein Buch im Status `writing` kann
weiter mit `/ask`, `/revise`, `/check` bearbeitet werden; `complete` ebenso.
