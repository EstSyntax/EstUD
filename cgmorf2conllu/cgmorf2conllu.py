#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import glob
import os
import re
import sys

if sys.version_info<(3,4,0):
	sys.stderr.write("You need python 3.5 or later to run this script\n")
	exit(1)

import codecs

from argparse import ArgumentParser

####################
#	remove repeated values from array
####################
def uniqArray(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]




####################
#	check Python version
####################
def isPythonVersion(version):
	if float(sys.version[:3]) == version:
		return True
	else:
		return False

####################
#	colored terminal output
####################
class bColors:
	colors1 = (
		'\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[1;38m',
		'\033[1;39m'
	)
	
	style = {
		'bold': '\033[1m'
		, 'red': '\033[1;31m'
		, 'green': '\033[0;32m'
		, 'yellow': '\033[0;33m'
		, 'blue': '\033[0;34m'
		, 'endc': '\033[0m'
	}
	pattern_red = style['red'] + '%s' + style['endc']
	pattern_yellow = style['yellow'] + '%s' + style['endc']
	pattern_green = style['green'] + '%s' + style['endc']
	pattern_blue = style['blue'] + '%s' + style['endc']
	pattern_bold = style['bold'] + '%s' + style['endc']
	
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

####################
#	print to STDERR
####################
def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)


if __name__ == '__main__':
	if sys.stdout.encoding is None:
		eprint(
			bColors.pattern_red % "please set python env PYTHONIOENCODING=UTF-8, example: export PYTHONIOENCODING=UTF-8, when write to stdout.")
		exit(1)


######################
#	find all lemma-rule files in dir. 
#	Pattern is /^[A-Z]+_.+$/
#	POS_smth.txt
######################
def read_parse_dict_folder(lemmalist_dir):
	posDictFiles = []
	try:
		posDictFiles = os.listdir(lemmalist_dir)
	except FileNotFoundError:
		eprint(bColors.pattern_red % ('Cannot open lemma POS rules folder: ' + wordlist_dir))
	for file in posDictFiles:
		pattern = re.compile("^[A-Z]+_.+$")
		if pattern.match(file):
			read_parse_dict(lemmalist_dir+'/'+file)

######################
#	read rules from dict
#	LEMMA _TAB_ POS _TAB_ FEATURES
######################
def read_parse_dict(dictname):
	#nimest äkki välja lugeda sõnaliik
	global POSdict
	filename = (dictname.split('/'))[-1]
	pos = (filename.split('_'))[0]
	if not pos in POSdict:
		POSdict[pos] = {}
	try:
		f_dict = codecs.open(dictname, "r", "utf-8")
		eprint(bColors.pattern_green % ('Read \'%s\' rules from : %s' %(pos, dictname)))
	except IOError:
		eprint(bColors.pattern_red % ('Cannot open POS dictionary: ' + dictname))
		exit()
		
	with f_dict as fp:
		for line in fp:
			line = line.strip()
			if line == '':
				continue
			aRow =  line.split("\t")
			if len(aRow)>2:
				POSdict[pos][aRow[0]] = {}
				POSdict[pos][aRow[0]]['pos']=aRow[1]
				POSdict[pos][aRow[0]]['features'] = []
				if (len(aRow)>2):
					POSdict[pos][aRow[0]]['features']=aRow[2].split(' ')	
	
