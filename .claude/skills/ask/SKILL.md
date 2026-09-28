---
name: ask
description: "Beantwortet eine Frage des Lerners zu einem learn-anything-Buch, oft mit einer ¶-Referenz auf eine Textstelle. Antwortet sofort im Chat und schlägt bei Bedarf vor, die Antwort als Leserfrage-Box einzuarbeiten oder das Kapitel zu verbessern. Verwenden bei jeder inhaltlichen Frage zum Stoff eines Buchs, auch ohne ausdrückliches /ask, z.B. wenn eine Nachricht mit „📍“ beginnt."
argument-hint: "[¶-Referenz] <Frage>"
---

# /ask: Fragen beim Lesen

Frage: $ARGUMENTS

Grundlagen: `.claude/docs/workflow.md` (A, B, D, E), `.claude/docs/book-format.md`.

Der Lerner liest gerade und will weiterlesen. **Die Antwort im Chat hat Vorrang**; alles andere
passiert danach und kurz.

## 1. Stelle finden

Eine ¶-Referenz sieht so aus:

```
📍 Buch › 3 Verben › 3.2 Der Aorist › Absatz 4
https://maroba.github.io/learn-anything/<slug>/chapters/03-verben.html#sec-aorist-p4
> Textausschnitt …
```

URL → `books/<slug>/chapters/03-verben.qmd`, Abschnitt `sec-aorist`. Die genaue Stelle über den
Textausschnitt suchen (Grep), denn die Absatzzählung kann sich verschoben haben. Ohne Referenz aus
dem Gesprächskontext erschließen, welche Stelle gemeint ist; nur im Zweifel nachfragen.

## 2. Antworten

- Lies die Stelle mit Umgebung, `LEARNER.md` (was weiß er schon?) und bei Bedarf `glossary.md`.
- Antworte im Chat: direkt, auf seinem Niveau, in der Sprache, in der er fragt, mit einem Beispiel,
  wenn es hilft. Knapp, aber vollständig. Bei fachlich heiklen Fragen lieber nachrechnen bzw.
  nachschlagen als aus dem Gedächtnis antworten; Unsicherheit offen sagen.
- Greift die Frage Stoff späterer Kapitel vor: kurz beantworten und sagen, wo es ausführlich kommt.

## 3. Einarbeiten?

Entscheide, welche Behandlung passt:

- **(a) Nur im Chat:** persönliche Neugier, Randthema, oder im Kapitel schon gut erklärt und nur
  überlesen.
- **(b) Leserfrage-Box:** Die Frage würden sich viele stellen, und die Antwort bereichert das Kapitel
  (Markup in book-format.md, allgemein formuliert, an der passenden Stelle).
- **(c) Kapitel verbessern:** Die Frage zeigt eine echte Lücke oder eine missverständliche Stelle.
  Dann die Erklärung selbst verbessern, nicht nur eine Box anhängen.

Bei (b) und (c): in **einer** Zeile vorschlagen („Soll ich das als Leserfrage-Box in 3.2
einbauen?“). Hat der Lerner eine Vorliebe festgelegt (in `LEARNER.md`, Abschnitt Vorlieben, z.B.
„Fragen immer einarbeiten“), ihr ohne Rückfrage folgen. Umsetzung wie bei `/revise` (mit
`changes`-Eintrag, veröffentlichen). Kleine Änderungen direkt, größere über den `author`.

## 4. Merken (privat)

- In `../learn-anything-private/books/<slug>/questions.md` eine Zeile: Datum, Stelle, Frage (kurz),
  Behandlung (a/b/c).
- Zeigt die Frage eine Wissenslücke oder ein Missverständnis, in `LEARNER.md` unter Schwächen
  notieren; das beeinflusst spätere Kapitel und Wiederholungen.
- Privates Repo committen und pushen. Das darf gebündelt passieren, aber spätestens am Ende der
  Antwortrunde, damit nichts mit dem Container verloren geht.
