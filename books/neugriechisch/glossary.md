# Glossar und Notation

<!-- Verbindliche Begriffe, Übersetzungen und Schreibweisen. Wird vor dem Schreiben der Kapitel
     festgelegt und vom Consistency Editor durchgesetzt. Begründungen: DOMAIN.md, Abschnitt
     „Konventionen“. -->

## Schrift und Typografie

- Monotonisches System; im Quelltext NFC-Zeichen mit Tonos (ά = U+03AC), keine polytonischen Oxia-Zeichen.
- Großbuchstaben: Akzent nur bei großem Anfangsbuchstaben (Άρης); keine CSS-Versalien auf griechischem Text.
- Griechisches Fragezeichen als `;`, Hochpunkt `·`, Anführungszeichen in griechischen Texten «…», Apostroph bei Elision `’` (το ’χω).
- Grundform ist die standardneutrale Form nach dem Standardwörterbuch des Triantafyllidis-Instituts; Varianten markieren (αγαπάω/αγαπώ).
- Jedes griechische Wort und jeder griechische Satz mit `lang="el"` auszeichnen.
- **Schluss-ν** (δε/δεν, μη/μην, τη/την, το/τον): nach der Regel der Schulgrammatik – das ν bleibt vor
  Vokal und vor κ π τ ξ ψ μπ ντ γκ τσ τζ, sonst fällt es (δε λέει, την πόλη, τη μητέρα). τον und
  έναν behalten es immer. Einmal in Kapitel 1 erklären und erwähnen, dass viele im Alltag δεν immer
  schreiben; das ist kein Fehler. Im Buch einheitlich nach der Regel.

## Aussprache

- IPA in eckigen Klammern, breite Umschrift, Betonungszeichen ˈ vor der betonten Silbe: [to ˈspiti].
- Allophone notieren: [c ɟ ç ʝ ʎ ɲ ŋ], [z] für σ vor stimmhaften Konsonanten.
- ρ als [r] notieren (einmal erklären: meist getippt wie span. *pero*).
- μπ/ντ/γκ als [b d g]; Pränasalierung [mb nd ŋg] einmal als verbreitete Variante erklären.
- Deutsche Annäherungen immer gleich formulieren:

| Laut | Annäherung im Buch |
|---|---|
| θ | wie engl. *think* |
| δ | wie engl. *this* |
| γ vor a, o, u | wie span. *g* in *agua* |
| γ vor e, i | wie *j* in *ja* |
| χ vor a, o, u | wie *ach* |
| χ vor e, i | wie *ich* |
| ζ | stimmhaft wie *s* in *Rose* |
| σ | immer stimmlos wie *ss* in *Tasse* |
| ρ | getippt wie span. *pero* |
| [c] (κ vor e/i) | wie *k* in *Kiel* mit einem Hauch *j* |
| [ɟ] (γκ/γγ vor e/i) | wie *g* in *Gier* mit einem Hauch *j* |
| [ʎ] (λι vor Vokal) | wie *lj* in *Million*, verschmolzen |
| [ɲ] (νι vor Vokal) | wie span. *ñ* |
| [ŋ] (γ vor κ/γ/χ) | wie *ng* in *Engel*; γγ = [ŋg] |

## Transliteration

- Keine Transliteration als Aussprachehilfe.
- Lateinschrift nur für Eigen- und Ortsnamen, nach ELOT 743 (*Thessaloniki*, *Chania*). **Eingebürgerte deutsche Namen haben Vorrang** (*Athen*, *Neapel*, *Mykene*, *Ithaka*, *Troja*, *Patras*, *Polyphem*); in etymologischen Vergleichen die eingebürgerte deutsche Form (*Philosophie*).

## Grammatikbegriffe

Beim ersten Auftreten mit dem griechischen Fachwort in Klammern.