############################
#	make dict from inforem sentence-lines array
############################
def makeDictFromArray(aSentence, i=None):
	sentence_dict = {'lines': {}}
	# sentence_dict['lines'][lineid]['type'] == 'token'
	# dict['analys']={}
	#           dict['analys']['lemma']=[]
	#          dict['analys']['case']=[]
	#         dict['analys']['morf']=[]
	#        dict['analys']['lemma'].append('ERROR!!! '+line)
	#        dict['analys']['case'].append('')
	#        dict['analys']['morf'].append(line)
	
	""""
		<Kord>"
			"kord" L0 D @ADVL #1->4
		"<olid>"
			"ole" Lid V aux indic impf ps3 pl ps af @FCV #2->4
		"<need>"
			"see" Ld P dem pl nom @OBJ #3->4
		"<suunatud>"
			"suuna" Ltud V main partic past imps @IMV #4->0
	"""
	token_line_pattern = '^"<(.+)>"$'
	lemma_line_pattern = '"(.+)" ([^\@]+)(\@.+)*( #(\d+->\d+))$'
	#lemma_line_pattern = '"(.+)" ([^\@]+)(\@.+)*( #(\d+->\d+))?$'
	morf_pattern = '^(L([^\s]+) )*([A-Z])([A-Za-z\d\s\?\<\>\-üõöä]+)*$'
	
	analyze_line_pattern =  '^"(.+)" [A-Z]'
	
	compiled_pattern_tokenline 		= re.compile(token_line_pattern)
	compiled_pattern_lemmaline 		= re.compile(lemma_line_pattern)
	compiled_pattern_analyzeline 	= re.compile(analyze_line_pattern)
	
	#rea alguse kindla struktuuriga elemendid
	compiled_pattern_analyzeline_lemma 	= re.compile('^"(.+?)" ')
	compiled_pattern_analyzeline_case 	= re.compile('^(L([^\s]+)) ')
	compiled_pattern_analyzeline_pos 	= re.compile('^([A-Z]) ?')
	
	
	#rea lõpu kindla struktuuriga elemendid
	compiled_pattern_analyzeline_relation = re.compile(' #(\d+->\d+)$')
	compiled_pattern_analyzeline_function = re.compile('(\@[^\s]+)$')
	
	
	
	line_id = 0
	for s in aSentence:
		
		# print (s)
		
		match_token = compiled_pattern_tokenline.match(s)
		match_analyzeline = compiled_pattern_analyzeline.match(s)
		
		if match_token:
			line_id += 1
			sentence_dict['lines'][line_id] = {}
			sentence_dict['lines'][line_id]['type'] = 'token'
			sentence_dict['lines'][line_id]['info'] = {}
			sentence_dict['lines'][line_id]['info']['analys'] = {}
			sentence_dict['lines'][line_id]['info']['analys']['lemma'] = []
			sentence_dict['lines'][line_id]['info']['analys']['case'] = []
			sentence_dict['lines'][line_id]['info']['analys']['morf'] = []
			sentence_dict['lines'][line_id]['info']['analys']['pos'] = []
			sentence_dict['lines'][line_id]['info']['analys']['function'] = []
			sentence_dict['lines'][line_id]['info']['analys']['relation'] = []
			sentence_dict['lines'][line_id]['info']['token'] = match_token.group(1)
		elif match_analyzeline:
			#"<Esimestel>"
			#"esimene" Ltel N ord pl ad l cap @AN> #1->2
			#"<kordadel>"
			#"kord" Ldel S com pl ad @ADVL #2->10
			#"<oli>"
			#"ole" Li V main indic impf ps3 sg ps af <FinV> <Intr> <0> @FMV #3->0
			#"<mul>"
			#"mina" Ll P pers ps1 sg ad @ADVL #4->3
			#hakkame eest ja tagant rida 'lammutama'
			#analyzeline = s
			#if (analyzeline
			lemma 		= ''
			morf 		= ''
			function 	= ''
			morf		= ''
			pos 		= ''
			case 		= ''
			relation 	= '%d->%d' % (line_id, line_id)
			
			analyzeline = s
			
			#elements from the beginning of the line
			#compiled_pattern_analyzeline_lemma 	= re.compile('^"(.+?)" ')
			match_analyze_lemma = compiled_pattern_analyzeline_lemma.match(analyzeline)
			if match_analyze_lemma:
				lemma = match_analyze_lemma.group(1).strip()
				analyzeline = compiled_pattern_analyzeline_lemma.sub('', analyzeline, 1).strip()
			
			#compiled_pattern_analyzeline_case 	= re.compile('^(L([^\s]+)) ')
			match_analyze_case = compiled_pattern_analyzeline_case.match(analyzeline)
			if match_analyze_case:
				case = match_analyze_case.group(1).strip()
				analyzeline = compiled_pattern_analyzeline_case.sub('', analyzeline, 1).strip()
			
			#compiled_pattern_analyzeline_pos 	= re.compile('^([A-Z]) ?')	
			match_analyze_pos = compiled_pattern_analyzeline_pos.match(analyzeline)
			if match_analyze_pos:
				pos = match_analyze_pos.group(1).strip()
				analyzeline = compiled_pattern_analyzeline_pos.sub('', analyzeline, 1).strip()
				
			
			#elements from the end of the line
			#compiled_pattern_analyzeline_relation = re.compile(' #(\d+->\d+)$')
			match_analyze_relation = compiled_pattern_analyzeline_relation.search(analyzeline)
			
			if match_analyze_relation:
				relation = match_analyze_relation.group(1).strip()
				analyzeline = compiled_pattern_analyzeline_relation.sub('', analyzeline, 1).strip()
			
			#compiled_pattern_analyzeline_function = re.compile('(\@[^\s]+)$')
			match_analyze_function = compiled_pattern_analyzeline_function.search(analyzeline)
			if match_analyze_function:
				function = match_analyze_function.group(1).strip()
				analyzeline = compiled_pattern_analyzeline_function.sub('', analyzeline, 1).strip()
			
			
			#rest part of the line is morf
			
			morf = analyzeline.lower()
			
			
			
			if pos == '':
				eprint()
				if i:
					eprint(bColors.pattern_blue % 'Unable to parse morf info, sentence %d line %d ' % (i, line_id), morf)
				else:
					eprint(bColors.pattern_blue % 'Unable to parse morf info, line %d ' % line_id, morf)
			
			
			#eprint (s)
			#eprint (analyzeline)

			sentence_dict['lines'][line_id]['info']['analys']['lemma'].append(lemma)
			sentence_dict['lines'][line_id]['info']['analys']['case'].append(case)
			
			sentence_dict['lines'][line_id]['info']['analys']['morf'].append(morf)
			sentence_dict['lines'][line_id]['info']['analys']['pos'].append(pos)
			sentence_dict['lines'][line_id]['info']['analys']['function'].append(function)
			sentence_dict['lines'][line_id]['info']['analys']['relation'].append(relation)
			
		else:
			eprint()
			eprint(bColors.pattern_red % 'Unknown line format, sentence %d, line %d ' % (i, line_id), s)
		# eprint (aSentence)
		
	#print (sentence_dict)
	return sentence_dict



