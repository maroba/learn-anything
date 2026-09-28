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
| σ | stimmlos wie *ss* in *Tasse*; vor stimmhaftem Konsonanten [z] ([ˈkozmos]) |
| ρ | getippt wie span. *pero* |
| [c] (κ vor e/i) | wie *k* in *Kiel* mit einem Hauch *j* |
| [ɟ] (γκ/γγ vor e/i) | wie *g* in *Gier* mit einem Hauch *j* |
| [ʎ] (λι vor Vokal) | wie *lj* in *Million*, verschmolzen |
| [ɲ] (νι vor Vokal) | wie span. *ñ* |
| [ŋ] (γ vor κ/γ/χ) | wie *ng* in *Engel*; γγ = [ŋg] |

## Transliteration

- Keine Transliteration als Aussprachehilfe.
- Lateinschrift nur für Eigen- und Ortsnamen, nach ELOT 743 (*Thessaloniki*, *Chania*). **Eingebürgerte deutsche Namen haben Vorrang** (*Athen*, *Neapel*, *Mykene*, *Ithaka*, *Troja*, *Patras*, *Polyphem*); in etymologischen Vergleichen die eingebürgerte deutsche Form (*Philosophie*). **Personen mit international etablierter Eigenschreibung:** diese Form (*Manos Hadjidakis*, *Michael Cacoyannis*, *Nana Mouskouri*), beim ersten Auftreten ggf. griechisch in Klammern.

## Grammatikbegriffe

Beim ersten Auftreten mit dem griechischen Fachwort in Klammern.

| Begriff im Buch | griechisch | Anmerkung | eingeführt in |
|---|---|---|---|
| imperfektiver Aspekt | εξακολουθητικός | Vorgang, Wiederholung („Film“) | 02 |
| perfektiver Aspekt | συνοπτικός | Handlung als Ganzes („Foto“) | 02 |
| perfektiver Stamm | – | nicht „Aoriststamm“; das Synonym einmal nennen | 02 |
| Präsens | ενεστώτας | | 01 |
| Nominativ | ονομαστική | | 01 |
| Akkusativ | αιτιατική | auch nach Präpositionen | 01 |
| Imperfekt | παρατατικός | | 04 |
| Aorist | αόριστος | erklärt als Vergangenheit im perfektiven Aspekt | 02 |
| Futur | μέλλοντας | „Futur mit θα“, in beiden Aspekten | 05 |
| να-Form (Konjunktiv) | υποτακτική | „να-Form“ als Arbeitsbegriff | 05 |
| Imperativ | προστακτική | | 09 |
| Genitiv | γενική | | 07 |
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
- Verben: 1. Person Präsens **und** Aorist (βλέπω, είδα); ab Kapitel 13 auch Aorist des Mediopassivs. Verben ohne perfektiven Stamm (είμαι, έχω, ξέρω) sowie θέλω (Aorist θέλησα selten): Präsens und Vergangenheit (είμαι, ήμουν; θέλω, ήθελα).
- Verben der Klasse -άω/-ώ stehen in `.vocab` in der umgangssprachlich häufigeren Form auf -άω (μιλάω); die Variante auf -ώ wird in Kapitel 1 einmal erklärt und nur bei Verben genannt, die überwiegend auf -ώ vorkommen.
- Adjektive: καλός, -ή, -ό.
- Registermarken in der Spalte Deutsch: (umg.), (salopp), (gehoben), (formell).

## Begriffe

