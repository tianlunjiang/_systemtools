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