################################
#	make conllu sentence line prefix
#	# sent_id = 1
#   # text = Lause tekst siia ühele reale.
################################

def construct_sentid_conllu(sent_id):
	#	# sent_id = 1
	conll_line = '# sent_id = %d' % sent_id
	return conll_line


def construct_senttext_conllu(sentence):
	#   # text = Lause tekst siia ühele reale.
	tokens = []
	for line_id in sorted(sentence['lines']):
		tokens.append(sentence['lines'][line_id]['info']['token'])
	return '# text = %s' % (' '.join(tokens))

################################
#	make conllu format line from sentence dict
################################
def construct_line_conllu(dict_info, line_id):
	
	conll_line = ''
	
	for i, v in enumerate(dict_info['analys']['lemma']):
		if (i>0): continue;
		lemma = v
		morf = dict_info['analys']['morf'][i]
		case = dict_info['analys']['case'][i]
		pos = dict_info['analys']['pos'][i]
		if 'pos2' in dict_info['analys']:
			pos2 = dict_info['analys']['pos2'][i]
		else:
			pos2 = pos
		function =  dict_info['analys']['function'][i]
		relation =  (dict_info['analys']['relation'][i].split('->'))[1]
		#print (dict_info['analys']['relation'][i].split('->'))
		if dict_info['analys']['function'][i] == '':
			function = '_'
		
		# conllu description http://universaldependencies.org/format.html
		# ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes.
		# FORM: Word form or punctuation symbol.
		# LEMMA: Lemma or stem of word form.
		# UPOSTAG: Universal part-of-speech tag.
		# XPOSTAG: Language-specific part-of-speech tag; underscore if not available.
		# FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
		# HEAD: Head of the current word, which is either a value of ID or zero (0).
		# DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
		# DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
		# MISC: Any other annotation.
		
		
		#kui tulp tühi, siis tühi '_'
		#ID
		col1 = str(line_id)	
		#FORM
		col2 = dict_info['token']
		#LEMMA
		col3 = lemma
		# UPOSTAG
		col4 = pos2
		# ?XPOSTAG
		col5 = pos
		# FEATS:
		col6 = morf.replace(' ','|')
		# HEAD:
		col7 = relation

		# ? DEPREL:
		col8 = function
		# ? DEPS:
		col9 = '_'
		# MISC:
		col10 = '_'
		
		
		if conll_line != '':
			conll_line += "\n"
		
		conll_line += "\t".join([col1, col2, col3, col4, col5, col6, col7, col8, col9, col10])
		
	return conll_line


