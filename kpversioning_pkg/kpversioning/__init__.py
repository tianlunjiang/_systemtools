'''

Commandline tool to version modules in kupipeline

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import platform
import os
import sys
import shutil
import re
from . import utilities as utl
from .kplogger import log as LOG
from .kplogger import col




#------------------------------------------------------------------------------
#-Header
#------------------------------------------------------------------------------




__VERSION__='1.0'
__OS__=platform.system()
__AUTHOR__="Tianlun Jiang"
__COPYRIGHT__="copyright %s" % __AUTHOR__

__TITLE__=os.path.basename(__file__).split('_')[0]


def _version_():
	ver='''

	version 1.0
    - Rename move and versioning up modules 

	'''
	return ver




#-------------------------------------------------------------------------------
#-Global Variables
#-------------------------------------------------------------------------------




DIR_OBS = '_obsolete'
RE_VER = re.compile('\d+\.\d+')




#-------------------------------------------------------------------------------
#-Main Functions
#-------------------------------------------------------------------------------




def main(pargs):
	"""main function that takes argparse output as input
	(input pargs.file must be a validat file)
	pargs: (obj) argparse namespace object
	"""

	this_file = pargs.file
	this_ver = get_this_version(this_file)
	this_basename, this_ext = os.path.splitext(os.path.basename(this_file))
	this_dir = os.path.dirname(this_file)
	dir_obs = get_dir_obsolete(this_dir)

	LOG.info("File: %s" % pargs.file)
	LOG.info("Version Detected: %s" % this_ver)

	# Get New Version Number 
	ver_new = None
	if pargs.set:
		LOG.debug("flag: set")
		ver_new = pargs.set 
	elif pargs.increase:
		LOG.debug("flag: increase")
		ver_new = this_ver + float(pargs.increase)
	else:
		while True:
			mode = input('set(s) or increase(i) or exit: ')
			if mode in ['s', 'set']:
				LOG.debug("mode: set")
				ver_new = get_input("Set New Version: ")
				break
			if mode in ['i', 'increase']:
				LOG.debug("mode: increase")
				ver_new = this_ver + get_input("New Version Increases by: ")
				break
			if mode in ['exit']:
				exit()

	LOG.info("New Version: %s" % ver_new)

	# Construct New File Name for Obsolete files
	new_basename = '_'.join(['obs', this_basename.split('_')[1]])
	out_basename = "{}_v{}s{}.py".format(new_basename, *str(this_ver).split('.'))
	out_file = utl.joinPath(dir_obs, out_basename)

	# Copy to dir_obs with new appended version name
	shutil.copy(this_file, out_file)
	LOG.info(col.fg.GREEN + "File Moved and Renamed Successfully!" + col.RESET)

	# Set new version in current file
	set_new_version(this_file, str(ver_new))

	LOG.info("%s (v%s) < %s" % (this_basename, ver_new, out_basename))

	return (this_file, ver_new, out_basename)




#-------------------------------------------------------------------------------
#-Supporting Functions
#-------------------------------------------------------------------------------




def get_this_version(f):
	"""parse input file and return the version number as float
	@f: (str) File path
	return: (float) File number
	"""
	LOG.debug("Input File: %s" % f)
	ver = None

	with open(f, 'r') as v:
		for l in v.readlines():
			if l.startswith("__VERSION__"): 
				LOG.debug(l.replace('\t', '').strip())
				ver=eval(l.split('=')[1].strip())
				break
	LOG.debug("Version: %s, Type: %s" % (ver, type(ver)))
	return float(ver)


def set_new_version(f, ver_new):
	"""sets new version for current file
	@f: (str) file path
	@ver_new: (str)
	"""
	LOG.debug("Setting new version...")

	with open(f, 'r') as o:
		lines = o.readlines()

		LOG.debug("Parsing Lines...")
		for idx, l in enumerate(lines):
			if l.startswith("__VERSION__"): 
				lines[idx] = RE_VER.sub(ver_new, l)
				LOG.debug("Line Edited: %s" % lines[idx])
				break
		LOG.debug("Writing File...")
		with open(f, 'w') as w:
			w.write(''.join(lines))

	LOG.debug(col.fg.GREEN + "New version set")

def get_input(title):
	"""get vailated inputs, loops if not
	@title: (str) title of the prompt
	return: (float) user input value
	"""
	val = None
	while val==None or val=='':
		val = input(title)
		val = None if len(val.split('.'))>2 else val
	
	return round(float(val),1)


def get_dir_obsolete(dir):
	"""get the obsolete dir in file directory
	@dir: (str) file path
	return: (str) obsolete directory path 
	"""

	dir_obs = utl.joinPath(dir, DIR_OBS)
	if not os.path.isdir(dir_obs):
		LOG.info("Make Dir: %s" % DIR_OBS)
		os.makedirs(dir_obs)

	return dir_obs





#-------------------------------------------------------------------------------
#-Supporting Classes
#-------------------------------------------------------------------------------




pass