| Begriff | Bedeutung / Schreibweise | eingeführt in |
|---|---|---|
| Digraph | zwei Buchstaben, ein Laut: Vokal-Digraphen [αι, ει, οι, ου]{lang="el"}, Konsonanten-Digraphen [μπ, ντ, γκ, τσ, τζ]{lang="el"} (dazu [γγ]{lang="el"} [ŋg]). [αυ, ευ]{lang="el"} sind „Vokal plus Konsonant“ ([av/af, ev/ef]), nicht Vokal-Digraphen | 01 |
| Trema, Akzent | [τα διαλυτικά]{lang="el"} (ϊ, ϋ) trennen zwei Vokale; im Fließtext „Akzent“ ([ο τόνος]{lang="el"}) | 01 |
| stimmhaft / stimmlos | Regel für [αυ, ευ]{lang="el"}: stimmlos sind [θ κ ξ π σ τ φ χ ψ]{lang="el"}, alles andere und Vokale stimmhaft | 01 |
| Verschlusslaut | Begründung der Schluss-ν-Regel: [κ π τ ξ ψ μπ ντ γκ τσ τζ]{lang="el"} | 01 |
| Schluss-ν | Name im Buch für das [ν]{lang="el"} von [την, δεν, μην]{lang="el"} (Abschnittstitel in 01: „Das wackelnde ν“); Regel siehe oben | 01 |
| stammbetont / endbetont | die drei Präsensmuster: [μένω]{lang="el"} stammbetont; [μιλάω]{lang="el"} und [μπορώ]{lang="el"} endbetont. Musterverben immer diese drei | 01 |
| Pro-Drop | Weglassen der Subjektpronomen; im Fließtext auch „ohne Subjektpronomen“ | 01 |
| Diskursmarker (Gespräch) | [λοιπόν]{lang="el"} (eröffnet, folgert), [έλα]{lang="el"} (Telefon, Antreiben, Staunen, [έλα τώρα]{lang="el"} Widerspruch), [ναι, αλλά]{lang="el"} (höflicher Widerspruch) | 01 |
| Kafenion | eingedeutschte Schreibweise für [το καφενείο]{lang="el"} (nicht „Kafeneío“) | 01 |
| Stamm: imperfektiver / perfektiver Stamm | Das Präsens kommt aus dem imperfektiven, Aorist, Futur (perfektiv) und να-Form aus dem perfektiven Stamm. Nicht „Präsensstamm“, nicht „Aoriststamm“ (nur einmal in 02 als Synonym genannt). „Der zweite Stamm“ nur als Titel-Formel (Kapiteltitel 02, 05), im Fließtext „perfektiver Stamm“. Stämme mit Bindestrich: [διαβασ-]{lang="el"} | 02 |
| Foto / Film | Bild für den Aspekt: perfektiv = Foto (als Ganzes, von außen), imperfektiv = Film (Vorgang, Wiederholung, Gewohnheit, Hintergrund). Immer diese beiden Wörter, keine anderen Metaphern | 02 |
| Vergangenheit im perfektiven Aspekt | Standarderklärung von „Aorist“; „als Ganzes“ heißt nicht „kurz“ | 02 |
| Perfekt-Falle | deutsches/spanisches Perfekt („Hast du … gelesen?“), wo Griechisch den Aorist nimmt | 02 |
| Augment | [ε-]{lang="el"}, bei einigen Verben [η-]{lang="el"} ([ήξερα – ξέραμε]{lang="el"}); steht nur betont; Merkformel „nur, wenn es betont ist“. Das [ή-/εί-]{lang="el"} in [ήρθα, ήπια, είδα, είπα]{lang="el"} gehört zum Stamm und bleibt im Plural ([ήρθαμε, είδαμε]{lang="el"}) | 02 |
| Bauform (unregelmäßige Aoriste) | (A) fester Anfang: zweisilbig, erste Silbe bleibt ([πήγα – πήγαμε]{lang="el"}); (B) Regel aus Kapitel 2: Augment nur betont, Betonung auf der drittletzten Silbe ([έκανα – κάναμε, ανέβηκα – ανεβήκαμε]{lang="el"}) | 03 |
| drittletzte / viertletzte Silbe | Betonungsposition immer so benennen (nicht „dritte von hinten“, „vier Silben vor dem Ende“) | 02 |
| Lippenlaut, Kehllaut | für [π β φ (ευ)]{lang="el"} bzw. [κ γ χ]{lang="el"} bei der Stammbildung ([-ψα, -ξα]{lang="el"}) | 02 |
| Präsens-Zutat | Laut, der nur im imperfektiven Stamm (Präsens, Imperfekt) steht und im perfektiven fehlt ([τ]{lang="el"} in [-πτω]{lang="el"}, [ν]{lang="el"} in [-χνω]{lang="el"}) | 02 |
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
| verschluckter Anfangsvokal | schnelle Rede nach [το, τα, μου, σου]{lang="el"}: [το ’πα, μου ’πε, τα ’φαγα, σ’ το ’πα]{lang="el"} mit Apostroph `’`; IPA: die Betonung wandert auf das kleine Wort, [ˈtopa], [ˈstopa], [ˈmupe] (nicht *[to ˈpa]); der Akzent wird trotzdem nicht geschrieben. Fachbegriffe (Elision, Aphärese) erst Kapitel 21 | 03 |
| Diskursmarker (Aoriste) | [Είδες;]{lang="el"} (Siehst du? Na bitte.), [Σ’ το ’πα.]{lang="el"} (Hab ich dir doch gesagt.), [Είπαμε!]{lang="el"} (Wie besprochen! / Ist ja gut.), [Το ’μαθες;]{lang="el"} (Hast du schon gehört?) | 03 |
| Namen aus der Odyssee | deutsche Formen: Odysseus, Penelope, Telemachos, Eumaios, Argos, Kirke, Kalypso, Polyphem, der Kyklop (Pl. Kyklopen), die Phaiaken, die Sirenen; Orte Ithaka, Troja, Thrakien | 03 |
| Imperfekt (Bildung) | Standarderklärung: „Vergangenheit im imperfektiven Aspekt“ (Film); imperfektiver Stamm + Aoristendungen, Augment-Regel wie beim Aorist ([έγραφα – γράφαμε]{lang="el"}); [η-]{lang="el"} bei [ήθελα, ήξερα]{lang="el"} | 04 |
| [-ούσα]{lang="el"}-Imperfekt | Verben auf [-άω]{lang="el"} und [-ώ]{lang="el"}: [μιλούσα, μπορούσα]{lang="el"}, immer auf [-ού-]{lang="el"} betont, nie Augment; umg. Variante [-αγα]{lang="el"} ([ξύπναγα]{lang="el"}) nur zum Wiedererkennen | 04 |
| kurze Verben (Imperfekt) | [λέω, τρώω, ακούω, καίω]{lang="el"} holen ein [γ]{lang="el"} heraus: [έλεγα, έτρωγα, άκουγα, έκαιγα]{lang="el"}; [πάω]{lang="el"} nimmt [πήγαινα]{lang="el"} (von [πηγαίνω]{lang="el"}) | 04 |
| Imperfekt = Aorist | [έκανα, περίμενα]{lang="el"}: eine Form für beides, „der Zusammenhang entscheidet“ | 04 |
| „und dann?“-Test | Probe für Foto oder Film: Bringt der Satz die Geschichte weiter, ist er ein Foto (Aorist). Zusatzprobe „gerade“/„immer“ für Film. Schreibweise: „und dann?“ in deutschen Anführungszeichen | 04 |
| Signalwörter | Wörter, die eher Film ([κάθε μέρα, πάντα, συνήθως, ενώ, εκεί που]{lang="el"}) oder eher Foto ([ξαφνικά, μια μέρα, δύο φορές]{lang="el"}) nach sich ziehen; „gezählt ist Foto, regelmäßig ist Film“ | 04 |
| erzählendes Präsens | [ιστορικός ενεστώτας]{lang="el"}: Präsens am Höhepunkt einer Erzählung über Vergangenes | 04 |
| Diskursmarker (Erinnern) | [Θυμάστε/Θυμάσαι τότε που…;]{lang="el"} (Wisst ihr/Weißt du noch, als …?), [Άλλες εποχές.]{lang="el"} (Andere Zeiten.), [Σ’ το ’λεγα.]{lang="el"} (Hab ich dir ja immer gesagt.), [Τι να κάνω;]{lang="el"} (Was soll(te) ich machen?, als Ganzes gelernt, να-Form erst 05) | 04 |
| Vorname [Γιάννης]{lang="el"} | nach ELOT 743 *Giannis* (nicht „Jannis“); Vornamen in Übersetzungen generell nach ELOT | 04 |
| eingedeutschte Sachwörter | *Tavli* ([το τάβλι]{lang="el"}), *Kaiki* ([το καΐκι]{lang="el"}), *Chora* ([η Χώρα]{lang="el"}, Hauptort einer Kykladeninsel), *Meltemi*, *Raki* (der), *Taverne* | 04 |
| männlich / weiblich / sächlich | Genusbezeichnung im Fließtext und in Tabellen; nicht „Maskulinum/Femininum/Neutrum“ bzw. „maskulin/feminin“ | 06 |
| Imperativ | für [Κοίτα, Πάρτε, δοκιμάστε]{lang="el"} usw. auch vor Kapitel 9 „Imperativ“, nicht „Befehlsform“ | 06 |
| kurzer *j*-Laut | unbetontes [ι]{lang="el"} zwischen Konsonant und Vokal ([τα παιδιά]{lang="el"} [ta peˈðʝa]); nicht „Gleitlaut“ | 01 |
| verschmelzen ([σε]{lang="el"} + Artikel) | [στον, στη(ν), στο, στους, στις, στα]{lang="el"}: „[σε]{lang="el"} verschmilzt mit dem Artikel“ (nicht „zusammengezogen“) | 01 |
| Nomenklassen nach Endung | männlich [-ος, -ας, -ης]{lang="el"}, weiblich [-α, -η]{lang="el"}, sächlich [-ο, -ι, -μα]{lang="el"}; „die Endung verrät Genus und Plural“; drei Fragen: Genus? Plural? Wandert die Betonung? | 06 |
| [-δ-]{lang="el"}-Silbe | Plural [ο ψαράς – οι ψαράδες, η γιαγιά – οι γιαγιάδες]{lang="el"}; Schreibweise mit Bindestrichen | 06 |
| die Betonung wandert | Standardformulierung für Akzentverschiebung ([πρόβλημα – προβλήματα, άνθρωποι – ανθρώπους, ανάλυση – αναλύσεις]{lang="el"}) | 06 |
| weibliche Nomen auf [-ος]{lang="el"} | [η μέθοδος, η έξοδος, η περίοδος, η διάλεκτος, η άσφαλτος]{lang="el"}: deklinieren wie [ο άνθρωπος]{lang="el"}, weibliches Adjektiv | 06 |
| Internationalismen | Fachbegriff ab 06 (in 01 „internationale Wörter“); Genusregel [-μα]{lang="el"} sächlich, [-ση, -ξη, -ψη, -ία]{lang="el"} weiblich, [-ισμός]{lang="el"} männlich | 06 |
| Zahlen mit Genus | „eins, drei, vier“: [ένας/μία/ένα, τρεις/τρία, τέσσερις/τέσσερα]{lang="el"}; Preise sächlich, Uhrzeiten weiblich; „anderthalb“ [ενάμισης, μιάμιση, ενάμισι]{lang="el"} | 06 |
| Laiki | eingedeutschte Schreibweise für [η λαϊκή (αγορά)]{lang="el"}, der Wochenmarkt; im Text „die Laiki“, nicht kursiv | 06 |
| Ortsnamen Athen | nach ELOT 743: *Exarcheia* (nicht „Exarchia“), *Thiseio*, *Kallidromiou*-Straße; *Megara*, *Naxos* | 06 |
| Zitierte Fremdsprachen (Ergänzung) | Herkunftswörter ebenfalls kursiv und ausgezeichnet: `lang="it"` (*patata*), `"tr"` (*manav*), `"pl"` (*ogórek*), `"nah"` (*tomatl*) | 06 |
| Futur mit [θα]{lang="el"} | Name im Buch für [ο μέλλοντας]{lang="el"}, in beiden Aspekten: Foto [θα γράψω]{lang="el"}, Film [θα γράφω]{lang="el"}; Merkformel „im Zweifel Foto“ gilt nur für die Zukunft. Verneint [δε θα]{lang="el"}; Reihenfolge [δε – θα – Objektwort – Verb]{lang="el"} | 05 |
| [να]{lang="el"}-Form (Konjunktiv) | Arbeitsbegriff für die Form nach [να]{lang="el"}; „Konjunktiv“ nur als Grammatikname nennen (nicht der deutsche Konjunktiv). Im Text mit ausgezeichnetem Griechisch: [να]{lang="el"}-Form, [θα]{lang="el"}-Form, [να]{lang="el"}-Sätze | 05 |
| ein Stamm, drei Einsätze | perfektiver Stamm in Aorist, Futur und [να]{lang="el"}-Form ([έγραψα, θα γράψω, να γράψω]{lang="el"}); Bildung: perfektiver Stamm ohne Augment + Präsensendungen | 05 |
| drei Handgriffe | vom Aorist zur [θα]{lang="el"}-Form: Augment weg, Betonung auf die letzte Stammsilbe, Endung [-ω]{lang="el"} (gilt für regelmäßige Verben und Bauform B) | 05 |
| Stamm ohne Anfang (Erklärung) | Merkformel „Der Anfang gehört zur Vergangenheit“: Bauform A verliert [εί-/ή-]{lang="el"} bzw. die erste Silbe, Kerne [δω, πω, βρω, βγω, μπω, πιω]{lang="el"} mit Endungen wie [μπορώ]{lang="el"}; „Einzelgänger“ [πάω, έρθω, πάρω]{lang="el"}; Ausnahme in Bauform B [φάω]{lang="el"}; [-ηκα → -ω]{lang="el"} | 05 |
| keine Wahl | Übungslabel nur für Verben ohne perfektiven Stamm ([είμαι, έχω, ξέρω]{lang="el"}); [κάνω, πάω, περιμένω]{lang="el"} haben gleiche Formen, werden aber nach Bedeutung als Foto oder Film eingeordnet | 05 |
| [θα ήθελα]{lang="el"} | „ich hätte gern, ich würde gern“, höfliche Bitte; als feste Wendung gelernt ([θα]{lang="el"} + Imperfekt), Irrealis erst Kapitel 24 | 05 |
| kein Infinitiv | „Das Neugriechische hat keinen Infinitiv“: Verb + [να]{lang="el"} + konjugiertes Verb ([θέλω να πάω / να πας]{lang="el"}); Verneinung [να μη(ν)]{lang="el"}, nie [να δεν]{lang="el"} | 05 |
| kleine Objektwörter | Umschreibung für schwache Pronomen vor Kapitel 8 ([το, μου, σου, σε, μας]{lang="el"}) | 01 |
| Diskursmarker (Pläne) | [Άκου, …]{lang="el"} (Hör mal), [Να σου πω]{lang="el"} (weißt du was), [λέω να]{lang="el"} (ich überlege, ob ich …, umg.), [Θα δούμε.]{lang="el"} (Mal sehen.), [Θα σε πάρω (τηλέφωνο).]{lang="el"}, [Τα λέμε.]{lang="el"} (Bis dann.), [Να ’σαι/’στε καλά.]{lang="el"} (Danke, das ist lieb) | 05 |
| verschluckter Anfangsvokal nach [θα, να]{lang="el"} | [θα ’ρθω, θα ’μαι, θα ’χω, να ’σαι, να ’στε]{lang="el"}; seltener fällt das [α]{lang="el"} der Partikel: [θ’ ανέβω, ν’ ακούσεις]{lang="el"}; IPA [ˈθarθo], [ˈθame], [ˈnase], aber [θaˈnevo] | 05 |
| Orte und Sachwörter (Kapitel 5) | *Piräus* (eingebürgert), *Serifos, Sifnos, Milos, Amorgos, Naxos* (ELOT); Inselnamen auf [-ος]{lang="el"} weiblich; *Beaufort* (Windstärke, [το μποφόρ]{lang="el"}); *Etesien*; [η ΠΝΟ]{lang="el"} griechisch geschrieben | 05 |
| Besitzwörter | [μου, σου, του, της, μας, σας, τους]{lang="el"} hinter dem Nomen, das seinen Artikel behält ([ο γιος μου]{lang="el"}); im Buch „Besitzwort“, nicht „Possessivpronomen“. Betont: [δικός μου, δική μου, δικό μου]{lang="el"} (richtet sich nach dem Besessenen). Merkregel: „Folgt ein Nomen, ist [του/της/τους]{lang="el"} der Artikel“ | 07 |
| Genitiv Singular (Faustregel) | männlich [-ς]{lang="el"} weg ([του πατέρα, του Γιάννη]{lang="el"}), [-ος → -ου]{lang="el"}; weiblich [+ ς]{lang="el"}; sächlich [-ου, -ιού, -ματος]{lang="el"}; Artikel [του, της, του]{lang="el"}. Plural „immer [-ων]{lang="el"}“, Artikel [των]{lang="el"}. Der Genitiv steht **hinter** dem Nomen, zu dem er gehört | 07 |
| Betonung im Genitiv | „[-ιού]{lang="el"} ist immer betont“; „[-ου]{lang="el"} zieht wie [-ους]{lang="el"}“ (drittletzte → vorletzte Silbe: [του ανθρώπου, Παπαδοπούλου]{lang="el"}); [-ματος]{lang="el"}: die Betonung wandert mit | 07 |
| Vokativregel | nur männliche Nomen im Singular haben eine eigene Form, alles andere wie der Nominativ. [-ας, -ης, -ούς]{lang="el"}: das [-ς]{lang="el"} fällt. [-ος]{lang="el"} bei Vornamen nach der Betonung: vorletzte Silbe betont → meist [-ο]{lang="el"} ([Γιώργο]{lang="el"}), drittletzte → [-ε]{lang="el"} ([Αλέξανδρε]{lang="el"}); gelehrte Namen auf [-ιος → -ιε]{lang="el"}; gewöhnliche Wörter und Nachnamen auf [-όπουλος]{lang="el"} meist [-ε]{lang="el"} ([φίλε, κύριε Παπαδόπουλε]{lang="el"}) | 07 |
| Höflichkeitsform | 2. Person Plural ([εσείς]{lang="el"}), Vergleich frz. *vous*; im Fließtext „du“/„Sie“, „duzen/siezen“; [κύριε/κυρία]{lang="el"} + Vorname mit [εσείς]{lang="el"} als Zwischenstufe; Adjektiv bei [εσείς]{lang="el"} im Singular für eine Person ([Είστε σίγουρος;]{lang="el"}) | 07 |
| Anredewörter | [ρε, βρε]{lang="el"} + Vokativ (vertraut, umg.), [Παιδιά!]{lang="el"} (an eine Runde, „Leute!“), [μου]{lang="el"} hinter der Anrede zärtlich ([Γιώργο μου, κορίτσι μου]{lang="el"}); volkstümlich [κυρ]{lang="el"} | 07 |
| Namenstag | [η γιορτή]{lang="el"}; Glückwunsch [Χρόνια πολλά!]{lang="el"}, an Angehörige [Να σας ζήσει!]{lang="el"}. Der Heilige heißt deutsch „der heilige Georg“, die Namensträger nach ELOT (*Giorgos*) | 07 |
| amtlicher Name / Alltagsname | [Γεώργιος – Γιώργος, Ιωάννης – Γιάννης, Κωνσταντίνος – Κώστας, Νικόλαος – Νίκος, Αικατερίνη – Κατερίνα]{lang="el"}; Lateinschrift nach ELOT (*Georgios, Ioannis, Nikolaos*) | 07 |
| Nachnamen im Genitiv | Frauen tragen den Nachnamen im Genitiv ([Παπαδοπούλου, Βλάχου, Σφακιανάκη]{lang="el"}); Männernamen wie [Γεωργίου, Νικολάου]{lang="el"} sind selbst Genitive. ELOT-Schreibweise *Papadopoulos*. Herkunft aus der Endung nur als Tendenz (Vorsicht-Box) | 07 |
| deutscher Genitiv von Namen auf *-s* | mit typografischem Apostroph `’`: *Giannis’ Haus, Kostas’ Auto* | 04 |
| Namen und Orte (Kapitel 7) | *Giorgos, Eleni, Angeliki, Kostas, Nikos, Manolis, Stelios* (ELOT); Straßen *Athinas, Aiolou, Ermou, Panepistimiou*, *Syntagma-Platz*; Berg *Kallidromo*; Mythologie deutsch: *Aiolos, Hermes, Athena, Homer*; *König Otto* | 07 |
| KEP | [το ΚΕΠ]{lang="el"} [cep] ([Κέντρο Εξυπηρέτησης Πολιτών]{lang="el"}), im Text griechisch geschrieben, erklärt als „Bürgeramt“ | 07 |
| Deponens, Deponentien | Verben, die im Präsens nur auf [-μαι]{lang="el"} vorkommen und aktiv gemeint sind ([το αποθετικό ρήμα]{lang="el"}); Plural „Deponentien“. Suchhilfe (keine Regel): Wo das Deutsche „sich“ hat, liegt [-μαι]{lang="el"} nahe. Die Endung heißt nach dem Mediopassiv (13), nicht „Passivendung“ | 10 |
| [-ομαι]{lang="el"}- / [-άμαι]{lang="el"}-Gruppe | die zwei Präsensmuster der Verben auf [-μαι]{lang="el"}; Musterverben [κάθομαι]{lang="el"} und [φοβάμαι]{lang="el"} (in 01: [έρχομαι, κοιμάμαι]{lang="el"}); wir-Form immer [-όμαστε]{lang="el"}, sie-Form der [-άμαι]{lang="el"}-Gruppe [-ούνται]{lang="el"}. [-μαι, -σαι, -ται]{lang="el"} klingen [me, se, te] | 10 |
| Aorist auf [-θηκα/-τηκα]{lang="el"} | Schreibweise mit Schrägstrich; Faustregeln: [-άμαι → -ήθηκα]{lang="el"}, [-ζομαι → -στηκα]{lang="el"}, [σκέφτομαι → σκέφτηκα]{lang="el"}; Aoristendungen, drittletzte Silbe, kein Augment. Futur/[να]{lang="el"}-Form [-θώ, -θείς …]{lang="el"} mit Endungen wie [μπορώ]{lang="el"} (Regel [-ηκα → -ω]{lang="el"} aus 05) | 10 |
| Ausreißer (Deponentien) | die drei Verben auf [-μαι]{lang="el"} mit aktivem Aorist: [ήρθα, έγινα, κάθισα]{lang="el"} (umg. [έκατσα]{lang="el"}); nicht zu verwechseln mit den „Einzelgängern“ aus 05/09 | 10 |
| [κάθισα / έκατσα]{lang="el"} | [κάθισα, καθίσω]{lang="el"} neutrale Standardform, [έκατσα, κάτσω]{lang="el"} umg., im Gespräch sehr häufig; Imperativ [Κάτσε!]{lang="el"} | 10 |
| Zustand / Moment | bei Deponentien: imperfektiver Stamm = **Zustand** (Film), perfektiver = **Moment**, in dem er beginnt, oder der Zustand als abgeschlossenes Ganzes (Foto): [φοβάμαι – φοβήθηκα, κοιμάμαι – κοιμήθηκα, κάθομαι – κάθισα, θυμάμαι – θυμήθηκα]{lang="el"}. Tabellenkopf „Film: Zustand \| Foto: Moment“ | 10 |
| Imperfekt auf [-όμουν]{lang="el"} | Imperfekt der Verben auf [-μαι]{lang="el"}: betontes [-ό-]{lang="el"} + Endungen von [ήμουν]{lang="el"} ([καθόμουν, κοιμόταν]{lang="el"}); sie-Form [κάθονταν, κοιμούνταν]{lang="el"}; umg. [-όμουνα, -όντουσαν]{lang="el"} nur zum Wiedererkennen; aktive Beherrschung erst mit dem Mediopassiv (13) | 10 |
| Diskursmarker (Deponentien) | [Γίνεται;]{lang="el"} (Geht das?), [Δε γίνεται.]{lang="el"} (Geht nicht.), [Έγινε!]{lang="el"} (Geht klar!), [Θα το σκεφτώ.]{lang="el"} (Ich überleg's mir.), [Λυπάμαι.]{lang="el"} (Es tut mir leid.), [Μου θυμίζει …]{lang="el"}, [Κάτσε!]{lang="el"}, [Μη φοβάσαι!]{lang="el"}; Erinnern: [Αν τον θυμάμαι;]{lang="el"}, [Σαν να ’ταν χθες.]{lang="el"}, [Αν είναι να γίνει, θα γίνει.]{lang="el"} | 10 |
| Namen und Orte (Kapitel 10) | *Kefalonia, Zakynthos, Thessaloniki* (ELOT), *Ithaka, Santorin, Kreta, Ägäis* (eingebürgert); *Poseidon, Homer*, Epitheton *Ennosigaios*; „Richterskala“ ([τα Ρίχτερ]{lang="el"}) | 10 |
