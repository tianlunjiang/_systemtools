'''

main executable as a package

'''




#-------------------------------------------------------------------------------
#-Module Import
#-------------------------------------------------------------------------------




import os
import argparse
import logging
from .kpversioning.kplogger import log, col, add_FileHandler
from . import kpversioning as kpver




#-------------------------------------------------------------------------------
#-Set up logger
#-------------------------------------------------------------------------------




log_file = logging.getLogger('file_logger')
log_file.setLevel(logging.INFO)
add_FileHandler(log_file, 
				os.path.join(os.path.dirname(__file__), 'kpversioning.log'))




#-------------------------------------------------------------------------------
#-Main
#-------------------------------------------------------------------------------




parser = argparse.ArgumentParser(description="Series of actions to process modules versions")

parser.add_argument('file', metavar='<path/to/file>', help="Module file that needed to be versioned")
parser.add_argument('-s', '--set', metavar='<ver_new>',	help="Set a new version number")
parser.add_argument('-i', '--increase', metavar='<increase_number>', help="Increase Version by the given number")

pargs = parser.parse_args()
log.debug('args' + str([a for a in pargs._get_kwargs() if not a[0].startswith('_')]))
# log.debug('type:' + str(type(pargs)))

if os.path.isfile(pargs.file):
	this_basename, ver_new, out_basename = kpver.main(pargs)
	log.info(col.msg.DONE)
	log_file.info("New Version Created: %s (v%s) < %s" % (this_basename, ver_new, out_basename))
else:
	log.critical("File Does not Exist: %s" % pargs.file)