def fix_connlu_features(features_array):
	features_dict = {}
	features_fixed = []
	for i, v in enumerate(features_array):
		feature = v.split('=')
		if len(feature) == 2:
			(feature_name, feature_value) = feature
			if not feature_name in features_dict:
				features_dict[feature_name] = []
			features_dict[feature_name] = features_dict[feature_name] + feature_value.split(',')
		#eprint (feature)
		#eprint (features_dict)
		
	for feature in sorted(features_dict):
		features_fixed.append('%s=%s' % (feature, ','.join(sorted(uniqArray(features_dict[feature])))))	
	return sorted(features_fixed)

################################
#	change (translate) sentence dict compabtible to conllu format
################################
def translateToConllu(dict_info, flags = '', sentence_id=None):
	#[pos][wordform]->newPOS 
	global POSdict

	dict_info['analys']['pos2'] = []
	
	
	for i, v in enumerate(dict_info['analys']['lemma']):
		if (i > 0):
			#eprint(bColors.pattern_red % ('Ambiguity in sentence %d'%sentence_id), dict_info['analys']['lemma'])
			next;
			
		a_morf = dict_info['analys']['morf'][i].split(' ')
		
		pos2 = dict_info['analys']['pos'][i]
		pos = dict_info['analys']['pos'][i]
		conllu_features = []
		
		
		# add "ma" ending to Verbs except 'ei', 'ära'
		if pos == 'V' and 'm' in flags and not dict_info['analys']['lemma'][i] in ['ei', 'ära'] :
			dict_info['analys']['lemma'][i] = dict_info['analys']['lemma'][i] + 'ma'
		
		lemma = dict_info['analys']['lemma'][i]
		wordform = dict_info['token']
		
		
		
		#POS TAG translation rules
		
		## S
		
		#first priority is for pos-lemma file rules
		if pos in POSdict and lemma in POSdict[pos]:
			#eprint(bColors.pattern_green % "MATCH", lemma)
			pos2 = POSdict[pos][lemma]['pos']
			#siin on loogika veidi dubleeritud 
			if len(POSdict[pos][lemma]['features']):
				conllu_features = list(POSdict[pos][lemma]['features'])
				#eprint(bColors.pattern_green % "MATCH", conllu_features)
		    
		
		#kui failis polnud sobivat infot, siis läheb reeglite järgi
		elif pos == 'S' and 'com' in a_morf:
			pos2 = 'NOUN'
		elif pos == 'S' and 'prop' in a_morf:
			pos2 = 'PROPN'
		
		## A
		elif pos == 'A' and 'pos' in a_morf:
			pos2 = 'ADJ'
			conllu_features.append('Degree=Pos')
		#???
		#if pos == 'A' and '???' in a_morf:
		#	pos2 = 'DET'
		elif pos == 'A' and 'comp' in a_morf:
			pos2 = 'ADJ'
			conllu_features.append('Degree=Cmp')
		elif pos == 'A' and 'super' in a_morf:
			pos2 = 'ADJ'
			conllu_features.append('Degree=Sup')
		
		## P
		elif pos == 'P':
			pos2 = 'PRON'
			conllu_features.append('PronType=Dem,Int,Ind,Prs,Rcp,Rel,Tot')
			
		## N
		elif pos == 'N' and 'card' in a_morf:
			pos2 = 'NUM'
			conllu_features.append('NumType=Card')

		elif pos == 'N' and 'ord' in a_morf:
			pos2 = 'ADJ'
			conllu_features.append('NumType=Ord')
	
		## K
		elif pos == 'K' and 'pre' in a_morf:
			pos2 = 'ADP'
			conllu_features.append('AdpType=Prep')
		elif pos == 'K' and 'post' in a_morf:
			pos2 = 'ADP'
			conllu_features.append('AdpType=Post')
	
		## D
		elif pos == 'D':
			pos2 = 'ADV'
		
		## V
		elif pos == 'V' and 'main' in a_morf:
			pos2 = 'VERB'
		elif pos == 'V' and 'aux' in a_morf:
			pos2 = 'AUX'
		elif pos == 'V' and 'mod' in a_morf:
			pos2 = 'AUX'

		## J
		elif pos == 'J' and 'crd' in a_morf:
			pos2 = 'CCONJ'
		elif pos == 'J' and 'sub' in a_morf:
			pos2 = 'SCONJ'

		
		## Y
		elif pos == 'Y' and re.search('[A-ZÜÕÖÜ]', lemma):
			pos2 = 'PROPN'
			conllu_features.append('Abbr=Yes')
		elif pos == 'Y':
			pos2 = 'SYM'
			conllu_features.append('Abbr=Yes')

		## X
		elif pos == 'X':
			pos2 = 'ADV'
		
		## Z
		elif pos == 'Z':
			pos2 = 'PUNCT'
			
		## T
		elif pos == 'T':
			pos2 = 'X'
		
		## I
		elif pos == 'I':
			pos2 = 'INTJ'
		#??
		#elif pos == 'I':
		#	pos2 = 'SYM'
		#elif pos == 'I':
		#	pos2 = 'X'
		
		## B
		elif pos == 'B':
			pos2 = 'PART'
		
		## E
		elif pos == 'E':
			pos2 = 'SYM'
		
		
		## G
		elif pos == 'G':
			pos2 = 'NOUN'
			conllu_features.append('Number=Sing')
			conllu_features.append('Case=Gen')
		
		
			
		dict_info['analys']['pos2'].append(pos2)
		
		
		#morf tunnused -> conllu_features
		
		#Number=X
		if 'sg' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM', 'VERB', 'AUX']:
			conllu_features.append('Number=Sing')
		if 'pl' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM', 'VERB', 'AUX']:
			conllu_features.append('Number=Plur')	
		#VerbForm=
		if 'inf' in a_morf:
			conllu_features.append('VerbForm=Inf')
			
		if 'ger' in a_morf:
			conllu_features.append('VerbForm=Conv')
			
		if 'sup' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('VerbForm=Sup')
			
		if 'partic' in a_morf and pos2 in ['ADJ', 'VERB', 'AUX']:
			conllu_features.append('VerbForm=Part')
		
		
		#Case=X
		if 'nom' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Nom')
			
		if 'gen' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Gen')
			
		if 'part' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Par')
			
		if 'ill' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ill')
		if 'ill' in a_morf and pos2 in ['VERB', 'AUX'] and 'VerbForm=Sup' in conllu_features:
			conllu_features.append('Case=Ill')
			
		if 'adit' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Add')
			
		if 'in' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ine')
		if 'in' in a_morf and pos2 in ['VERB', 'AUX'] and 'VerbForm=Sup' in conllu_features:
			conllu_features.append('Case=Ine')
			
		if 'el' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ela')	
		if 'el' in a_morf and pos2 in ['VERB', 'AUX'] and 'VerbForm=Sup' in conllu_features:
			conllu_features.append('Case=Ela')
			
		if 'all' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=All')	
			
		if 'ad' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ade')
			
		if 'abl' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Abl')
			
		if 'tr' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Tra')
		if 'tr' in a_morf and pos2 in ['VERB', 'AUX'] and 'VerbForm=Sup' in conllu_features:
			conllu_features.append('Case=Tra')	
			
		if 'term' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ter')
			
		if 'es' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Ess')
			
		if 'abes' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Abe')		
		if 'abes' in a_morf and pos2 in ['VERB', 'AUX'] and 'VerbForm=Sup' in conllu_features:
			conllu_features.append('Case=Abe')
			
		if 'kom' in a_morf and pos2 in ['NOUN', 'PROPN', 'ADJ', 'DET', 'PRON', 'NUM']:
			conllu_features.append('Case=Com')
			
		#Degree=	 
		if 'pos' in a_morf and pos2 in ['ADJ']:
			conllu_features.append('Degree=Pos')
		if 'comp' in a_morf and pos2 in ['ADJ']:
			conllu_features.append('Degree=Cmp')
		if 'super' in a_morf and pos2 in ['ADJ']:
			conllu_features.append('Degree=Sup')

		#NumForm=	 
		if 'digit' in a_morf and pos2 in ['ADJ'] and 'NumType=Ord' in conllu_features:
			conllu_features.append('NumForm=Digit')
		if 'digit' in a_morf and pos2 in ['NUM']:
			conllu_features.append('NumForm=Digit')
		elif lemma.isdigit() and pos2 in ['NUM']:
			conllu_features.append('NumForm=Digit')
		
		if 'l' in a_morf and pos2 in ['ADJ'] and 'NumType=Ord' in conllu_features:
			conllu_features.append('NumForm=Letter')
		if 'l' in a_morf and pos2 in ['NUM']:
			conllu_features.append('NumForm=Letter')	
			
		if 'roman' in a_morf and pos2 in ['ADJ'] and 'NumType=Ord' in conllu_features:
			conllu_features.append('NumForm=Letter')
		
		
		#Person=
		if 'ps1' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Person=1')
			
		if 'ps2' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Person=2')
			
		if 'ps3' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Person=3')
			
		#Polarity=
		#if 'af' in a_morf and pos2 in ['VERB', 'AUX']:
		#	conllu_features.append('Polarity=Pos')

		if 'neg' in a_morf and lemma in ['ei','ära']:
			conllu_features.append('Polarity=Neg')
		elif 'neg' in a_morf and pos2 in ['VERB','AUX'] and wordform in ['pole','Pole','polnud','Polnud','poldud','Poldud','poleks','Poleks','poleksid','Poleksid','polegi','Polegi','polnudki','Polnudki']:
			conllu_features.append('Polarity=Neg')
		elif 'neg' in a_morf and pos2 in ['VERB','AUX']:
			conllu_features.append('Connegative=Yes')
		
		#Voice=
		if 'ps' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Voice=Act')
		if 'imps' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Voice=Pass')
			
		#Tense=
		if 'impf' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Tense=Past')
			
		if 'past' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Tense=Past')
			
		if 'pres' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Tense=Pres')
		
		#Voice= and #Tense=
		if '<v>' in a_morf and 'partic' in a_morf:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Act')
		
		if '<tav>' in a_morf and 'partic' in a_morf:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Pass')
		if 'tav' in lemma[-3:] and 'partic' in a_morf:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Pass')
		elif 'tav' in lemma[-3:] and pos2 in ['ADJ'] and lemma not in ['ustav','pool_tuttav','tuttav','naeratav','joonistav','äratav','isu_äratav','pimestav','otsustav','pimestav','ehmatav','tõotav','rahustav','uinutav','lömitav']:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Pass')
			conllu_features.append('VerbForm=Part')
		elif 'v' in lemma[-1:] and 'partic' in a_morf:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Act')
		elif 'v' in lemma[-1:] and pos2 in ['ADJ'] and lemma not in ['harv','igav','imal-terav','kirev','kuiv','lõtv','odav','osav','pool_tuttav','pidev','pinev','põnev','terav','tugev','tuttav','sügav','ustav','verev','vägev']:
			conllu_features.append('Tense=Pres')
			conllu_features.append('Voice=Act')
			conllu_features.append('VerbForm=Part')
		
		if 'nud' in lemma[-3:] and 'partic' in a_morf:
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Act')
		elif 'nud' in lemma[-3:] and pos2 in ['ADJ'] and len(conllu_features) <= 2: #jama
			conllu_features.append('VerbForm=Part')
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Act')	
			
		if 'tud' in lemma[-3:] and 'partic' in a_morf:
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Pass')	
		elif 'tud' in lemma[-3:] and pos2 in ['ADJ'] and len(conllu_features) <= 2: #jama
			conllu_features.append('VerbForm=Part')
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Pass')
		if 'dud' in lemma[-3:] and 'partic' in a_morf:
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Pass')	
		elif 'dud' in lemma[-3:] and pos2 in ['ADJ'] and len(conllu_features) <= 2: #jama
			conllu_features.append('VerbForm=Part')
			conllu_features.append('Tense=Past')
			conllu_features.append('Voice=Pass')
		if 'mata' in lemma[-4:] and 'partic' in a_morf:
			conllu_features.append('Case=Abe')
			conllu_features.append('Voice=Act')	
			conllu_features.append('VerbForm=Sup')
			conllu_features.remove('VerbForm=Part')
		#if 'tud' in lemma[-3:]:
		#        eprint(bColors.pattern_red % conllu_features)
								
		
		#Mood= and VerbForm=
		if 'indic' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Mood=Ind')
			conllu_features.append('VerbForm=Fin') #??
			
		if 'imper' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Mood=Imp')
			conllu_features.append('VerbForm=Fin') #??
			
		if 'cond' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Mood=Cnd')
			conllu_features.append('VerbForm=Fin') #??
			
		if 'quot' in a_morf and pos2 in ['VERB', 'AUX']:
			conllu_features.append('Mood=Qot')
			conllu_features.append('VerbForm=Fin') #??
			
		if 'sup' in a_morf and 'VerbForm=Fin' in conllu_features:
			conllu_features.remove('VerbForm=Fin')
		if 'inf' in a_morf and 'VerbForm=Fin' in conllu_features:
			conllu_features.remove('VerbForm=Fin')	

		#wordform rules
		#??? to lc
		if wordform in ['oma'] and pos2 in ['PRON'] and 'sg' in a_morf and 'gen' in a_morf :
			conllu_features.append('Poss=Yes')
		
		#lemma rules
		if lemma in ['ise', 'enda', 'enese', 'ise_enda', 'ise_enese', 'oma_enda', 'oma_enese'] and pos2 in ['PRON', 'DET']:
			conllu_features.append('Reflex=Yes')
		
		#korrastame features array-id - sorteerime ja korjame duplikaadid välja
		conllu_features = fix_connlu_features(conllu_features)

		if len(conllu_features)==0:
			dict_info['analys']['morf'][i] = '_'
		else:
			dict_info['analys']['morf'][i] = ' '.join(sorted(conllu_features, key=str.lower))
		
		
		
		
		
		#relation and function logic
		relations =  (dict_info['analys']['relation'][i].split('->'))
		if (relations[0] == '1'):
			relations[1] = '0'
			dict_info['analys']['function'][i] = 'root'
		else:
			relations[1] = '1'
			dict_info['analys']['function'][i] = 'dep'
		
		dict_info['analys']['relation'][i] = '->'.join(relations)
		

	return dict_info
	
				

