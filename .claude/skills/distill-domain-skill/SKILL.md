---
name: distill-domain-skill
description: "Macht aus den Erfahrungen eines learn-anything-Buchs (DOMAIN.md, STYLE.md, Review-Befunde, typische Fragen) einen wiederverwendbaren Skill, entweder einen neuen Archetyp-Skill oder eine Verbesserung eines bestehenden. So lernt das Projekt dazu. Verwenden, wenn ein Buch fertig ist, ein neuer Archetyp gebraucht wird oder der Nutzer darum bittet."
argument-hint: "<slug> [archetyp]"
---

# Domänenwissen als Skill festhalten

Argumente: $ARGUMENTS

## Sammeln

Aus dem Buch `books/<slug>/`: `DOMAIN.md`, `STYLE.md` (Vereinbarungen im Verlauf), `progress.md`
(wiederkehrende Review-Befunde), `outline.md`, Kapitelstruktur. Aus dem privaten Repo
`questions.md` und `exercises.md`: welche Fragen und Fehler kamen häufig, welche Erklärungen
haben funktioniert?

## Verallgemeinern

Trenne:

- **Archetyp-Wissen:** gilt für alle Themen dieser Art (alle Sprachen, alle Mathematikgebiete).
  → `.claude/skills/archetype-<archetyp>/SKILL.md` anlegen oder ergänzen.
- **Themenwissen:** gilt nur für dieses Thema (Griechisch, Galois-Theorie), ist aber für künftige
  Bücher zum selben oder einem nahen Thema wertvoll (z.B. ein zweites Griechischbuch auf höherem
  Niveau). → `.claude/skills/topic-<thema>/SKILL.md` anlegen.
- **Persönliches:** Vorlieben dieses einen Lerners gehören in keinen Skill.

Nur aufnehmen, was sich bewährt hat oder aus Fehlern gelernt wurde, nicht bloß, was in DOMAIN.md
schon stand. Konkret formulieren („Aorist vor Imperfekt einführen, weil …“).

## Skill-Format

```markdown
---
name: archetype-<archetyp>          # bzw. topic-<thema>
description: <wofür, wann lesen; mit Archetyp- bzw. Themenname>
user-invocable: false
---
```

Aufbau wie `.claude/skills/archetype-languages/SKILL.md`: Grundhaltung, Lehrreihenfolge,
typische Stolpersteine, Übungsformen, Prüfpunkte für Reviewer. Unter 300 Zeilen.

Neue Archetypen zusätzlich in `scripts/new_book.py` (`ARCHETYPES`) und `.claude/skills/new-book/SKILL.md`
eintragen. Die Agents finden Archetyp-Skills über den Pfad
`.claude/skills/archetype-<archetyp>/SKILL.md`; Themen-Skills in der `DOMAIN.md` des neuen Buchs
verlinken.

## Abschluss

Dem Nutzer die wichtigsten neuen Erkenntnisse zeigen und bestätigen lassen, dann committen und
nach `main` pushen.
