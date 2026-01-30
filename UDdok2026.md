# **Eesti keele universaalsõltuvuste (*Universal Dependencies*, UD) eesti keele puudepank ja selle märgendusskeem**

**Lühikokkuvõte**  
Universaalsõltuvused ([Universal Dependencies](https://universaldependencies.github.io/docs/introduction.html)), lühidalt UD on projekt, mille eesmärgiks on luua ühtne, tüpoloogiliselt relevantne morfoloogiline ja sõltuvussüntaktiline märgendussüsteem võimalikult paljude keelte jaoks.

Eesti keele UD sõltuvuspuude pank EBT on loodud [Eesti keele sõltuvuspuude panga](https://www.keeletehnoloogia.ee/et/ekt-projektid/vahendid-teksti-mitmekihiliseks-margendamiseks-rakendatuna-koondkorpusele/soltuvussuntaktiliselt-analuusitud-korpus) teisendamise teel UD kujule, kuid selle teisendamise tulemust on käsitsi palju täiendatud ja täpsustatud. Teine eesti keele universaalsõltuvuste korpus \- veebitekstide sõltuvuspuude pank EWT on loodud tekste käsitsi märgendades.

UD sõltuvuspuude pankades on märgendatud:  
1\. lemma e algvorm  
2\. sõnaliik  
3\. morfoloogilised kategooriad (*features*)  
4\. ülemus sõltuvuspuus  
5\. sõltuvussuhe (*relations*)  
6\. nn täiustatud sõltuvused (*enhanced dependencies*)  
7\. muu: ortograafiavead, nimeüksused, verbikesksed argumendistruktuurid.

# **Sisukord**

[CONLLU formaat](#conllu-formaat)

[Sõnestamine (tokenization)](#sõnestamine-tokenization)

[UD morfoloogiline märgendus](#ud-morfoloogiline-märgendus)

[Lemma](#lemma)

[Sõnaliigid](#sõnaliigid)

[Morfoloogilised kategooriad (features)](#tunnused-features)

[Sõltuvussüntaktiline märgendus](#sõltuvussüntaktiline-märgendus)

[UD üldpõhimõtted, lühidalt](#ud-üldpõhimõtted-lühidalt)

[Koopulalaused](#koopulalaused)

[Väljajättelised struktuurid ehk ellipsid](#väljajättelised-struktuurid-ehk-ellipsid)

[Muud sõltuvusstruktuuri küsimused](#muud-sõltuvusstruktuuri-küsimused)

[Eesti keele UD süntaktilised märgendid (relations)](#eesti-keele-ud-süntaktilised-märgendid-relations)

[Tuumargumendid](#tuumargumendid)

[Muud laiendid](#muud-laiendid)

[Muud verbi alluvad](#muud-verbi-alluvad)

[Koordinatsioon](#koordinatsioon)

[Muu](#muu)

[Mitmesõnalised üksused (sisemise struktuurita sõnaühendid)](#mitmesõnalised-üksused-sisemise-struktuurita-sõnaühendid)

[Nõrgalt seotud suhete märgendid (*loose joining relations*)](#nõrgalt-seotud-suhete-märgendid-loose-joining-relations)

[Täiustatud sõltuvused (*Enhanced Dependencies*)](#täiustatud-sõltuvused-enhanced-dependencies)



# **CONLLU formaat**

Puudepankade failid on UTF-8-kodeeringus. Failides on kolme tüüpi ridu:

1. Sõnad, kirjavahemärgid jm tekstiüksused koos nende märgendusega: reas on 10 tabelimärgiga eraldatud välja, täpsemalt allpool.  
2. Tühjad read lausepiiride märkimiseks.  
3. \# märgiga algavad kommentaariread.

Laused koosnevad ühest või rohkematest ridadest, vt järgnev näide:

```
# sent_id = aja_ee200110_1714  
# text = Lumetorm muutub üha tihedamaks, tee libedamaks.  
1    Lumetorm    lume_torm    NOUN    S    Case=Nom|Number=Sing    2    nsubj    2:nsubj|4:nsubj    Arg=muutuma_Arg_1  
2    muutub    muutuma    VERB    V    Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act    0    root    0:root    Verb=muutuma  
3    üha    üha    ADV    D    _    4    advmod    4:advmod    _  
4    tihedamaks    tihedam    ADJ    A    Case=Tra|Degree=Cmp|Number=Sing    2    xcomp    2:xcomp    Arg=muutuma_Arg_2|SpaceAfter=No  
5    ,    ,    PUNCT    Z    _    6    punct    6:punct    _  
6    tee    tee    NOUN    S    Case=Nom|Number=Sing    2    conj    6.1:nsubj|7:nsubj    _  
6.1    muutub    muutuma    VERB    V    Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act    _    _    0:root|2:conj    _  
7    libedamaks    libedam    ADJ    A    Case=Tra|Degree=Cmp|Number=Sing    6    orphan    6.1:xcomp    SpaceAfter=No  
8    .    .    PUNCT    Z    _    2    punct    2:punct    _

```
 Lauset moodustavate üksuste read koosnevad järgmistest väljadest:

* ID: sõna indeks e järjekorranumber lauses. Iga lause esimene sõna on numbriga 1\.  
  * Kui identifikaator on naturaalarvude vahemik, siis on tegemist mitmesõnalise üksusega ning järgmised read kirjeldavad seda üksust sõne kaupa, esineb väga harva. Kui identifikaator on kujul naturaalarv.naturaalarv, siis on tegemist elliptilise lausega, milles on väljajätteline sõna või sõnad märgendusse lisatud, nt verbivorm *muutub* real 6.1 ülalolevas näites. Erandkorras võib lisatav sõna paikneda ka lause algul, siis algab indeks arvuga 0\.  
* FORM: Sõnavorm st tekstisõna, punktuatsioonimärk või muu sümbol  
* LEMMA: algvorm  
* UPOS: Sõnaliik, vt altpoolt  
* XPOS: Sõnaliik nagu need on määratletud siin [https://filosoft.ee/html\_morf\_et/morfoutinfo.html\#2](https://filosoft.ee/html_morf_et/morfoutinfo.html#2)  
* FEATS: Morfoloogilised kategooriad (*features*), vt altpoolt. Kui sellel üksusel neid pole, siis alakriips \_  
* HEAD: Ülemus sõltuvuspuus. Lause juurtipu ülemus on 0  
* DEPREL:sõltuvussuhte nimi (*deprel*), vt altpoolt  
* DEPS: Täiustatud sõltuvused (*enhanced dependency graph*) ülemus-alluv paaride loendina. Kui pole märgendatud, siis alakriips \_  
* MISC: Muu märgendus, vt täpsemalt altpoolt.

Väljad peavad vastama järgmistele tingimustele:

1. Väljad ei tohi olla tühjad. Kui vastavat infot pole, siis on väljal alakriips \_  
2. Muud väljad peale FORM, LEMMA ja MISC ei tohi sisaldada tühikuid.  
3. UPOS, HEAD, ja DEPREL väljad ei tohi olla täitmata, välja arvatud juhud,  juhul kui need paiknevad mitmesõnaliste üksuste vahemikku kirjeldaval real, siis on nad vaikeväärtusega “\_”, esineb harva. Samuti on väljad HEAD ja DEPREL  vaikeväärtustega elliptilistes lausetes lisatud verbi kirjelduses.

# **Sõnestamine (*tokenization*)**

Üldiselt sõnestatakse nn tavalisel viisil: sõnapiiriks on tühik või reavahetus, kirjavahemärgid tõstetakse sõnadest lahku.   
Tühikuteta kuupäev stiilis 07.06.03 on üks sõne.  
Kui tühik on algtekstis olnud sõna sees (*kas sile* pro *kassile*), siis on tühikuga eraldatud järelosa omaette real ja tema süntaktiliseks märgendiks on goeswith. Kuid kokku-lahku kirjutamise vigu *(lasteaed* vs *laste aed*) ei parandata.

Kui sõna sisaldab sidekriipsu ja see on korrektne, siis märgendatakse sõna vastavalt tema morfoloogilise informatsioonile, nt

```
1    Aeg-ajalt    aeg-ajalt    ADV    D    _    2    advmod    2:advmod    _
```

Kui sõna on koordinatsioonis olev liitsõna esimene pool (nt *riist- ja tarkvara*),  siis märgendatakse sõna selle morfoloogilise märgendusega, mis on selle sõnapoole kohta teada

```
14    riist-    riist    NOUN    S    Hyph=Yes    17    nmod    _    _
```

# **UD morfoloogiline märgendus**

## 1.  **Lemma**

   Lemma määramise erijuhud:

- [ ]  Kui tekstisõnas on trüki- või õigekirjaviga, vastab tema lemma tema korrektsele kujule ning sõnal on märgend kirjavea kohta (Typo=Yes) ning õigekirjareeglitele vastava korrektse vormi kohta. Veebitekstide puudepanga EWT tekstides eiratakse sageli ortograafiareegleid, sh nõuet kirjutada pärisnimi suure algustähega. Väikese algustähega kirjutatud pärisnime lemma on suure algustähega ja sõnal on märgend kirjavea kohta (Typo=Yes) ning õigekirjareeglitele vastava vormi kohta:
```
      28    eestis    Eesti    PROPN    S    Case=Ine|Number=Sing|Typo=Yes    26    conj    21:acl|26:conj    CorrectForm=Eestis
```

- [ ] „tsenseeritud” sõnavormi lemma on tsenseerimata sõna, nt *\*\*\*\*\*iidi* lemma on *perseiid*. Kui õige lemma kontekstist üheselt ei selgu, siis jääb muidugi „tsenseeritud” variant.  
      

## 2.  **Sõnaliigid**

- ADJ adjektiiv. Täiendi positsioonis olevad mineviku partitsiibid on sõnaliigilt omadussõnad, aga omavad ka verbi morfoloogilisi kategooriaid, nt  
> tehtud	tehtud	ADJ	A	Degree=Pos|Tense=Past|VerbForm=Part|Voice=Pass  
- ADP adpositsioon, ees- ja tagasõna eristatakse tunnuse AdpType abil.  
- ADV adverb  
- AUX abiverb. Need on ainult:  
	- *olema* liitaegades, modaalid: *saama*, *võima*, *pidama*  
	- *olema* koopulalausetes  
	- *ei, ära* vormid verbi eitava liitvormi koosseisus  
- CCONJ koordineeriv sidend, nendena on märgendatud *aga, ega, ehk, elik, ent, ja, kui, kuid, kuni (kolm kuni neli kuud), nagu, nii* (liitsidendis *nii … kui), ning, vaid, või*  
- DET määratleja (*determiner*). Määratleja kohta eesti keeles vt Erelt ja Metslang „Eesti keele süntaks” lk 382 jj.  
Määratlejatena on eesti keele UD puudepankades märgendatud: *see, too, seesama, toosama, sama, esimene, teine, mis* (tähenduses *milline,* nt kasutustes *mis vahe on* ..., *mis asi on* ..., *mis tähtsust sellel on* jne), *iga, kõik, kogu, keegi, miski, üks, ükski, mingi, terve* (tähenduses ’kogu’, nt *keetsin terve potitäie suppi*), *muu, mõni, paljud, igasugu, igasugune, mitmesugune, niisugune, niisamasugune, samasugune, selline, seesamune, seesugune, nihuke, sihuke, siuke, säherdune, säärane, selletaoline, taoline*  
Määratleja on alati täiendi positsioonis:  
*See maja on suur* – *see* on DET ; *See on suur maja* – *see* on PRON  
- INTJ interjektsioon. Ka üneemid (*ah, mh, no* jm) on märgendatud interjektsioonidena.  
- NOUN substantiiv  
- NUM numeraal; täis- ja järgarvsõnu eristatakse tunnuste NumType abil.  
- PRON pronoomen, alaliike eristatakse tunnuse PronType abil.  
- PROPN pärisnimi  
- PUNCT punktuatsioon  
- SCONJ alistav sidend, sellena on märgendatud *ehkki, et, justkui, kui* (v.a. liitsidendis *nii … kui*)*, kuigi, kuna, kuni, nagu, otsekui, selmet, sest.*  
- SYM sümbol, nt 50 %, Saab 340B, Ansip & Co. Märgendi SYM saavad ka emotikonid veebitekstides, nt :) ;D ja adressaati tähistav @ EWT mõnedes foorumitekstides.  
- VERB verb  
- X muu, selle märgendi saavad:
	- muukeelsed sõnad. Kui neil on lauses süntaktiline funktsioon, saavad nad sellekohase märgendi, nt lauses

```
# text = Üheks teadaolevaks dementsuse põhjuseks sel perioodil oli dementia paralytica, süüfilise tertsiaalses staadiumis tekkiv dementsus.  
/…/  
8 dementia dementia X T Foreign=Yes 4 nsubj:cop 4:nsubj OrigLang=la  
9 paralytica paralytica X T Foreign=Yes 8 flat:foreign 8:flat OrigLang=la|SpaceAfter=No
```

## **Tunnused (*features*)**

Algselt olid sellel väljal ainult morfoloogiliste kategooriate märgendid, aga aja jooksul on lisandunud hulk muid tunnuseid, esitame need tähestiku järjekorras.

Abbr=Yes lühend (sõnaliik vastab lühendi tähendusele/kasutusele, nt *jne* on ADV)

AdpType=Post adpositsiooni liik: postpositsioon

AdpType=Prep adpositsiooni liik: prepositsioon

Case=Abe kääne: abessiiv

Case=Abl kääne: ablatiiv

Case=Add kääne: aditiiv (illatiivi lühike vorm)

Case=Ade kääne: adessiiv

Case=All kääne: allatiiv

Case=Com kääne: komitatiiv

Case=Ela kääne: elatiiv

Case=Ess kääne: essiiv

Case=Gen kääne: genitiiv

Case=Ill kääne: illatiiv

Case=Ine kääne: inessiiv

Case=Nom kääne: nominatiiv

Case=Par kääne: partitiiv

Case=Ter kääne: terminatiiv

Case=Tra kääne: translatiiv

Connegative=Yes: verbi eitava liitvormi osa, nt *tea* liitvormis *ei tea*.

Degree=Cmp võrdlusaste: komparatiiv

Degree=Pos võrdlusaste: positiiv

Degree=Sup võrdlusaste: superlatiiv

ExtPos püsiühendi kui terviku sõnaliik. Rakendatakse juhul kui sõnaühend on ühendatud süntaktilise märgendiga fixed, vt loendit selle juurest.

Foreign=Yes märgendiga sõna on võõrkeelne sõna (mis pole sama mis võõrsõna) Kui sõnaliik on X, on alati see märgend, aga ta on ka võõrkeelsetel PROPN sõnaliigi märgendiga sõnadel (nt *ajakiri Foreign Affairs*, *Rail Baltic*). Kui sõna tunnuste hulgas on selline tunnus, siis peab MISC väljal olema märgend selle sõna keelsuse kohta. Teine variant selliste sõnade puhul on märgendada sõna toorlaenuna, seda kasutatakse nt siis, kui sõnal on eesti keele muutetunnused (nt *…kui sa kettalt bootida tahad…*). Sellistel sõnadel on sõnaliigi ja süntaktilise funktsiooni märgend vastavalt nende tähendusele ja lausekasutusele, kuid MISC väljal on märgend keelsuse kohta.

Mood=Cnd kõneviis: konditsionaal

Mood=Imp kõneviis: imperatiiv

Mood=Ind kõneviis: indikatiiv

Mood=Qot kõneviis: kvotatiiv

Number=Plur arv: mitmus

Number=Sing arv: ainsus

NumForm=Digit arvsõna: numbritena

NumForm=Letter arvsõna: sõnana

NumForm=Roman arvsõna: Rooma numbritena

NumType=Card arvsõna: põhiarv

NumType=Ord arvsõna: järgarv

Person=1 isik: 1

Person=2 isik: 2

Person=3 isik: 3

Polarity=Neg kõneliik: eitav (jaatavat pole märgendatud)

Poss=Yes possessiivne. Praegu on nii märgendatud asesõnad *oma, omaenda, omaenese* 

PronType \- asesõna liik. Märgend võib olla ka muul sõnal kui asesõnal, nt kõigil määratlejatel DET, omadussõna sõnaliigimärgendiga aseomadussõnadel *milline, selline, sama, samasugune, säärane, niisugune, missugune, mingisugune, igasugune* jne.

PronType=Dem: demonstratiiv: *see, too, seesama, toosama, sama, esimene, teine*

PronType=Ind: indefiniitne: *keegi, miski, üks, igaüks, muu, mõned, paljud*

PronType=Int , Rel: interrogatiiv-relatiivne: *kes, mis, kumb, missugune, milline, mitu, mitmes*

PronType=Prs: personaalne: *mina, sina, tema, meie, teie, nemad, oma, ise, iseenda, omaenese*

PronType=Rcp: retsiprookne: *üksteise, teineteise*

PronType=Tot: totaalne e kollektiivne: *kõik, iga, kogu, terve*

Reflex=Yes refleksiivne: *ise*, *enda, iseenese, iseenda*

Tense=Past aeg: minevik

Tense=Pres aeg: olevik

Typo=Yes sõnaortograafia viga. Kui sõnal on see märgend, on MISC väljal märgendiga CorrectForm näidatud sõnavormi õige kuju. 

VerbForm=Fin verbi vorm: finiitne

VerbForm=Inf verbi vorm: infiniitne (da-infinitiiv)

VerbForm=Part verbi vorm: partitsiip

VerbForm=Sup verbi vorm: supiin (ma-infinitiiv)

VerbForm=Conv verbi vorm: konverb (des-vorm)

Voice=Act tegumood: personaal

Voice=Pass tegumood: impersonaal ja passiiv

Kogu kasutusel olev tunnuste süsteem on leitav kodulehelt: [https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify\_feature.pl?lcode=et](https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify_feature.pl?lcode=et)

# **Sõltuvussüntaktiline märgendus**

Sõltuvussüntaktilise analüüsi puhul esitatakse kogu lausestruktuur kahe sõnavormi vaheliste ebasümmeetrilise suhtena (põhi e ülemus \- laiend e alluv), sellel suhtel on nimi (süntaktiline funktsioon). Lausestruktuuri esitamisel mitteterminaalseid sümboleid ei kasutata, st sõltuvussuhted on sõnade vahel, vahesõlmi (fraase, moodustajaid) ei moodustata. Ühel sõnal võib olla mitu alluvat, aga ainult üks ülemus.

## **UD üldpõhimõtted, lühidalt.**

Pikemalt vt [https://universaldependencies.org/u/overview/syntax.html](https://universaldependencies.org/u/overview/syntax.html).

Universal Dependencies' süntaktiline märgendus esitab sõnadevahelised sõltuvussuhted koos nende süntaktiliste funktsioonide nimetustega.

Sõltuvuste nimetuste (süntaktiliste funktsioonide) taksonoomia aluseks on eristus tuumargumentide (subjektid, objektid, seotud infiniittarindilised või osalauselised laiendid (*clausal complements*)) ja ülejäänud argumentide e seotud laiendite vahel. Samas ei üritata eristada seotud obliikva laiendeid vabadest laienditest.

On keelelisi konstruktsioone, mille jaoks sõltuvusesitus sobib väga hästi ja ka neid, mille puhul ühte konstruktsioonis osalevat sõnavormi teise alluvaks või ülemuseks kuulutada on mõnevõrra kunstlik. Sellisteks konstruktsioonideks on näiteks kaassõna- või kvantoriühendid, verbiahelad, koordinatsioon. Nende keelendite analüüsil lähtub UD süsteem rohkem semantikast kui näiteks eesti keele sõltuvuspuude panga märgendamisel kasutatud kitsenduste grammatika (CG) märgendussüsteem. Nimelt:

\- kaassõna ülemuseks on käändsõna (*laua all*);  
\- kvantori ülemuseks on käändsõna (*kolm meest, pudel piima*) 

\- verbiahela ülemuseks on leksikaalne verb, mitte finiitne abiverbi, modaalverbi jms vorm (*pean tegema*), kolmest ja enamast komponendist koosnevat verbiahelat (*oleks pidanud ette nägema*) ei märgendata „ahela” vaid „põõsana”;  
\- koordineeritud üksused (*Luik, haug ja vähk*) on CG süsteemis samuti esitatud „ahelana” ning UD süsteemis „põõsana”. Koordineeritud sõnavormide ülemuseks on esimene koordineeritud element.

UD süsteem ei erista osalauseid ja infiniittarindeid (lauselühendeid), näiteks saavad sama märgendi täiendkõrvallause (relatiivlause) ja täiendina kasutatav infiniitne verbivorm.

Ka võrdsustab see süsteem verbi infiniitsed laiendid ja EKG II mõistes ahelverbi infiniitsed osad, st verbiahelaid (v.a. verbi liitvormid ja modaalkonstruktsioonid) ei üritatagi jagada ahelverbideks ja verb \+ laiend konstruktsioonideks.

Kasutusel on küll abiverbi märgend aux, mille saavad verbi *olema* vormid liitaegades ja koopulalausetes ning verbid *saama*, *võima* ning *pidama* modaalkonstruktsioonides. Ülejäänud finiitverbi ühendites infiniitsete verbivormidega saavad infiniidid märgendi xcomp või advcl.

UD märgendusskeemis on rikkalik märgendite repertuaar mitmesõnaliste leksikaalsete üksuste jaoks (fixed, flat, compound); selle poolest erinevad UD märgendid positiivselt eesti keele kitsenduste grammatika märgenditest.

## **Koopulalaused**

Kui lause põhiverbiks on verb *olema*, loetakse lause koopulalauseks ja juurtipuks ei ole mitte *olema* vorm, vaid mingi teine element lauses ning koopulana toimiv *olema*\-verbi vorm allub sellele ja saab abiverbi sõnaliigi märgendi AUX ning koopula süntaktilise märgendi cop. cop-l ei tohi olla alluvaid, st kõik, mis muidu on öeldise alluvad, on nüüd selle juurtipuks määratud sõna alluvad.

Koopulalauseteks EI OLE järgmised *olema*\-verbi sisaldavad laused:

1. Need, kus on ainult *olema*\-verb ja selle subjekt (pluss viimase täiendid); võib olla ka veel modaaladverb (*Oli tore õhtu*, *Raha ei ole ju, Raha küll ei ole*).  
2. Need, kus *olema*\-verb on ühendverbi osa (talle allub sõna märgendiga compound:prt)  
   olema-ga ühendverbid: t*arvis, vaja, läbi, ära, üle  olema* Seda hulka võib vajadusel täiendada

3. mas-vormis alluvaga olema, kus mõlemad osalised on sõnaliigiga VERB ja *olema* on osalause juurtipp. (mitte *ta on söömas* tüüp, aga *ta oli vette hüppamas* tüüp). Sagedasim selline konstruktsioon on *olemas olema*. mas-vorm selles konstruktsioonis on xcomp.  
4. kui öeldistäide on da-infinitiiv (mis siis on ccomp, nt *Kihk oli uurida midagi ürgset …*)  
5. Lause koosneb küsisõnast süntaktilise märgendiga mark, *olema*\-verbist ja alusest: *Kus on kirves?* Kas-küsimused siia alla ei käi.

**Koopulalause juurtipp** määratakse vastavalt järgmisele hierarhiale:

1. öeldistäide. *Kadri on inimene. Maja on suur.*

2. öeldistäitemäärus (T*a oli Valgas õpetajaks, Hiinlased on teistsuguse psühholoogiaga*)

3. öeldistäitesarnane määrus (*Kõik on halvasti, Nad olid kahekesi; Tal on klapid peas*).

ka: *tulemus oli 5 %. Tulemus oli üle viie protsendi. Aeg esimesel ringil oli 3:20.*

4. omaja ja kogeja (*Tal oli kodus kass; Tal oli kodus külm*)

5. Koht (*Ta oli õhtul kodus; ka Ta oli õhtul õnnetuna kodus*) 

6. Aeg (*See oli möödunud aastal*)

7. Viis (*See on nii, et ...*, ka *Sellega on nii, et...*)

## **Väljajättelised struktuurid ehk ellipsid**

Üldpõhimõtted.

Kui väljajäetud elemendil ei ole alluvaid, ei tehta midagi.

Kui väljajäetud elemendil on alluvad, siis „ülendatakse” üks neist väljajäetu asemele (=saab tema süntaktilise funktsiooni) ja teised, kui neid on,  alluvad talle. Nt lauses *Ostsin ühe kollase pliiatsi ja kaks roosat.* on *roosat* conj pliiatsi küljes ja *kaks* allub *roosale*.

Kui väljajäetud element on osalause tipp (öeldis), aga mõni abiverb on alles, siis abiverb ülendatakse põhiverbi kohale.

Muul juhul, kui väljajäetud element on osalause tipp (öeldis) siis ülendatakse üks tema alluvatest osalause tipuks vastavalt hierarhiale nsubj \> obj \> iobj \> obl \> advmod \> csubj \> xcomp \> ccomp \> advcl \> dislocated \> vocative. Kui lauses on mitu sama funktsiooniga „orvukest”, ülendatakse osalause tipuks see, mis on lausealgulisem.

Need sõnad, mille ülemus peaks olema see väljajätteline öeldis, on „ülendatud” moodustaja alluvad märgendiga orphan. Erandiks funktsioonisõnad, nt sidendid, nemad ei saa märgendit orphan, vaid oma tavalise märgendi. Nt lauses *Kass sööb pasteeti, aga koer konti*. on teise osalause ülemus sõnavorm *koer*, mis allub esimese osalause öeldisele *sööb* kui conj ja sõnavorm *konti* allub sõnavormile *koer* märgendiga orphan.

## **Absoluuttarindid e verbita lauselühendid** 

Absoluuttarindid (*kepp käes, kott üle õla*) on analüüsitud kui koopulalaused, mille juurtipuks on mitte-subjekt (*käes, õla*), tüüpiliselt funktsiooniga advcl ja  nominatiivne element (*kepp, kott*) on märgendatud kui sellele alluv subjekt. 

## **Muud sõltuvusstruktuuri küsimused**

Finiitse ja infiniitse verbi ühendites tekib sageli küsimus, kummale verbile ülejäänud lauseliikmed peaksid alluma. Mõnes lauses on see täiesti selge, mõnes mitte. Subjekt allub igal juhul finiitsele verbile. Lausetüübis *keelama/käskima/laskma/paluma* \+ kellelgi \+ da-infinitiiv, nt *keelasin koeral maad kraapida on* alalütlevas moodustaja *koeral* sisuliselt mõlema verbi alluv, aga on märgendatud finiitverbi (*keelan, käsen*, jne) alluvaks.

## **Eesti keele UD süntaktilised märgendid (*relations*)** 

Märkusena: näiteid saab otsida näiteks päringuvahendi grew.match abil https://universal.grew.fr/?corpus=UD\_Estonian-EDT@2.17\# 

### **Tuumargumendid** 

- **nsubj** – käändsõnaline subjekt, nt *Kass* *nägi koera*.

- **nsubj:cop** – koopulalauselause käändsõnaline subjekt, nt *Kass* *on triibuline.*

- **csubj** – infiniitne või osalauseline subjekt. Infiniitidest saab subjektiks olla ainult da-infinitiiv: *Tüdrukule meeldib* *tantsida.*

Osalauselise subjekti näide: *Aga mulle tundub, et kogu maailm ootab muusikamaailmalt midagi erutavalt uut minimalismi kõrvale.*

- **csubj:cop** – koopulalause infiniitne või osalauseline subjekt, nt *Imelik, et ma seda veel näidata julgen.  Seda vältida on võimatu.*

- **obj** – käändsõnaline objekt, nt *Kass nägi* *koera.* da-infinitiivne objekt saab märgendi xcomp.

- **xcomp** on heterogeenne kategooria, kuid ühendav tunnus on see, et see on predikaat, mille sisuline subjekt on “ülemuslause” subjekt, objekt või, harva, määrus:

*Kadri tahab suppi süüa. Kadri sundis lapse suppi sööma. Kadri käskis lapsel supi ära süüa.*

*Puulehed värvusid kollaseks. Kadri värvis aia kollaseks.*

Märgendi **xcomp** saavad:

1. ahelverbi infiniitsed osad, välja arvatud modaalverbide *saama, võima ja pidama* laiendid, nt *hakkan* *tegema*, *jäi* *magama, ajab* *nutma* jne,  
2. da-infiniitsed objektid, nt  *tahan* *teha,*  
3. Lisaks saavad märgendi xcomp ka translatiivsed predikatiivadverbiaalid, nt *President nimetas Juhani* *ministriks. Ta tegi selle* *raskeks.* ning essiivsed predikatiivadverbiaalid verbide *näima, paistma, tunduma, näikse, püsima, säilima, seisma, toimima, funktsioneerima, esinema, käituma, avalduma, teenima, töötama, käibima, kehtima, nägema, teadma, tundma* laiendina.  
4. Samuti saavad märgendi xcomp seotud laiendina toimivad otstarbemäärused, nt *Poiss võttis raamatu lugeda, See firma sobib vahendajaks.*  
5. Verbi *mata*\-vorm on xcomp verbide *jääma* ja *jätma* ning ühel korral verbi *hoidma* (*Uurija hoidis Sööti kaks nädalat järjest magamata*) seotud laiendina  
6. Verbi *mast*\-vorm on xcomp verbide *keelduma, hoiduma, takistama, tulema, väsima* jt seotud laiendina.  
   NB\! xcomp saab olla ainult verbi või adjektiivi alluv, nominalisatsioonis on vastav infiniit acl (*teha tahtmine*) ja vastav käändsõna oma sõnaliigi järgi nmod (*pühakuks kuulutamine*) või amod (*lolliks pidamine*)

- **ccomp**

1. verbi laiendav komplementlause, nt *Ta ütles, et tuleb homme. Tulen homme, ütles ta. Ta ütles: „Tulen homme.”*  
   Kuna samale verbile ei tohi UD valideerimisreeglite järgi alluda korraga sihitis ja ccomp, siis lauses  *Kui ministrid küsivad meie hinnanguid, siis seda me ka teeme, " ajab komissar Hannes Kont mõistujuttu.*  on root *ajab*, *mõistujuttu* on obj ja *teeme* on parataxis 

   vt ka https://universaldependencies.org/u/dep/ccomp.html\#reported-speech  
2. da-infinitiivne öeldistäide, nt *Tema eesmärk on ellu* *jääda.* *Olema*\-verb sel juhul on osalause juurtipp.

### **Muud laiendid** 

- **obl** – nimisõnaline (sh asesõnaline) määrus, nt *Kass põõnas* *diivanil*; ka koos kaassõnaga, nt *Kass põõnas* *palmi* *all*.

	-**obl** alaliigid (igal obl-l pole alaliiki):

	- **obl:agent** \- tegijamäärus, nt *Päästemeeskonna kohale jõudes põles kahekordne puidust elumaja täisleegis. Seni on kõik krüpteerimist murdvad programmid USA kohtu poolt keelatud.*

	- **obl:tmod** \- ajamäärus, nt *Avatud kuni 23\. maini. Lõuna paiku saabub Kadriorust kuller…*

	- **obl:lmod** \- kohamäärus, nt *See on kavandatud madala võserikuga soisele alale. Kui see juhtub, siis liigub tööpuuduse tase järkjärgult tagasi tasemeni, mis oli enne produktiivsuse kasvu.*

	- **obl:mode** \- viisimäärus, nt *Projekt valmis koostöös…, Naerab südamest.*

	- **obl:arg** \- sõltuvusmäärus, nt *…avaldub Vermeeri töödes…, …kus ta valdavalt toetus mõistatustele*.

	- **obl:state** \- seisundimäärus, nt *on heas vormis*, *jõudis tootmisse*.

	- **obl:quant** \- hulgamäärus, nt *raha oli suures osas ära kulutatud, sissetulek jääb 3000 krooni piirile.*

	- **obl:idiom** \- nimisõnalised määrusena märgendatud verbi alluvad, mis moodustavad koos verbiga idiomaatilise üksuse, nt *pani südamele, peab meeles*

- **nmod**  \- nimisõnaline (sh asesõnaline) täiend

- **appos** – lisand. Lisand saab praegu UD-s oma ülemusele ainult järgneda, mitte eelneda.

appos märgendi on saanud:

1. nimed, pealkirjad, jm, kui on olemas eelnev liigisõna: *arhitekt Boulle on üks minu kangelasi*   
   *Kust tuli mõte kirjutada ooper " Writing to Vermeer "? Jällegi täissaalile lugesid oma luulet ja tõlkeid marilane Vladimir Kozlov , komilane Niina Obrezkova , liivlane Valt Ernstreit , soomlane Kari Sallamaa jt .* 

2. Eesti keele traditsioonilise süntaksikäsitluse mõistes järellisand: *Keegi küsis , kuidas võidi Sallamaa kutsuda Ižkari detsembris, kõige trööstitumal aastaajal .* 

- **nummod** – arvsõnaline (sh ka numbritega kirjutatud) täiend, nt *aastal 2016. Paadis istus* *kolm* *meest. Orkaan tappis* *sadu* *inimesi. Selles asulas on 15* *800* *elanikku.* Viimases näites saab *15* märgendi compound. Pangem tähele, et hulgafraasi käsitletakse UD raamistikus nii, et hulgasõna on kvantifitseeritava sõna alluv, st eelnevates näidetes on sõna *meest* sõna *kolm* ülemus jne.

NB\! nummod on ainult täiendi märgend, muus funktsioonis arvsõnad märgendatakse vastavalt oma funktsioonile: nt *jagas kolmeks* on xcomp

- **amod** – adjektiivne täiend, nt *Triibuline* *kass lõi nurru.*

- **advcl** 

1. määruskõrvallause, nt *Kui sa tuled, too mul lilli.*  
2. infiniitne määruslik laiend, nt *Koer jooksis saba* *liputades* *mööda tänavat*. *Pikalt* *mõtlemata* *asus ta asja kallale*  
3. võrdlustarind; lausetes nagu *Üldiselt töötavad naised osaajaga enam kui mehed*. käsitletakse võrdluskonstruktsiooni *enam kui mehed* väljajättelisena (*enam kui mehed töötavad*) ja märgendatakse kui advcl, mitte kui advmod.

- **advmod** – määrsõnaline laiend (määrus); ka *kas* kas-küsimuste algul

	- **advmod:lmod** \- määrsõnaline kohamäärus, nt *läks kaugele ära*

	- **advmod:tmod** \-  määrsõnaline ajamäärus, nt *see on alati nii*

	- **advmod:mode** \- määrsõnaline viisimäärus *ajab edukalt oma igapäevaasju*

- **acl** – nimisõna infiniitne täiend, sh ka partitsiiptäiendid, nt *Õpetaja andis talle loa koju* *minna. Ema* *küpsetatud* *kook maitseb hea. Haukuv* *koer ei hammusta*

- **acl:relcl** \- täiendkõrvallaused: *Mees, kes seal seisab, on minu isa. See, et päike tõuseb iga päev, teda ei lohuta.*

täiendkõrval**laused** on kõik acl:relcl. Infiniitsed täiendid, lauselühendid täienditena on acl.

acl:relcl märgendi saab ka kõrvallause, millel on korrelaat pealauses. Korrelaat saab oma (ja kõrvallause) süntaktilise funktsiooni märgendi. St korrelaati laiendav kõrvallausel ei ole sama funktsioon, mis korrelaadil, vaid ta on korrelaadi täiend. 

*Mõtlesin seda, et varsti tuleb(acl:relcl-\>seda) suvi.*

- **case** – kaassõna, nt *Kass ronis diivani* *alla. Kass hüppas* *üle* *diivani.*

### **Muud verbi alluvad**

- **vocative** – üte, nt *Mari, tule palun siia\! Hooligan88 , kas sul on sidemeid-tutvusi mille kaudu see Viimsi muuseumi külastus kokku leppida?*

- **aux** – abiverb: *olema* verbi liitaegades; modaalverbid *saama, pidama, võima* modaalkonstruktsioonides; *ei* verbi eitavas vormis, *ära* ja *ärge* verbi käskiva kõneviisi eitavates vormides. Ülemuseks on leksikaalne verb, nt *olin* *teinud*; *saan* *teha,* *võin* *teha,* *pean* *tegema; ei tee,*  *ära* *tee,* *ärge* *tehke.*

- **cop** – koopula, verb *olema* koopulalausetes, kus öeldistäide (v.a infinitiivne või osalauseline) vm moodustaja saab märgendi root ja verbi *olema* vorm allub sellele, nt *Kass* *on* *triibuline*. *See raamat* *on* *minu oma. Mari on kodus.*

Kui koopula on verbi *olema* liitvorm (*Maja oli kunagi olnud punane*), siis ei allu verbivormid üksteisele vaid kumbki eraldi osalause juurtipule. 

- **mark** – alistavad sidendid osalause algul; küsisõnad küsilause algul, *nagu*, k*ui, otsekui, justkui* võrdlustarindites, nt *Supp on kuumem* *kui* *päike.* Sõnaliigiliselt on need adverbid ADV või alistavad sidendid SCONJ.

- **discourse** – hüüundid ja üneemid nagu *tere, ahah, noh, nojah, appi, aitäh* jms.

Samuti saavad selle märgendi nn partiklid (*Tõesti või icicic\!*) ja emotikonid. Samuti adressaati märkiv sümbol @ teatud foorumitekstides EWTB-s. 

### **Koordinatsioon** 

- **conj** – koordineeritud elemendid. Nende puhul märgendatakse esimene element oma süntaktilise funktsiooni märgendiga ning ülejäänud koordineeritud elemendid alluvad sellele märgendiga conj, nt *Luik,* *haug* *ja* *vähk* *vedasid vankrit.*

- **cc** \- koordineeriv sidend, ülemuseks on järgnev koordineeritud element nt *Luik, haug* *ja* *vähk vedasid vankrit.*

Ka lause alguses olev *aga* on cc*. Aga ilm on täna ilus.* 

- **cc:preconj** \- lahksidendi esikomponent. Praeguse seisuga saavad selle märgendi:

*nii* | *niihästi* | *niivõrd* (järelkomponent: *kui*); *kas* (*või*); *küll* (*küll*); *nii* | *sellepärast* (*et*); *selle asemel* | *vaatamata* | *hoolimata* | *enam* (*et*); *siis* | *samal ajal* (*kui*); *nii* (*nagu*) 

- **punct** – punktuatsioon. Punktuatsioon ei ole muidugi tegelikult lause süntaktilise struktuuri osa, nende ülemuste määramine käib järgmiselt. Lauselõpumärk allub juurtipule, välja arvatud juhul, kui sellest tekkiks ristuv kaar. Sulud, jutumärgid jm paariskirjavahemärgid alluvad nende vahel oleva konstruktsiooni kõrgeimale ülemusele, v.a. juhul, kui sellest tekiks ristuv kaar. 

Sidendite ja punktuatsioonimärkide ülemuseks on vahetult järgnev konjunkt.

### **Muu**

**root** – lause juurtipp, pealause öeldisverb, verbi liitvormi või ahelverbi puhul põhitähendust kandev komponent, nt *Sa oled palju ära* *teinud. Võid nüüd* *sööma* *hakata.* Koopulalause juurtipu määramise kohta vt Koopulalaused.

**dep** – spetsifitseerimata sõltuvus. St alluvussuhe on selgelt olemas, aga funktsiooni pole võimalik määrata. 

### **Mitmesõnalised üksused (sisemise struktuurita sõnaühendid)** 

**compound** – ühendab mitmesõnalisi leksikaalseid üksusi. Selle märgendi saavad

1. Mitmesõnalised arvud, nt *kolm tuhat seitsesada kaheksakümmend viis* märgendatakse nii, et ühendi viimane osis saab ühendi kui terviku süntaktilise funktsiooni märgendi ja ülejäänud osised on selle otsesed alluvad märgendiga compound. Nii on märgendatud ka muud numbrijadad, nt lauses *Kohtumine lõppes seisuga 1:2* on '2' '1' alluv märgendiga compound. 

Kuid tühikuga numbritega kirjutatud arvud (100 000\) on märgendatud märgendiga goeswith.

2. Väljendverbid, nt *aru saama, kirja panema, lukku panema, kätte andma, käest andma, tülli minema, kirja minema, käest minema, heaks kiitma, kätte jõudma, heaks arvama, lukku keerama, kätte maksma, heaks võtma, kätte võtma,*  jne

**compound:prt** ühendverbi afiksaaladverbiline osis, nt *leidis* *üles.* Ühendverbid on avatud hulk. 

**flat**  \- sellega märgendatakse eksotsentrilised, st selge ülemuseta sõnaühendid. Märgendi  flat puhul on ülemuseks alati mitmesõnalise üksuse esimene komponent ja teised alluvad talle. Märgendi flat saavad mh

1.  pärisnime osad. Pärisnime esimene osis märgendatakse pärisnime kui terviku süntaktilise funktsiooniga ja nime ülejäänud osad märgendatakse selle otseste alluvatena märgendiga flat, nt *New York, Carl Robert Jakobson*. Praeguses versiooni märgendataksegi suhtega name ainult isikunimed ja väike hulk kohanimesid. Kuid kui nimel on süntaktiline struktuur, märgendatakse teda selle struktuuri järgi, nt *Tartu Ülikool*.  
2.  Võõrkeelsed fraasid, nt *siis mõeldi just entry level kaamerate hindu*; *nn süsinikneutraalsele (carbon neutral) tasemele*

**fixed** – sellega märgendatakse grammatiseerunud sõnaühendeid, mis süntaktiliselt „töötavad” funktsioonisõnade või määrustena.

Sellena on märgendatud (*alati* tähendab "alati siis, kui nende vahel pole koma")

SIDENDID

- *ainult et* \- alati
- *enam kui* \- osad (*Seda valmistatakse enam kui 200 maitsevariatsioonis* \- fixed; *Seda on tervelt kaks korda enam kui eelmisel aastal* \- ei ole fixed)
- *enne kui* \- alati
- *eriti kui* \- alati
- ilma et \- alati
- *isegi kui* \- alati
- *just kui* \- alati
- *just nagu* \- alati
- *nii et* \- alati
- *nii kui* \- alati
- *nii nagu* \- alati
- *niipalju kui* \- alati
- *nõnda et* \- alati
- *nõnda nagu* \- alati
- *peaaegu et* \- alati
- *rohkem kui* \- osad (fixed lauses *Meid toetati rohkem kui miljoni krooniga*; ei ole fixed lauses *Õnnetusi on meil kaks korda rohkem kui Soomes*)
- *samas kui* \- alati
- *samuti kui* \- osad
- *samuti nagu* \- osad (*Koju, samuti nagu tema hingeelu salaurgastesse uudistama palutud keegi naljalt pole* \- fixed; *Hiina keisrid suhtusid välismaalastesse täpselt samuti nagu Rooma keisrid* \- ei ole fixed)
- *seeasemel et* \- alati
- *seni kuni* \- alati
- *ükskõik kuhu* \- alati
- *ükskõik kui* \- alati
- *ükskõik kuidas* \- alati
- *ükskõik kus* \- alati
- *ükspuha kus* \- alati
- *vaat et* \- alati
- *vaata et* \- alati
- *vähem kui* \- osad

MUU, st mitte-sidendid

- pseudoühilduvad väljendid sõnadega 'pool', 'poole', 'poolt', mh *igale poole, igal pool, igalt poolt* \- NB\! *iga* sõnaliik on siin PRON, mitte DET

*ühelt poolt, teiselt poolt, omalt poolt, mõlemalt poolt*

- ühendid sõnadega *iganes* ja *tahes*, mh *mis iganes, mis tahes*, *kus iganes, kus tahes*, jne  
- *tahes tahtmata*  
- ühendid sõnaga *teab*, mh *teab mis, teab kus, teab milline, teab mitmes*  
- *seda enam* konstruktsioonides *seda enam, et ..* aga muidugi mitte konstruktsioonis *seda enam ei tehta*  
- *eks ju*  
- *mis siis* lausetes nagu *mis siis sellest*, *mis siis ikka*   
- *kas või* lausetes nagu *Meenutagem kas või noort Peeter Volkonskit.*

### **Nõrgalt seotud suhete märgendid (*loose joining relations*)** 

**parataxis**

1. Kõrvuasendiga osalaused, mille vahel pole süntaktilist seost. Kui osalausete vahel on sidesõna või koma, on tegemist konjunktsiooniseosega. *Eesti on juba ammu üleerutatud seisundis: lugege päevauudiseid. Proloog \-- laupäev, 15\. mai.*  
2. Sulgudes osalaused ja lauseosad, nt *Samuti on ajaleht avaldanud vastulause juures oma kommentaari (08.01.99). Antud küsimuses laiema kultuurilise hoiaku (mis asi see on?) saavutamiseks ...* Samas: kui sulgudes on tõesti sama asi teise sõnaga öeldud, nt *TÜ (Tartu Ülikool)* või *Tartu Ülikool (TÜ)*, siis on suhe  appos.  
3. Kui otsese või kaudse kõne saatelause paikneb otse- või kaudkõne keskel, riputatakse ta otsekõne juurtipu külge märgendiga parataxis: *Kui sa tuled, ütles ta, too palun piima ka.*

**list** UD juhendi järgi peaks sellega märgendatama loendeid, aadresse jm loendisarnaseid asju.  Praegu on EDT-s märgendi list saanud aadressid, nt *Tartu, Kreutzwaldi 1* või struktuurid nagu *Teenuse kasutamiseks tuleb saata SMS sõnum kujul "PEATUS peatuse nimi liini number" lühinumbrile 1311\.*

**orphan** sellega märgendatakse märgenduse nn põhitasandil elliptilise öeldisega lausete elemente, mis muidu peaksid alluma öeldisele. Täpsemalt vt väljajättelised struktuurid.

**goeswith** sellega märgendatakse sõnad, mis ortograafiareeglite järgi peaksid olema kokku kirjutatud. Lisaks märgendatakse sellega ka numbritega kirjutatud arvud, mille keskel on tühik, nt 100 000\. Ülemuseks on esimene komponent. Selle alla käivad ka tühikutega telefoninumbrid.

Kõik sõltuvused on kirjeldatud ka kodulehel: [https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify\_deprel.pl?lcode=et](https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify_deprel.pl?lcode=et)

# **Täiustatud sõltuvused (*Enhanced Dependencies*)**

Vt ka [https://universaldependencies.org/u/overview/enhanced-syntax.html](https://universaldependencies.org/u/overview/enhanced-syntax.html)

Täiustatud märgendus ei ole kohustuslik, samuti võib UD juhendi järgi märgendatavate nähtuste loendist valida enda puudepangas märgendamiseks välja ainult mõned, aga EDT-s ja EWT-s on täiustatud sõltuvuste abil märgendatud kõik soovitatud keelendid, nimelt:

1. elliptilised predikaadid, nn nulltipud ja nende alluvad, st lause *Kass sööb konservi ja koer konti* täiustatud analüüsikihis on teise osalausesse lisatud kustutatud predikaat *sööb* ning sõna *koer* on selle nulltipu subjekt ning *konti* selle objekt.  
2. konjunktsiooniseoses olevate predikaatide subjektid, nt lauses *Koer sööb konti ja uriseb* on *Koer* märgendatud ka predikaadi *uriseb* subjektina.  
3. Koordinatsiooniseoses olevad subjektid ja objektid on otse seotud oma sisulise ülemusverbiga, nt lauses *Koer ja kass söövad* on verbivormil *söövad* kaks subjekti: *koer* ja *kass*.  
4. Kontrolli- ja tõstekonstruktsioonide jm sarnaste konstruktsioonide subjektid. UD süsteemis kasutatakse süntaktilist märgendit xcomp (*external complement*) selliste konstruktsioonide märgendamiseks, mida eesti traditsioonilises grammatikas käsitletakse ahelverbi osana (*Kass hakkab sööma*), da-infiniitse objektina (*Kass tahab süüa*) või öeldistäitemäärusena (*Kass muutus kurvaks*, *Kass värvis aia kollaseks*). Selliste konstruktsioonide puhul saab xcompina märgendatud verbil või ka öeldistäitemäärusel olla subjekt (*Kass sööb, Kass on kurb, Aed on kollane)* ja see subjekt võib pindmises süntaksikihis olla nii konstruktsiooni ülemusverbi subjekt, objekt kui ka määrus (*Lasen kassil konservi süüa \-\> Kass sööb konservi*).  
5. Relatiivpronoomenitega *kes* ja *mis* algavate relatiivlausete “tegelikud” subjektid, st on ära näidatud, et lauses *Kass, kes seal istub, on ilus* on *kass* verbi *istub* tegelik subjekt.

# **MISC e muu märgendus**

Nagu nimigi ütleb, on sellele väljale kuhjatud erinevat infot, erinevaid tunnuseid, nimelt:  
**SpaceAfter=No** \- sellel real oleva stringi ja järgmise stringi vahel pole tekstis tühikut, tavaline olukord kirjavahemärkide puhul.

**Lang** \- sõna keelsuse märgend mitte-eestikeelsete sõnade puhul.  
**OrigLang** \- sõna päritolukeel toorlaenude puhul.

**CorrectForm** \- ortograafiaveaga sõna õige vorm.

**Empty** \- eesti puudepanga spetsiifiline märgend, kasutatakse juhul, kui lausesse on lisatud elliptiline predikaat, nn null-node, siis saab see järjekorranumbriks talle eelneva sõna järjekorranumbri, millele lisatakse punkt ning selle sõna järjekorranumber “taastatud” fraasis, nt

```
17    meie    mina    PRON    P    Case=Gen|Number=Plur|Person=1|PronType=Prs    18    nmod    18:nmod    _  
18    kanalitelt    kanal    NOUN    S    Case=Abl|Number=Plur    3    conj    18.1:obl    _  
18.1    meeldib    meeldima    VERB    V    Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act    _    _    0:root|2:conj    Empty=18.1|Place=19  
18.2    jälgida    jälgima    VERB    V    VerbForm=Inf    _    _    18.1:csubj    Empty=18.2|Place=20  
19    “    “    PUNCT    Z    _    20    punct    20:punct    NE=B-Prod  
20    Kuldvillakut    kuldvillak    NOUN    S    Case=Par|Number=Sing    18    orphan  {#muud-verbi-alluvad}   18.2:obj    
```

**Place** \- eesti puudepanga spetsiifiline märgend, kõigil Empty märgendiga sõnadel on ka märgend Place, mis näitab selle tõelist järjekorranumbrit lauses. Vt eelnevat näidet.

## **NE (*Named Entities*)**

NE-algulise märgendiga on märgendatud nimeüksused. Neid märgendeid kasutatakse vaid eesti keele puudepankades. Teiste keelte puudepankade kirjelduses NE märgendus kas puudub või on kasutatud mõnda teist strateegiat.  Nimeüksused on märgendatud IOB-formaadis, st NE=B tähistab nimeüksuse algussõna, NE=I algusmärgendile B järgnevaid samasse nimeüksusesse kuuluvaid sõnu. Märgendatud nimeüksuste liigid on:

**Per** \- isik, elusolendite nimed. Inimeste, aga ka nt kasside jm nimed.  
**Loc** \- koht, nt *Emajõgi,  planeet Maa, (keegi viidi) Rakvere haiglasse, (avarii toimus) Võsu \- Vergi teel*  
**Gep** \- geopoliitiline üksus, koht, mis käitub organisatsioonina, õigemini küll mida esitatakse keeleliselt toimijana, elusana, personifitseerituna: *Moskva saatis kirja, Prantsusmaa otsustas nii, Ja üha irratsionaalsemaks muutuv Venemaa. Iirimaa võitis Eesti 2:0*  
**Org** \- organisatsioon. *BBC andmetel ..., Riigikogu võttis vastu otsuse…*  
**Prod** \- artefakt st “tehtud asi”, toode, ka teos, nt *“Püha õhtusöömaaeg”*, *“Tõde ja Õigus”*, *ajakiri Horisont, Berliini müür*  
**Event** \- sündmus, nt *teatrifestival Kuldne Mask* , *Külm sõda, Rakenduslingvistika Ühingu aastakonverents, Paide arvamusfestival, näitus "100 maailma kirjeldavat objekti"*  
**Muu** \- nimeüksus ei kuulu ühtegi eelnevasse kategooriasse   
**Unk** \- ei saa liigitada ebapiisava info tõttu

**Nime ulatus.** Liigisõna (*Tartu **linn,** Ülikooli **tänav,*** ) on nime osa.   
 Tiitel ei ole nime osa: ***härra** Greenaway*: *härra* pole nime osa

Pärisnimega algavad **liitsõnad** *Pariisi-reis, Nokia-vaimustus* ei ole nimeüksused.

Üksteise sees olevaid nimesid ei erista, st *Tartu ülikooli jalgpallimeeskond FC Fauna* on üks NE, mille liik on Org

**Kirjavahemärgid**  
Sellistel juhtudel nagu näiteks  *"Inimesed, ma kardan teid" \- niisugune veidi ehmatava pealkirjaga raamat,...* on nimeüksuse osaks ka jutumärgid ja koma.

**EDT-s ja EWT-s** kasutati erinevat lähenemist otsustamaks, kas sõna või sõnaühend on nimeüksus või mitte. EDT-s lähtuti ortograafiast, st oletati, et nimeüksuse koosseisus on pärisnimi, mida kirjutatakse suure algustähega. Veebitekstides me sellest oletusest ei lähtunud, st nimeüksus EWT-s ei pruugi sisaldada ühtegi suure algustähega sõna.  
nt *kui koidulas koolis käisin 10 aastat tagasi,...*  
*… aga dodo pizzas on ananassi, pohlade ja kondenspiimaga pitsa.*

## **Verbi argumendistruktuuri märgendus**

EDT korpuses on MISC väljal ka verbi argumendistruktuuri märgendus. See on eesti keele spetsiifiline. Kasutatud on PropBanki (https://propbank.github.io/) märgenduspõhimõtteid. Märgendatud on nende lihtverbide argumendistruktuurid, mis esinevad EDT-s vähemalt 14 korda. Verbi enda MISC-väljal on märgend Verb=verbi\_algvorm ja juhul kui verbil on mitu tähendust ja mitu argumendistruktuuri, siis ka tähenduse number. Selle verbi subjekti ja seotud laiendite MISC-väljal on argumendi number. Argumentide numeratsioon algab nullist. Näiteks: 
```
12    sõbrad    sõber    NOUN    S    Case=Nom|Number=Plur    13    nsubj    13:nsubj    Arg=tooma_Arg_0  
13    tõid    tooma    VERB    V    Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin|Voice=Act    7    conj    3:ccomp|7:conj    Verb=tooma_1  
14    kottidega    kott    NOUN    S    Case=Com|Number=Plur    13    obl    13:obl    _  
15    igasuguseid    iga_sugune    DET    P    Case=Par|Number=Plur|PronType=Ind    16    det    16:det    _  
16    raamatuid    raamat    NOUN    S    Case=Par|Number=Plur    13    obj    13:obj    Arg=tooma_Arg_1|SpaceAfter=No
```
