---
name: outline
description: "Erstellt oder überarbeitet die Outline (Kapitelplan mit Lernzielen, Voraussetzungen und Lesezeit) eines learn-anything-Buchs und stimmt sie mit dem Lerner ab. Verwenden nach /new-book oder wenn der Nutzer den Aufbau des Buchs ändern möchte."
argument-hint: "[slug] [Änderungswunsch]"
---

# /outline: Kapitelplan entwerfen und abstimmen

Argumente: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, E, F).

## Entwerfen

Lade den Kontext des Buchs (workflow.md, B), besonders `DOMAIN.md` (bewährte Lehrreihenfolge,
Stolpersteine) und `LEARNER.md` (Ziel, Vorwissen, Einstufung, Zeitbudget, Umfang).

Leitfragen:

- Führt jedes Kapitel sichtbar zum Ziel des Lerners? Was er schon kann, wird nur kurz wiederholt.
- Früh ein Erfolgserlebnis: Nach den ersten ein, zwei Kapiteln kann er etwas Echtes (einen Satz
  sagen, ein Programm laufen lassen, einen Satz beweisen).
- Voraussetzungen vor ihrer Verwendung, Spiralprinzip: Wichtiges kehrt vertieft wieder.
- Kapitelgröße nach book-format.md; Gesamtumfang nach Zeitbudget und Wunsch aus dem Interview.
- Bei Sprachbüchern: einen **Immersionsplan** vorschlagen (ab welchem Kapitel was in der
  Zielsprache erklärt wird), siehe `archetype-languages`.

## Format von `books/<slug>/outline.md`

Das Format ist verbindlich, weil Werkzeuge es auslesen (Abhängigkeitsgraph, Fortschritt):

```markdown
# Outline

Kurzbeschreibung des Gesamtbogens in zwei, drei Sätzen.

## Teil I: Grundlagen

### 01 Titel des Kapitels
- **Datei:** 01-kurzname
- **Lernziele:** Der Lerner kann …; … ; …
- **Voraussetzungen:** keine
- **Lesezeit:** 30 min
- **Inhalt:** Stichpunkte zu Abschnitten, Leitbeispiel, Übungsideen

### 02 …
- **Voraussetzungen:** 01
```

Teile (`## Teil …`) nur bei mehr als etwa acht Kapiteln. Voraussetzungen als Kapitelnummern, durch
Komma getrennt. Lernziele als überprüfbare Fähigkeiten formulieren („kann … bilden“, nicht „kennt …“).

Lege außerdem in `glossary.md` die zentralen Begriffe und Konventionen an, die das ganze Buch
betreffen (Notation, Transliteration, feste Übersetzungen), damit spätere Kapitel parallel
geschrieben werden können.

## Abstimmen

Zeige dem Lerner die Outline kompakt im Chat (Kapitelnummer, Titel, ein Satz Inhalt, Lesezeit,
Gesamtumfang) und erkläre in zwei, drei Sätzen die Grundidee des Aufbaus. Frage gezielt nach dem,
was am ehesten strittig ist (Tempo, Schwerpunkte, Reihenfolge). Änderungswünsche einarbeiten, bis
er zufrieden ist.

## Abschluss

- Wähle das Probekapitel vor (repräsentativ, mit echtem Inhalt, nicht Kapitel 1) und begründe die
  Wahl in einem Satz.
- Status `sample`, beide Repos committen und pushen.
- Vorschlagen, mit dem Probekapitel weiterzumachen (`/sample`).

Bei späteren Änderungen an der Outline (z.B. aus `/revise`): bereits geschriebene Kapitel und
`progress.md` mitziehen, Kapitelnummern und Dateinamen nur ändern, wenn es sich nicht vermeiden
lässt (URLs und ¶-Referenzen hängen daran).
