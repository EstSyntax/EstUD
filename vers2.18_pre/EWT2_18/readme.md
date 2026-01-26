EWT 2.17 puudepank asub [UD puudepanga portaalis](https://universaldependencies.org/treebanks/et_ewt/index.html).

Eesti UD puudepanga uue meedia korpuse eelversioon erineb eelmisest versioonist peamiselt lausestamise abistamiseks 
foorumi tekstide voorupiiride eristamiseks lisatud # newpar märgendite tõttu. Märgendid tähistavad lõiguvahetust ning on algsest korpusest
teisendamiste käigus kaduma läinud.

Katseliselt ilmnes, et uue meedia korpuse nõrgim lüli automaatselt analüüsil on lausestamine, vale lausestus aga tähendab ka vigu analüüsis.

Samuti on parandatud NOUN-PROPN vigu. Nimede  eristamine uue meedia tekstides ei ole triviaalne ülesanne. Sageli võtavad omale kasutajad nimeks 
juhusliku nimisõna, tähe-numbrikombinatsiooni või hoopis sümbolite jada. Samuti võib tekstis sees olla nimekasutus väiksetäheline.

Sisseviidud muudatused näitasid, et parser (UDPipe ewt217 mudelil) suutis  lauseid tuvastada 6,5% paremini, kuid see mõjutas UAS/LAS näitajaid 
ligikaudu 0,6-0,7%.

Katsed näitasid ka, et ewt test- ja trainjaotuse puudepankade parsimisel edt2.17 mudeliga on erinevused suured, mida saab seletada ainult sellega, 
et juhuslikult on testkorpusesse sattunud parseri jaoks keerulised tekstid. Olukord ühtlustuks, kui kogu puudepank oleks suurem.

Järgmine täisversioon avaldatakse mais 2026 [UD portaalis](https://universaldependencies.org/).