| Begriff im Buch | griechisch | Anmerkung | eingeführt in |
|---|---|---|---|
| imperfektiver Aspekt | εξακολουθητικός | Vorgang, Wiederholung („Film“) | 02 |
| perfektiver Aspekt | συνοπτικός | Handlung als Ganzes („Foto“) | 02 |
| perfektiver Stamm | – | nicht „Aoriststamm“; das Synonym einmal nennen | 02 |
| Präsens | ενεστώτας | | 01 |
| Imperfekt | παρατατικός | | 04 |
| Aorist | αόριστος | erklärt als Vergangenheit im perfektiven Aspekt | 02 |
| Futur | μέλλοντας | „Futur mit θα“, in beiden Aspekten | 05 |
| να-Form (Konjunktiv) | υποτακτική | „να-Form“ als Arbeitsbegriff | 05 |
| Imperativ | προστακτική | | 09 |
| Vokativ (Anredeform) | κλητική | beim ersten Auftreten „Vokativ (Anredeform)“ | 07 |
| Augment | αύξηση | | 02 |
| Mediopassiv | παθητική φωνή | nicht „Passiv“ | 13 |
| Deponens | αποθετικό ρήμα | | 10 |
| Perfekt, Plusquamperfekt | παρακείμενος, υπερσυντέλικος | | 14 |
| schwache Pronomen (Klitika) | αδύνατοι τύποι | | 08 |
| starke Pronomen | δυνατοί τύποι | | 20 |
| Partizip (auf -μένος) | μετοχή | | 19 |
| Gerundium (auf -οντας) | μετοχή ενεστώτα | | 19 |
| Diskursmarker | – | λοιπόν, έλα, ρε, δηλαδή … | 01 |

## Vokabeltabellen

- Spalten: Griechisch | Aussprache | Deutsch; in einem `::: {.vocab}`-Block (siehe archetype-languages).
- Nomen mit Artikel; auffällige Pluralformen und Betonungswechsel dazu.
- Verben: 1. Person Präsens **und** Aorist (βλέπω, είδα); ab Kapitel 13 auch Aorist des Mediopassivs. Verben ohne perfektiven Stamm (είμαι, έχω, ξέρω): Präsens und Vergangenheit (είμαι, ήμουν).
- Verben der Klasse -άω/-ώ stehen in `.vocab` in der umgangssprachlich häufigeren Form auf -άω (μιλάω); die Variante auf -ώ wird in Kapitel 1 einmal erklärt und nur bei Verben genannt, die überwiegend auf -ώ vorkommen.
- Adjektive: καλός, -ή, -ό.
- Registermarken in der Spalte Deutsch: (umg.), (salopp), (gehoben), (formell).

## Begriffe

