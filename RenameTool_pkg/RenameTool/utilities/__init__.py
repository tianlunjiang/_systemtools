'''

utility functions

'''




#-------------------------------------------------------------------------------
#-Module Import
#-------------------------------------------------------------------------------




import os
import re
from ..kplogger import log, col




#-------------------------------------------------------------------------------
#-Functions
#-------------------------------------------------------------------------------




def joinPath(*path):
	try:
		return os.path.join(*path).replace('\\','/')
	except:
		print(path)

def lexer(str_format, token='$'):
	'''parse strings with given token
	source: https://www.techiedelight.com/split-string-with-delimiters-python/
	@str: (str) string to parse
	@token='$': token to seperate tokens
	return: (list of str) list of keywords
	'''

	if token not in str_format:
		return [str_format.strip()]

	ls_cmpt = str_format.split(token)
	ls_out = []
	pattern_letter = re.compile('[^a-zA-Z0-9]')
	# pattern_delimiters = re.compile('[$:/ ._]+')

	log.debug("split cmpt: %s" % ls_cmpt)
	for s in ls_cmpt:
		if s != '':
			s.strip()
			k = re.split('[%s:/ ,._*#@^!()-]+' % token, s)
			# _o = pattern_letter.sub('', s)
			try: k.remove('')
			except: pass
			ls_out.append(k[0])

			log.debug("trim cmpt: %s -> %s" % (s, k[0]))

	log.info("lexer output: " + (str(ls_out) if len(ls_out)>0 else "CLEAR"))

	return ls_out

def parser(str_format, dict_replace, token='$'):
	'''parse and repace str_format with given lexer ouput_out and token replacement
	@str_format: (str) original input string
	@dict_replace: (dict) dict of keywards and replacement text
	@token='$': (str) token used to reconstruct
	return: (str) parser replaced string
	'''

	keywards_parsed = []

	for k, v in dict_replace.items():

		_this_keyword = token+k

		if _this_keyword in str_format and v != '':
			str_format = str_format.replace(_this_keyword, v)
			keywards_parsed.append(k)
			log.debug("parsing %s: " % _this_keyword + str_format)
		else:
			log.debug(col.fg.MAGENTA + "skipped: " + col.RESET + _this_keyword)

	keywards_remain = lexer(str_format)

	log.debug("keywards parsed: %s" % ', '.join(keywards_parsed))
	log.debug("keywards remain: %s" % ', '.join(keywards_remain))
	log.info("parsed output: " + str_format)
	
	return str_format

def listInclude(ls_compare, ls_ref):
	'''check if all of ls_a is included in ls_b
	@ls_a: (list) compare list
	@ls_b: (list) reference list
	return: (bool) True if all of ls_a in ls_b
	'''

	check = False
	ls_illegal = [] # list of items that are not in ls_b

	for i in ls_compare:
		if i in ls_ref:
			check = True
		else:
			check = False
			ls_illegal.append(i)

	allincluded = True if (check and len(ls_illegal)==0) else False
	log.debug("Includes all items" if allincluded else "Different items: %s" % ls_illegal)
	return allincluded

def listConflict(ls_compare, ls_ref):
	'''check if two lists have overlaping items
	@ls_a: (list) compare list
	@ls_b: (list) reference list
	return: (bool) True if ls_a not in ls_b
	'''

	overlap = False
	ls_conflict = [] # list of items that are in ls_b

	if len(ls_compare) < len(ls_ref):
		ls_conflict = [i for i in ls_compare if i in ls_ref]
	else:
		ls_conflict = [i for i in ls_ref if i in ls_compare]

	log.debug(ls_conflict)

	overlap = True if len(ls_conflict) > 0 else False

	log.debug("No conflict between lists" if not overlap else "Conflicted items: %s" % ls_conflict)
	return overlap
		