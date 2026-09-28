---
name: archetype-languages
description: "Didaktik für Sprachlehrbücher in learn-anything (Archetyp „languages“). Lehrreihenfolge, Aussprache, Wortschatz, Grammatik, Immersion, Übungsformen und Prüfpunkte. Lesen, bevor an einem Buch mit archetype languages geplant, geschrieben oder reviewt wird."
user-invocable: false
---

# Archetyp: Sprachen lernen

Allgemeine Didaktik für alle Sprachbücher. Was nur für eine bestimmte Sprache gilt, gehört in die
`DOMAIN.md` des Buchs. Begriffe: **Buchsprache** = Erklärsprache (`language`), **Zielsprache** =
die zu lernende Sprache (`target-language`).

## Grundhaltung

- **Kommunikativ mit expliziter Grammatik:** Der Lerner soll von Anfang an echte Sätze verstehen
  und bilden, die Grammatik wird aber auch klar erklärt, denn Erwachsene profitieren von Regeln.
  Reihenfolge im Abschnitt: Situation/Dialog → auffällige Form → Regel → Übung.
- **Häufigkeit vor Systematik:** zuerst die häufigsten Wörter, Formen und Wendungen, nicht
  vollständige Paradigmen. Unregelmäßige Formen häufiger Verben früh, auch bevor die Regel dahinter
  erklärt ist.