| Begriff | Bedeutung / Schreibweise | eingeführt in |
|---|---|---|
| Stamm: imperfektiver / perfektiver Stamm | Das Präsens kommt aus dem imperfektiven, Aorist, Futur (perfektiv) und να-Form aus dem perfektiven Stamm. Nicht „Präsensstamm“, nicht „Aoriststamm“ (nur einmal in 02 als Synonym genannt). „Der zweite Stamm“ nur als Titel-Formel (Kapiteltitel 02, 05), im Fließtext „perfektiver Stamm“. Stämme mit Bindestrich: [διαβασ-]{lang="el"} | 02 |
| Foto / Film | Bild für den Aspekt: perfektiv = Foto (als Ganzes, von außen), imperfektiv = Film (Vorgang, Wiederholung, Gewohnheit, Hintergrund). Immer diese beiden Wörter, keine anderen Metaphern | 02 |
| Vergangenheit im perfektiven Aspekt | Standarderklärung von „Aorist“; „als Ganzes“ heißt nicht „kurz“ | 02 |
| Perfekt-Falle | deutsches/spanisches Perfekt („Hast du … gelesen?“), wo Griechisch den Aorist nimmt | 02 |
| Augment | [ε-]{lang="el"}, bei einigen Verben [η-]{lang="el"} ([ήξερα – ξέραμε]{lang="el"}); steht nur betont; Merkformel „nur, wenn es betont ist“. Das [ή-/εί-]{lang="el"} in [ήρθα, ήπια, είδα, είπα]{lang="el"} gehört zum Stamm und bleibt im Plural ([ήρθαμε, είδαμε]{lang="el"}) | 02 |
| Bauform (unregelmäßige Aoriste) | (A) fester Anfang: zweisilbig, erste Silbe bleibt ([πήγα – πήγαμε]{lang="el"}); (B) Regel aus Kapitel 2: Augment nur betont, Betonung auf der drittletzten Silbe ([έκανα – κάναμε, ανέβηκα – ανεβήκαμε]{lang="el"}) | 03 |
| drittletzte / viertletzte Silbe | Betonungsposition immer so benennen (nicht „dritte von hinten“, „vier Silben vor dem Ende“) | 02 |
| Lippenlaut, Kehllaut | für [π β φ (ευ)]{lang="el"} bzw. [κ γ χ]{lang="el"} bei der Stammbildung ([-ψα, -ξα]{lang="el"}) | 02 |
| Präsens-Zutat | Laut, der nur im Präsens steht und im perfektiven Stamm fehlt ([τ]{lang="el"} in [-πτω]{lang="el"}, [ν]{lang="el"} in [-χνω]{lang="el"}) | 02 |
| Verben ohne perfektiven Stamm | [είμαι, έχω, ξέρω]{lang="el"}: „haben nur eine Vergangenheit“ ([ήμουν, είχα, ήξερα]{lang="el"}) | 02 |
| ich-Form, wir-Form … | Personenbezeichnung in Übungen („Bilde die ich-Form“), klein geschrieben | 02 |
| Aoristendungen | [-α, -ες, -ε, -αμε, -ατε, -αν]{lang="el"}; 3. Pl. [-αν]{lang="el"} neutral, [-ανε]{lang="el"} umg. | 02 |
| Diskursmarker (Erzählen) | eingeführt in 02: [άκου να δεις]{lang="el"} (jetzt pass auf), [που λες]{lang="el"} (Erzählfüller, „weißt du“), [και ξαφνικά]{lang="el"}, [με τα πολλά]{lang="el"}, [τελικά]{lang="el"}; dazu [λοιπόν]{lang="el"} aus 01 | 02 |
| Zuhörer-Reaktion | Reaktionen im Gespräch: [Μη μου πεις.]{lang="el"} (Sag bloß.), [Έλα!]{lang="el"} (Ach was!), [Σοβαρά;]{lang="el"} (Im Ernst?), [Όχι…]{lang="el"} | 02 |
| Verbindungswörter | Erzählsequenz [πρώτα – μετά/ύστερα – αργότερα – ξαφνικά – στο τέλος – τελικά]{lang="el"} | 02 |
| Hör-Auftrag | Übung mit externer Quelle am Ende der Hörspur; Schreibweise mit Bindestrich | 02 |
| Zitierte Fremdsprachen | Spanische, französische, lateinische Beispiele kursiv und mit `lang="es"`, `"fr"`, `"la"`; Grammatiklabels (*indefinido*, passé composé, imparfait) ohne Auszeichnung | 02 |
| Aufzug | Merkbild für [μπαίνω, βγαίνω, ανεβαίνω, κατεβαίνω]{lang="el"} „rein, raus, rauf, runter“, alle aus altem [βαίνω]{lang="el"}, Aorist auf [-ηκα]{lang="el"} (Eselsbrücke *Anabasis/Katabasis*) | 03 |
| Stamm ohne Anfang | [δεις, πεις, βγεις]{lang="el"}: perfektiver Stamm ohne [εί-]{lang="el"} bzw. Augment; in 02/03 nur so benannt, erklärt in Kapitel 5 (να-Form) | 03 |
| verschluckter Anfangsvokal | schnelle Rede nach [το, τα, μου, σου]{lang="el"}: [το ’πα, μου ’πε, τα ’φαγα, σ’ το ’πα]{lang="el"} mit Apostroph `’`; IPA [to ˈpa], [sto ˈpa]. Fachbegriffe (Elision, Aphärese) erst Kapitel 21 | 03 |
| Diskursmarker (Aoriste) | [Είδες;]{lang="el"} (Siehst du? Na bitte.), [Σ’ το ’πα.]{lang="el"} (Hab ich dir doch gesagt.), [Είπαμε!]{lang="el"} (Wie besprochen! / Ist ja gut.), [Το ’μαθες;]{lang="el"} (Hast du schon gehört?) | 03 |
| Namen aus der Odyssee | deutsche Formen: Odysseus, Penelope, Telemachos, Eumaios, Argos, Kirke, Kalypso, Polyphem, der Kyklop (Pl. Kyklopen), die Phaiaken, die Sirenen; Orte Ithaka, Troja, Thrakien | 03 |
