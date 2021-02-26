'''

test functions

'''




#-------------------------------------------------------------------------------
#-Import Modules
#-------------------------------------------------------------------------------




from ..RenameTool.kplogger import log, col, add_FileHandler
import re




#-------------------------------------------------------------------------------
#-Test Code
#-------------------------------------------------------------------------------




test_format = '$show_$shot_$type_$res_$name_v$version_002.$ext'
test_constant = 'show, shot, type, res'
test_dynamic = 'name, version'

dict_replace_first = {
	'show': 'tag',
	'shot': 'pit1200',
	'type': 'comp',
	'res': '1080p',
	# 'name': 'mastercomp',
	# 'version': '001',
	'ext': 'nk'
}

def lexer(str_format, token='$'):
	'''parse strings with given token
	source: https://www.techiedelight.com/split-string-with-delimiters-python/
	@str: (str) string to parse
	@token='$': token to seperate tokens
	return: (list of str) list of placeholder text
	'''

	ls_cmpt = str_format.split(token)[1:]
	ls_out = []
	pattern_letter = re.compile('[^a-zA-Z0-9]')
	# pattern_delimiters = re.compile('[$:/ ._]+')

	log.debug("split cmpt: %s" % ls_cmpt)
	for s in ls_cmpt:
		if s != '':
			k = re.split('[%s:/ ._*#@^!()-]+' % token, s)[0]
			# _o = pattern_letter.sub('', s)
			ls_out.append(k)

			log.debug("trim cmpt: %s -> %s" % (s, k))

	log.info("lexer out: " + (str(ls_out) if len(ls_out)>0 else "NONE"))

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

		if _this_keyword in str_format:
			str_format = str_format.replace(_this_keyword, v)
			keywards_parsed.append(k)
			log.debug("parsing %s: " % _this_keyword + str_format)
		else:
			log.debug(col.fg.MAGENTA + "skipped: " + col.RESET + _this_keyword)

	keywards_remain = lexer(str_format)

	log.debug("keywards parsed: %s" % ', '.join(keywards_parsed))
	log.debug("keywards remain: %s" % ', '.join(keywards_remain))
	log.info("output: " + str_format)
	return str_format




#-------------------------------------------------------------------------------
#-Run Test Senarios
#-------------------------------------------------------------------------------




log.info("\n\nParse Patch: First")
str_format = parser(test_format, dict_replace_first)

dict_replace_second = {
	# 'show': 'tag',
	# 'shot': 'pit1200',
	# 'type': 'comp',
	# 'res': '1080p',
	'name': 'mastercomp',
	'version': '001',
	# 'ext': 'nk'
}

log.info("\n\nParse Patch: Second")
parser(str_format, dict_replace_second)
