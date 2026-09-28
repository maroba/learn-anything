# Design: learn-anything

Dieses Dokument hält die Architektur- und Designentscheidungen fest, die aus der Diskussion
über [VISION.md](VISION.md) hervorgegangen sind. Jede Claude-Code-Cloud-Session startet in
einem frischen Container. Was hier nicht steht, ist für spätere Sessions verloren. Neue
Entscheidungen bitte hier nachtragen (Abschnitt „Entscheidungslog“).

---

## 1. Grundprinzip: Der Zustand liegt im Repo

Ein Buch besteht nicht nur aus seinem Text, sondern auch aus seinem **Zustand**:
Stilvereinbarung, Outline, Glossar, Quellen, Fortschritt und das Lernerprofil. Alles davon
wird als Datei versioniert, damit jede Session nahtlos weiterarbeiten kann.

## 2. Repositories

| Repo | Sichtbarkeit | Inhalt |
|---|---|---|
| `maroba/learn-anything` | öffentlich | Tooling (`.claude/`), Quarto-Projekt, Buchtexte, Buch-Metadaten. Wird auf GitHub Pages veröffentlicht. |
| `maroba/learn-anything-private` | privat | Alles über den Lerner: Lernerprofile, Einstufungstests, eigene Übungslösungen, Fortschritt, Notizen. |

**Regel:** Informationen über den Lerner (Vorwissen, Schwächen, Fehler, gestellte Fragen,
Lösungsversuche) landen **niemals** im öffentlichen Repo. Ein Hook prüft vor Commits, dass
keine Lernerdateien ins öffentliche Repo geraten.

Jede Session, die an einem Buch arbeitet, braucht beide Repos ausgecheckt.

## 3. Deployment

- Claude darf **direkt nach `main`** des öffentlichen Repos pushen, damit Änderungen
  schnell live sind.
- Eine GitHub Action baut bei jedem Push nach `main` die Quarto-Bibliothek und deployt sie
  auf GitHub Pages (Settings → Pages → Source: „GitHub Actions“).
- Vor dem Push baut Claude lokal testweise, damit kein kaputter Stand live geht.

## 4. Technik

- **Quarto** als Buchsystem: Theorem- und Beweis-Umgebungen, Callouts, Querverweise,
  ausführbarer Code, PDF/EPUB-Export, UI in vielen Sprachen, Unicode und RTL.
- **Mehrere Bücher in einem Repo** mit einer Bibliotheks-Startseite, die alle Bücher listet.
  Jedes Buch ist ein eigenes Quarto-Book-Projekt; die CI setzt alles unter `_site/<slug>/`
  zusammen.
- Ein **SessionStart-Hook** installiert Quarto (und weitere Tools) im Cloud-Container.

## 5. Verzeichnisstruktur (Entwurf)

Öffentliches Repo:

```
.claude/
  commands/         # Slash-Commands (/new-book, /write, …)
  agents/           # Subagents (Researcher, Author, Reviewer, …)
  skills/           # Domänen-Archetypen und wiederverwendbare Skills
  hooks/
CLAUDE.md           # Grundregeln für alle Sessions
DESIGN.md
index.qmd           # Bibliotheks-Startseite
shared/             # gemeinsame Quarto-Filter, JS, CSS (¶-Referenzen, Audio, …)
books/<slug>/
  _quarto.yml
  book.yml          # Thema, Buchsprache, Zielsprache, Niveau, Status
  STYLE.md          # ausgehandelter Stil (Ergebnis der Probekapitel-Runde)
  DOMAIN.md         # themenspezifisches Didaktik-Wissen aus der Recherche
  outline.md        # Kapitel, Lernziele, Abhängigkeiten, Lesezeit
  glossary.md       # Begriffe und Notation
  sources.md        # Quellen und Standardwerke
  progress.md       # Stand der Kapitel, offene TODOs
  chapters/NN-*.qmd
```

Privates Repo:

```
books/<slug>/
  LEARNER.md        # Ziele, Vorwissen, Zeitbudget, Stärken und Schwächen
  placement.md      # Einstufungstest und Ergebnis
  questions.md      # gestellte Fragen und wie sie behandelt wurden
  exercises.md      # Lösungsversuche und Korrekturen
```

## 6. Lebenszyklus eines Buchs und Commands

