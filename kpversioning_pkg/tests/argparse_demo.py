'''

Argparse demo to testing out arguements

'''




#-------------------------------------------------------------------------------
#-Module Import
#-------------------------------------------------------------------------------




import argparse
import logging
from ..kpversioning.kplogger import log




#-------------------------------------------------------------------------------
#-Demo
#-------------------------------------------------------------------------------




parser = argparse.ArgumentParser(description="Series of actions to process modules versions")

parser.add_argument('file', metavar='<path/to/file>',  help="Module file that needed to be versioned")
parser.add_argument('ver_new', metavar='<ver_new>',	help="New Version number")
parser.add_argument('-i', '--increase', metavar='<increase_number>', help="Increase Version by the given number")


args = parser.parse_args()
log.debug(args.file)
log.debug(args.ver_new)
log.debug(args.increase)