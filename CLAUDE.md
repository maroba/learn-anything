# learn-anything

Claude schreibt hier Lehrbücher zu beliebigen Themen und veröffentlicht sie auf GitHub Pages
(https://maroba.github.io/learn-anything/). Während der Lerner liest, beantwortet Claude
parallel im Chat Fragen und überarbeitet das Buch. Hintergrund: [VISION.md](VISION.md),
Architektur und Entscheidungen: [DESIGN.md](DESIGN.md). Neue Grundsatzentscheidungen dort im
Entscheidungslog nachtragen.

Mit dem Lerner wird Deutsch gesprochen. Die Bücher sind in der Sprache geschrieben, die in
ihrer `book.yml` unter `language` steht.

## Zwei Repos, strikte Trennung

- **Dieses Repo ist öffentlich.** Hier liegen Tooling, Buchtexte und Buch-Metadaten.
- **Alles über den Lerner** (Profil, Vorwissen, Einstufung, Fragen, Übungslösungen, Fehler)
  gehört ins private Repo `maroba/learn-anything-private`, das neben diesem Repo unter
  `../learn-anything-private` ausgecheckt sein muss. Fehlt es, mit `add_repo` einbinden und dorthin
  klonen, bevor an einem Buch gearbeitet wird.
- Auch indirekt nichts Persönliches ins öffentliche Repo schreiben: keine Formulierungen wie
  „der Lerner verwechselt ständig …“ in `progress.md`, Commit-Messages oder Buchtexten.
  Leserfrage-Boxen im Buch sind anonym und allgemein formuliert.
- Ein pre-commit-Hook (`.githooks/`) und die CI verweigern Dateien wie `LEARNER.md`. Den Hook nie
  mit `--no-verify` umgehen.

## Commands, Agents, Skills

Der Lebenszyklus eines Buchs (Details in DESIGN.md, Abschnitt 6):

| Command | Zweck |
|---|---|
| `/new-book <Thema>` | Interview, Buch anlegen, Einstufungstest, Recherche |
| `/outline` | Kapitelplan entwerfen und abstimmen |
| `/sample` | Probekapitel schreiben und veröffentlichen |
| `/feedback` | Stil anhand des Probekapitels abstimmen, Einigungen in STYLE.md |
| `/write [n\|next\|all]` | Kapitel schreiben und einzeln veröffentlichen |
| `/ask` | Frage beim Lesen beantworten, ggf. einarbeiten (auch ohne `/ask`, z.B. bei „📍“-Referenzen) |
| `/revise` | Änderungswunsch umsetzen, mit Änderungsvermerk |
| `/check` | Übungslösung korrigieren, Fehlermuster merken |
| `/status` | Überblick und nächster Schritt |

Die Commands liegen als Skills unter `.claude/skills/<name>/SKILL.md` und stützen sich auf zwei
gemeinsame Dokumente, die vor der Arbeit an einem Buch zu lesen sind:

- `.claude/docs/workflow.md`: Buchauswahl, Kontext laden, Kapitel-Pipeline, Lernerprofil,
  Veröffentlichen, Status
- `.claude/docs/book-format.md`: technisches Format der Kapitel (Anker, Callouts, Übungen,
  `lang`-Auszeichnung, Änderungsvermerke)

Agents (`.claude/agents/`): `researcher`, `author`, `didactics-reviewer`, `technical-reviewer`,
`consistency-editor`, `exercise-designer`. Archetyp-Skills mit allgemeiner Didaktik:
`.claude/skills/archetype-<archetyp>/`. `distill-domain-skill` macht aus einem fertigen Buch einen
neuen Skill.

`python3 scripts/check_claude_config.py` prüft das Front Matter aller Agents und Skills (läuft auch
in der CI). Beschreibungen mit Doppelpunkt in Anführungszeichen setzen.

## Aufbau

```
_extensions/learn-anything/  Quarto-Format für alle Bücher: Stil, Schriften, ¶-Referenzen, Änderungsvermerke
templates/book/              Vorlage für neue Bücher (private Vorlage: ../learn-anything-private/templates/book/)
books/<slug>/                ein Quarto-Book-Projekt pro Buch, dazu Arbeitsdateien (siehe DESIGN.md, Abschnitt 5)
library/                     Bibliotheks-Startseite, listet alle Bücher mit `published: true`
scripts/new_book.py          legt ein neues Buch an (öffentlich und privat)
scripts/build.py             baut alles nach _site/
```

`_extensions` in `books/<slug>/` und `library/` ist ein Symlink auf das gemeinsame `_extensions/`.

## Bauen und veröffentlichen

```bash
python3 scripts/new_book.py <slug> --title "…" --topic "…" --lang de [--target-lang el] --archetype languages
python3 scripts/build.py --book <slug>   # ein Buch schnell prüfen (auch unveröffentlicht)
python3 scripts/build.py                 # alles, wie die CI
```

- **Veröffentlichen heißt: nach `main` pushen.** Claude darf direkt nach `main` pushen
  (`git push origin HEAD:main`). Die Action `.github/workflows/publish.yml` baut und deployt dann
  in ein bis zwei Minuten.
- Vor jedem Push `scripts/build.py --book <slug>` ausführen. Es darf keine Fehler und keine neuen
  Warnungen geben. Nie einen kaputten Stand veröffentlichen.
- Änderungen im privaten Repo ebenfalls committen und dort nach `main` pushen, sonst sind sie
  mit dem Container verloren.

## Konventionen für Buchtexte

- Kapitel liegen in `books/<slug>/chapters/NN-kurzname.qmd` und werden in `_quarto.yml` unter
  `book.chapters` eingetragen.
- **Änderungsvermerk:** Jede inhaltliche Überarbeitung eines veröffentlichten Kapitels bekommt
  einen Eintrag im Front Matter; die Box oben im Kapitel entsteht daraus automatisch:

  ```yaml
  changes:
    - date: 2026-09-28
      note: "Beispiel zum Aorist ergänzt (Abschnitt 3.2)"
  ```

- **Stabile Anker:** Abschnitte bekommen explizite IDs (`## Der Aorist {#sec-aorist}`), damit Links
  und ¶-Referenzen nach Umformulierungen der Überschrift gültig bleiben.
- **¶-Referenzen** aus dem Chat sehen so aus:

  ```
  📍 Buch › 3 Verben › 3.2 Der Aorist › Absatz 4
  https://maroba.github.io/learn-anything/<slug>/chapters/03-verben.html#sec-aorist-p4
  > Textausschnitt …
  ```

  Die URL führt zu `books/<slug>/chapters/03-verben.qmd`. `sec-aorist` ist der Abschnitt,
  `p4` der vierte Block darin (Absatz, Listenpunkt, Tabelle, Callout, Codeblock). Die Stelle im
  Quelltext immer über den Textausschnitt verifizieren, denn die Zählung verschiebt sich bei
  Änderungen.
- Arbeitsdateien des Buchs (`STYLE.md`, `DOMAIN.md`, `outline.md`, `glossary.md`, `sources.md`,
  `progress.md`) vor dem Schreiben lesen und aktuell halten. `STYLE.md` ist verbindlich.
- Keine Übernahmen aus existierenden Lehrbüchern. Unsicheres markieren statt souverän behaupten.