| Phase | Command | Ergebnis |
|---|---|---|
| Interview | `/new-book <Thema>` | Ziel, Vorwissen, Tiefe, Zeitbudget, Buchsprache, Tonfall, Übungsart. Legt `book.yml` und `LEARNER.md` an. |
| Einstufung | (Teil von `/new-book`) | Kurzer Einstufungstest; das Ergebnis geht in `LEARNER.md`. |
| Recherche | (automatisch) | `DOMAIN.md`, `sources.md` |
| Outline | `/outline` | `outline.md` inkl. Abhängigkeitsgraph |
| Probekapitel | `/sample` | Ein repräsentatives Kapitel (nicht Kapitel 1), sofort live. Optional zwei Stilvarianten zur Auswahl. |
| Iteration | `/feedback <…>` | Anpassung; jede Einigung wird in `STYLE.md` festgeschrieben. |
| Schreiben | `/write [kapitel\|all]` | Schreiben, Review, Publizieren; über mehrere Sessions fortsetzbar dank `progress.md`. |
| Begleitung | `/ask`, `/revise` | Fragen beantworten, einarbeiten, überarbeiten |
| Übungen | `/check <Nr>: <Lösung>` | Lösung korrigieren, Fehlermuster privat merken |
| Überblick | `/status` | Stand des Buchs |

## 7. Agents

1. **Researcher**: Themenlandschaft, Curricula, typische Stolpersteine, Quellen. Erzeugt
   `DOMAIN.md` und `sources.md`.
2. **Author**: schreibt strikt nach `STYLE.md`, `glossary.md` und `LEARNER.md`.
3. **Didactics Reviewer**: Reihenfolge der Voraussetzungen, kognitive Last, Beispiele,
   Passung von Übungen und Lernzielen.
4. **Technical Reviewer / Fact-Checker**: *rechnen statt glauben*. Code ausführen, Umformungen
   mit SymPy prüfen, Behauptungen gegen Quellen abgleichen.
5. **Consistency Editor**: Notation, Terminologie, Querverweise, Glossar.
6. **Exercise Designer**: Übungen mit gestuften Hinweisen und ausklappbaren Lösungen.

Ablauf pro Kapitel: Author → Didactics- und Technical-Reviewer (parallel) → Author überarbeitet
→ Editor → Commit und Publish. Kapitel können parallel geschrieben werden, sobald Glossar und
Notation feststehen.

## 8. Selbstlernende Domänen-Skills

- **Ebene 1: Archetypen** als feste Skills: Sprachen, formale Wissenschaften, Naturwissenschaften,
  Programmieren, Geistes-/Sozialwissenschaften, praktische Fertigkeiten.
- **Ebene 2: themenspezifische Recherche** pro Buch → `DOMAIN.md`.
- Ein Meta-Skill kann aus einer bewährten `DOMAIN.md` einen neuen wiederverwendbaren Skill in
  `.claude/skills/` machen.

## 9. Parallel lesen und reden

- **Kanal:** Der Lerner liest im Browser und spricht parallel in der Claude-App mit einer
  Cloud-Session. (Ein GitHub-Issue-Kanal über die Claude GitHub Action ist vorerst nicht geplant.)
- **Stabile Referenzen:** Jeder Absatz und jede Gleichung bekommt eine stabile ID. Ein ¶-Symbol
  beim Hovern kopiert z.B. `griechisch/03-verben#p-3-2-4` plus Textausschnitt in die
  Zwischenablage, zum Einfügen in den Chat.
- **Umgang mit Fragen:** (a) nur im Chat beantworten, (b) als „Leserfrage“-Box ins Kapitel
  einarbeiten, (c) das Kapitel umschreiben, wenn eine didaktische Lücke sichtbar wird.
  Jede Frage wird im privaten Repo in `questions.md` notiert und fließt in spätere Kapitel ein.
- **Änderungsvermerke:** Pro Kapitel ein sichtbarer Hinweis auf die letzten Überarbeitungen.

## 10. Lern-Features (alle gewünscht)

1. Einstufungstest vor der Outline
2. Übungen im Chat lösen; Claude korrigiert und merkt sich Schwächen (privat), das Buch wird
   dadurch adaptiv (Wiederholungsboxen, angepasste spätere Kapitel)
3. Spaced Repetition: Anki-Decks pro Kapitel (`genanki`)
4. Audio für Sprachen über die Web Speech API des Browsers
5. Schrittweise Immersion: Buchsprache und Zielsprache getrennt konfigurierbar; die
   Erklärsprache kann sich im Verlauf zur Zielsprache verschieben
6. Abhängigkeitsgraph der Kapitel auf der Startseite, verschiedene Lernpfade
7. Interaktive Visualisierungen (Plots, Widgets, Mermaid, TikZ)
8. Vertrauensmarker und Quellen bei unsicheren Stellen
9. Mehrere Bücher mit Bibliotheks-Startseite

## 11. Qualität und Recht

- Keine Übernahmen aus existierenden Lehrbüchern; Bilder selbst erzeugt oder frei lizenziert.
- Unsicheres wird markiert statt souverän behauptet.

## 12. Erstes Testthema: Neugriechisch

Besonderheiten, die das System dabei abdecken muss:

- Entschieden: **Neugriechisch**. Das Interview soll trotzdem generell klären, welche Variante
  eines Themas gemeint ist (bei Griechisch: Neu-, Altgriechisch, Koine).