- **Chunks:** feste Wendungen („Wie geht's?“, „Ich hätte gern …“) als Ganzes lernen, lange bevor
  ihre Grammatik dran ist.
- **Niveau:** am Gemeinsamen Europäischen Referenzrahmen (GER, A1–C2) orientieren. Die Outline
  nennt, welches Niveau am Ende erreicht sein soll; `DOMAIN.md` hält die Kann-Beschreibungen fest.

## Schrift und Aussprache

- **Andere Schrift zuerst:** Hat die Zielsprache eine andere Schrift, ist sie Thema des ersten
  Kapitels oder der ersten beiden. Buchstaben in Gruppen einführen (vertraute, trügerische wie
  griechisch ρ = r, neue), sofort in echten Wörtern lesen lassen (Ortsnamen, Internationalismen).
  Transliteration nur als Stütze am Anfang, dann schrittweise weglassen (im Immersionsplan
  festlegen).
- **Aussprache:** IPA angeben, aber zusätzlich eine Annäherung für Sprecher der Buchsprache
  („wie *th* in englisch *think*“). Betonung immer markieren, wenn die Schrift sie nicht zeigt.
  Laute, die es in der Buchsprache nicht gibt, gesondert üben.
- Jedes Wort und jeder Satz in der Zielsprache wird mit `lang` ausgezeichnet
  (`[καλημέρα]{lang="el"}`), damit Audio-Wiedergabe möglich ist.

## Wortschatz

- Neuer Wortschatz eines Abschnitts in einer **Vokabeltabelle** am Ende des Abschnitts:

  ```markdown
  ::: {.vocab}
  | Griechisch | Aussprache | Deutsch |
  |---|---|---|
  | [το σπίτι]{lang="el"} | [to ˈspiti] | das Haus |
  :::
  ```

  Spaltentitel in der Buchsprache, erste Spalte immer die Zielsprache. Diese Tabellen werden später
  automatisch zu Karteikarten (Anki) verarbeitet. Nomen mit Artikel, Verben in der Grundform
  plus auffälligen Formen, Adjektive in der Grundform.
- **Zwei Stufen:** `.vocab` enthält nur den **Kernwortschatz**, den der Lerner aktiv lernen soll
  (wird zu Anki-Karten). Wörter, die nur zum Verstehen eines Textes oder Dialogs nötig sind, stehen
  eingeklappt als **Wortschatz zum Text** und werden nicht zu Karten:

  ```markdown
  ::: {.callout-note collapse="true" .vocab-text}
  ## Wortschatz zum Text
  | Griechisch | Deutsch |
  |---|---|
  | [το οικόπεδο]{lang="el"} | das Baugrundstück |
  :::
  ```

- **Kernwortschatz pro Kapitel höchstens etwa 50 bis 60 Einträge**, je nach Niveau und
  Zeitbudget. Wortschatz, den der Lerner laut Profil oder aus früheren Kapiteln schon kennt, nicht
  erneut in `.vocab` aufnehmen. Hochfrequente Wörter aus Texten gehören in den Kern, seltene in den
  Textwortschatz.
- Wörter in Wortfeldern und Situationen einführen, nicht alphabetisch. Eselsbrücken über Lehnwörter,
  Fremdwörter und Etymologie nutzen (für Griechisch besonders ergiebig), vor falschen Freunden
  warnen (`.callout-warning`).
- Wortschatz früherer Kapitel in neuen Texten wiederverwenden (Spiralprinzip).

## Grammatik

- Eine Struktur pro Abschnitt. Formen in Tabellen, mit markierten Endungen.
- Vergleiche mit der Buchsprache und mit anderen Sprachen, die der Lerner kann, wo sie helfen;
  Unterschiede, die typische Fehler verursachen, ausdrücklich benennen.
- Fachbegriffe der Grammatik nur so viel wie nötig; beim ersten Auftreten kurz erklären.

## Texte und Kultur

- Jedes Kapitel hat mindestens einen zusammenhängenden Text oder Dialog in der Zielsprache mit
  Übersetzung (eingeklappt) oder Worthilfen. Gern eine durchgehende Geschichte mit wiederkehrenden
  Figuren, wenn STYLE.md das vorsieht.
- Kulturelle Hinweise (Anrede, Höflichkeit, Alltag) als Exkurse, wo sie für die Kommunikation
  zählen.

## Immersionsplan

Wird in `/outline` vorgeschlagen und in STYLE.md festgehalten, z.B.:

1. Anfang: Erklärungen in der Buchsprache, Beispiele in der Zielsprache mit Übersetzung.
2. Ab etwa A1 abgeschlossen: Arbeitsanweisungen und Überschriften der Übungen in der Zielsprache,
   Übersetzungen eingeklappt statt sichtbar, Transliteration nur noch für neue Wörter.
3. Ab etwa A2: einfache Erklärungen in der Zielsprache, Grammatik weiter in der Buchsprache.
4. Später: überwiegend Zielsprache, Buchsprache nur für schwierige Grammatik.

Der Wechsel geschieht schrittweise und wird im Buch angekündigt.

## Übungsformen

Wiedererkennen: Zuordnen, Hörverstehen (sobald Audio verfügbar), richtig/falsch zu einem Text.
Anwenden: Lückentext, Formen bilden, Sätze umformen, Satzbau aus Bausteinen.
Produzieren: Übersetzen in die Zielsprache, auf eine Frage antworten, kurze Texte schreiben,
Dialoge fortsetzen. Produktion frühzeitig und regelmäßig, denn im Chat lässt sie sich korrigieren.

Für Antworten im Chat: Der Lerner darf transliteriert schreiben, wenn er keine Tastatur für die
Zielschrift hat; in der Korrektur die richtige Schreibweise zeigen.

## Prüfpunkte für Reviewer

- Rechtschreibung, Akzente, Diakritika, Groß- und Kleinschreibung in der Zielsprache
- Formen korrekt (Kasus, Genus, Numerus, Tempus, Aspekt); Paradigmentabellen vollständig
- Beispielsätze natürlich und idiomatisch, im passenden Register; nichts, was ein Muttersprachler
  so nie sagen würde
- Aussprache und IPA korrekt, Betonung markiert
- Übersetzungen treffend in beide Richtungen
- Wortschatz nur aus früheren Kapiteln oder in diesem eingeführt (sonst glossiert)
- Kein neues Wort ohne Eintrag in einer Vokabeltabelle
