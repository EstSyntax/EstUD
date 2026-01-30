# Töö käik eesti keele puudepankade üleslaadimiseks universaldependencies.org portaali

## Puudepanga failid
- Failid on jagatud Dev, Test ja Train kataloogidesse
- Iga EDT puudepanga faili identifikaator näitab teksti žanri (aja, ilu, tea, arborest)
- Mõistlik on faile redigeerida ühekaupa ning nad siis kokku kleepida kolmeks dev-, test- ja train-failiks

## Valideerimine
1. Jälgida [valideerimisraportit](https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/validation-report.pl) 
2. Vigade korral laadida alla uusim validaator ud githubist tools kataloogist - pigem vajalik kogu [tools kataloog](https://github.com/UniversalDependencies/tools)
vt [juhendit](https://universaldependencies.org/contributing/validation.html#running-the-validator-locally)
3. > cat file |~/git/tools/validate.py --lang=et

## Redigeerimine
Kui CONLLU formaat on võõras, siis kasutada ainult spetsredaktoreid, näiteks [conllueditor](https://universaldependencies.org/tools.html#conllueditor)

## Kokkupanek
Faile on  mugav kokku panna shelli scripti abil

```
#!/bin/sh
cat Train/*.conllu > et_ewt-ud-train.conllu
cat Test/*.conllu > et_ewt-ud-test.conllu
cat Dev/*.conllu > et_ewt-ud-dev.conllu

python3 tools/tools-master/validate.py --lang et et_ewt-ud-train.conllu
python3 tools/tools-master/validate.py --lang et et_ewt-ud-test.conllu
python3 tools/tools-master/validate.py --lang et et_ewt-ud-dev.conllu


 udapy -TAM ud.MarkBugs < et_ewt-ud-train.conllu >vead1.txt
 udapy -TAM ud.MarkBugs < et_ewt-ud-test.conllu >vead2.txt
 udapy -TAM ud.MarkBugs < et_ewt-ud-dev.conllu >vead3.txt
 
 cat et_ewt-ud-train.conllu | udapy util.Wc
 cat et_ewt-ud-test.conllu | udapy util.Wc
 cat et_ewt-ud-dev.conllu | udapy util.Wc
``` 

Siin [udapy](https://github.com/udapi/udapi-python) kasutamine on soovitatav, moodul ud.MarkBugs leiab üles ka küsitavad kohad, mis pole otseselt vead, util.Wc genereerib statistika puudepanga jaoks.
Failide nimed on olulised, EWT puudepangal on nimes ewt, EDT puudepangal vastavalt edt.

## Üleslaadimine
Versioonivahetus toimub kaks korda aastas,  mais ja novembris. Kui validaator viga ei näita ja muudatusi pole, siis ei pea puudepanka uuendama.

Kui EWT-puudepanka on võimalik üles laadida ka otse githubi veebiliidese kaudu [EWT lehe dev-harusse](https://github.com/UniversalDependencies/UD_Estonian-EWT/tree/dev),
siis EDT vajab oma mahu tõttu käsurealahendust. Vt [üldist juhist](https://universaldependencies.org/contributing/index.html).
Oluline on silmas pidada, et kasutataks **dev-haru**.