- Schrift und Alphabet als eigenes Lernproblem (interaktive Übungen, frühe Anki-Karten).
- Audio: Browser haben meist eine `el-GR`-Stimme; für Altgriechisch gibt es keine, und die
  rekonstruierte Aussprache ist umstritten.
- Griechische Eingabe in Übungen: Bildschirmtastatur oder Transliterations-Umwandlung.
- Polytonische Schrift braucht eine passende Schriftart (z.B. Gentium, Noto Serif).
- Schrittweise Immersion von Deutsch zu Griechisch.

## 13. Umsetzungsplan

1. **Infrastruktur** (erledigt, 2026-09-28): Quarto-Bibliothek, Pages-Deployment, ¶-Referenzen, Änderungsvermerke,
   SessionStart-Hook, `CLAUDE.md`, Schutz-Hook für Lernerdaten.
2. **Commands, Agents, Skills** (erledigt, 2026-09-28): siehe Abschnitte 6–8; zunächst der Archetyp „Sprachen“.
3. **Lern-Features:** Einstufungstest, Anki-Export, Audio, Eingabehilfe, Abhängigkeitsgraph,
   interaktive Übungen.
4. **Echter Durchlauf mit Griechisch** und Verbesserungen aus den Erfahrungen.

## 14. Entscheidungslog

| Datum | Entscheidung |
|---|---|
| 2026-09-28 | Claude darf direkt nach `main` pushen. |
| 2026-09-28 | Fragekanal: Claude-App-Session parallel zum Lesen (kein Issue-Kanal vorerst). |
| 2026-09-28 | Buchsystem: Quarto. |
| 2026-09-28 | Mehrere Bücher in einem Repo. |
| 2026-09-28 | Bücher öffentlich; Lernerdaten im privaten Repo `maroba/learn-anything-private`. |
| 2026-09-28 | Alle Lern-Features aus Abschnitt 10 sind gewünscht. |
| 2026-09-28 | Erstes Testthema: Neugriechisch. |
| 2026-09-28 | Quarto-Version fest auf 1.10.18 (CI und SessionStart-Hook). |
| 2026-09-28 | Gemeinsames Quarto-Format `learn-anything-html` als Extension in `_extensions/`; jedes Buch verlinkt es per Symlink. |
| 2026-09-28 | ¶-Referenzen: IDs `<abschnitt>-p<n>` werden im Browser vergeben, die kopierte Referenz enthält zusätzlich einen Textausschnitt, über den Claude die Stelle im Quelltext eindeutig findet. Auf Touch-Geräten erscheint das ¶ nach Antippen des Absatzes. |
| 2026-09-28 | Änderungsvermerke über `changes:` im Front Matter; „neu seit letztem Besuch“ per localStorage im Browser des Lesers (nichts davon landet im Repo). |
| 2026-09-28 | Vorlagen für die privaten Dateien liegen im privaten Repo (`templates/book/`). |
| 2026-09-28 | Commands als Skills in `.claude/skills/`, gemeinsame Abläufe in `.claude/docs/workflow.md`, technisches Kapitelformat in `.claude/docs/book-format.md`. |
| 2026-09-28 | Zusätzlicher Command `/check` für Übungslösungen im Chat (Grundlage für das adaptive Buch). |
| 2026-09-28 | Pipeline: Author setzt `EXERCISE`-Platzhalter, Exercise Designer füllt sie, dann Reviews parallel. |
| 2026-09-28 | Feste Formate, die spätere Werkzeuge auslesen: `outline.md` (Datei, Lernziele, Voraussetzungen, Lesezeit) für den Abhängigkeitsgraphen, `.vocab`-Tabellen für Anki, `lang`-Auszeichnung für Audio. |
| 2026-09-28 | Fragen beim Lesen: Antwort im Chat zuerst; Einarbeiten (Leserfrage-Box oder Überarbeitung) nur nach kurzer Rückfrage, außer der Lerner hat eine feste Vorliebe festgelegt. |
| 2026-09-28 | Wortschatz in zwei Stufen: `.vocab` = Kernwortschatz (höchstens ca. 50–60 pro Kapitel, wird zu Anki-Karten), `.vocab-text` = eingeklappter Wortschatz zum Text (keine Karten). Anlass: Didaktik-Review des ersten Probekapitels. |
| 2026-09-28 | Audio: vorab erzeugte MP3s (LuvVoice oder OpenAI, Wahl per Blindtest) für Kernwortschatz und Texte in der Zielsprache, committet und per Hash zwischengespeichert; ▶-Knopf im Buch, Browser-Sprachausgabe als Rückfallebene. API-Schlüssel nur als Umgebungsvariablen der Cloud-Umgebung. |
| 2026-09-28 | Neugriechisch: Audio mit den nativen el-GR-Stimmen von LuvVoice (Athina für Vokabeln und Texte, Dialoge abwechselnd Athina/Nestoras über `audio.dialogue-voice`). Auswahl nach technischen Kriterien auf Wunsch des Lerners. |
