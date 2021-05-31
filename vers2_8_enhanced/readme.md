# Enhanced versions of Estonian universal dependencies treebanks

[UD EWT treebank](https://github.com/UniversalDependencies/UD_Estonian-EWT/tree/master) consists of different genres of new media. [UD EDT treebank](https://github.com/UniversalDependencies/UD_Estonian-EDT/tree/master) consists of genres of fiction, newspaper texts and scientific texts.
Enhanced dependcies ([see](https://universaldependencies.org/u/overview/enhanced-syntax.html)) have been added as following:
* Empty nodes for elided predicates - manually
* Propagation of incoming dependencies to conjuncts - automatically using [Treex](https://github.com/ufal/treex) software
* Propagation of outgoing dependencies from conjuncts - automatically using Treex
* Additional subject relations for control and raising constructions - automatically using Treex
* Coreference in relative clause constructions - manually
* Modifier labels that contain the preposition or other case-marking information - automatically using Treex
