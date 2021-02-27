'''

main test file

'''



#-------------------------------------------------------------------------------
#-Import Module
#-------------------------------------------------------------------------------




import unittest




#-------------------------------------------------------------------------------
#-Test Code
#-------------------------------------------------------------------------------




dict_replace = {
	'prefix': '',
	'basename': 'filebase',
	'idf': '_',
	'suffix': 'v',
	'seq': '1001',
	'ext': '.nk'
}

# s = "{prefix}{idf}{basename}{idf}{suffix}{seq}{ext}"
s = "{prefix}{idf}{basename}{idf}{seq}{ext}"
print(s.format(**dict_replace))