'''

main test file

'''




#-------------------------------------------------------------------------------
#-Module Import
#-------------------------------------------------------------------------------




import os
import argparse
import logging
from ..kpversioning.kplogger import log, col
from .. import kpversioning as kpver




#-------------------------------------------------------------------------------
#-Setup
#-------------------------------------------------------------------------------




TEST_DIR = '/kpversioning_pkg/tests/demo/'




#-------------------------------------------------------------------------------
#-Test
#-------------------------------------------------------------------------------




parser = argparse.ArgumentParser(description="Series of actions to process modules versions")

parser.add_argument('file', metavar='<path/to/file>', help="Module file that needed to be versioned")
parser.add_argument('-s', '--set', metavar='<ver_new>',	help="Set a new version number")
parser.add_argument('-i', '--increase', metavar='<increase_number>', help="Increase Version by the given number")

pargs = parser.parse_args()
log.debug('args' + str([a for a in pargs._get_kwargs() if not a[0].startswith('_')]))
# log.debug('type:' + str(type(pargs)))

if os.path.isfile(pargs.file):
	kpver.main(pargs)
	log.info(col.msg.DONE)
else:
	log.critical("File Does not Exist: %s" % pargs.file)