##########################
#	commandline arguments
##########################

parser = ArgumentParser(description="description")
parser.add_argument("-i", dest="i_file", required=False,
                    help="Inforem input file name", metavar="InforemFileName")

parser.add_argument("-o", dest="o_file", required=False,
					help="Conllu output file name", metavar="ConlluFileName")

parser.add_argument("-w", dest="wordlistfolder", required=False,
                    help="POS wordlists folder", metavar="WordListsFolder")

parser.add_argument("-d", "--debugmode", required=False,
                    help="debugmode", action='store_true')

parser.add_argument("-m", "--ma", required=False,
                    help="maEnding", action='store_true')

args = parser.parse_args()
		
##########################
#	logic
##########################
			
script_name = (os.path.realpath(__file__))
script_dir = os.path.dirname(script_name)

wordlist_dir = script_dir+'/POS_LEMMA_RULES'

flags = ''

if args.debugmode:
	flags += 'd'

if args.ma:
	flags += 'm'


if args.wordlistfolder:
	wordlist_dir = args.wordlistfolder 

#	lemma - POS rules dict
global POSdict
POSdict = {}

#	parse all pos-wordlists from wordlists folder
read_parse_dict_folder(wordlist_dir)

# input inforem file
global lineNr
lineNr = 0
f_inforem = None
if not args.i_file:
	f_inforem = sys.stdin
else:

	try:
		f_inforem = codecs.open(args.i_file, "r", "utf-8")
	except IOError:
		eprint(bColors.pattern_red % ('Cannot open ' + args.i_file))
		exit()


	
f_out = None


if not args.o_file:
	f_out= sys.stdout
else:
	# open output file
	try:
		f_out = codecs.open(args.o_file, "w", "utf-8")
	
	except IOError:
		eprint(bColors.pattern_red % ('Cannot open ' + args.o_file))
		exit()
	
	
i = 0

arr_sentence = []
in_sentence = False
with f_inforem as fp:
	for line in fp:
		lineNr +=1
		line = line.strip()
		if line == '':
			continue
		elif line == '"<s>"' and in_sentence == False:
			i += 1
			in_sentence =  True
		
		
		elif line == '"</s>"' and in_sentence == True:
			
			in_sentence = False
			sentence = makeDictFromArray(arr_sentence, i)
			arr_sentence = []
			
			
			f_out.write(construct_sentid_conllu(i) + "\n")
			f_out.write(construct_senttext_conllu(sentence) + "\n")
			for line_id in sorted(sentence['lines']):
				if 'd' in flags:
					f_out.write(construct_line_conllu(sentence['lines'][line_id]['info'], line_id) + "\n")
				sentence['lines'][line_id]['info'] = translateToConllu(sentence['lines'][line_id]['info'], flags, i)
				f_out.write(construct_line_conllu(sentence['lines'][line_id]['info'], line_id) + "\n")
			f_out.write("\n")
		
		else:
			arr_sentence.append(line)

f_out.close()

eprint()
eprint('Done.')
if args.o_file:
	eprint('Result saved to %s' % args.o_file)
