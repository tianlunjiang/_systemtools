'''

Python script to setup python project
built to run in command-line

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import platform
import os
import sys
import shutil
import logging
from kplogger import log, col, add_FileHandler




#------------------------------------------------------------------------------
#-Header
#------------------------------------------------------------------------------




__VERSION__='1.0'
__OS__=platform.system()
__AUTHOR__="Tianlun Jiang"
__COPYRIGHT__="copyright %s" % __AUTHOR__

__TITLE__=__name__


def _version_():
	ver='''

	version 1.0
	- Copy and Rename template

	'''
	return ver




#-------------------------------------------------------------------------------
#-Set up logger
#-------------------------------------------------------------------------------




log_file = logging.getLogger('file_logger')
log_file.setLevel(logging.INFO)
add_FileHandler(log_file, 
				os.path.join(os.path.dirname(__file__), 'ProjectSetup.log'))




#-------------------------------------------------------------------------------
#-Global Variables
#-------------------------------------------------------------------------------



DIR_TEMPLATE = "D:/Dropbox/REPOSITORIES/_kptools/_templates/template_PyProject_pkg"
DIR_REPLACE = 'PyProject'




#-------------------------------------------------------------------------------
#-Main Functions
#-------------------------------------------------------------------------------




def main(dir_cwd, name_project):
	'''main function
	@dir_cwd: (str) current directory
	@name_project: (str) name of the project
	'''

	dir_new_proj = joinPath(dir_cwd, name_project+'_pkg')
	log.info(">>> New project Path: \n    %s" % dir_new_proj)

	try:

		log.info(">>> Creating new directory from template")

		shutil.copytree(DIR_TEMPLATE, dir_new_proj)

		log.info(col.msg.DONE)

	except:

		log.error(col.ERROR + "Directory already exist, exit" + col.ENDLN)

		exit()

	project_tmp = joinPath(dir_new_proj, DIR_REPLACE)
	project_mod = joinPath(dir_new_proj, name_project)
	file_readme = joinPath(dir_new_proj, 'README.md')

	log.debug("Temp Package: %s" % project_tmp)
	log.debug("New Package: %s" % project_mod)
	log.debug("README file: %s" % file_readme)

	log.info(">>> Start renaming main module")

	if os.path.isdir(project_tmp):
		os.rename(project_tmp, project_mod)

		log.info(col.msg.DONE)
		
	else:
		log.error(col.ERROR + "Main Module name replace error, exit" + col.ENDLN)
		exit()

	editREADME(file_readme, name_project)
	printDirTree(dir_new_proj)
	
	log.info('\n\n' + '='*20 + "\n%s is setup!" % name_project)

	return dir_new_proj




#-------------------------------------------------------------------------------
#-Support Function
#-------------------------------------------------------------------------------




def joinPath(*args):
	try:
		return os.path.join(*args).replace('\\', '/')
	except: pass


def printDirTree(dir):
	print ('\n'+'='*20 +'\nListing Project Directries\n')
	
	for root, dirs, files in os.walk(dir):
		level = root.replace(dir, '').count(os.sep)
		indent = ' ' * 4 * (level)
		print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			print('{}{}{}{}'.format(subindent,col.DISABLE, f, col.ENDLN))


def editREADME(file, name_project):
	'''source: https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python#:~:text=Use%20file.,at%20a%20certain%20line%20number.'''
	
	print('-'*20)
	des = input('\n' + col.bg.CYAN + " Add oneline description of {}: \n".format(name_project) + col.ENDLN)
	print('-'*20)

	if des and name_project:

		log.info("Edit project name and oneline description")

		with open(file, 'r') as r:
			lines = r.read()
			lines = lines.format(name_project=name_project, description=des)
			with open(file, 'w') as w:
				w.write(lines)

		log.info(col.msg.DONE)

	else:
		log.error("Error editing README.md")




#-------------------------------------------------------------------------------
#-Execution
#-------------------------------------------------------------------------------




if __name__ == '__main__':

	dir_cwd = os.getcwd().replace('\\', '/')
	log.debug("current directory: %s" % dir_cwd)

	if len(sys.argv) >= 2:
		if len(sys.argv) > 2:
			log.error("Command-line only takes 1 input, take 1st one instead")
		name_project = sys.argv[1]
		main(dir_cwd, name_project)
		
		log_file.info("%s created! (%s)" % (name_project, joinPath(dir_cwd,name_project)))
		
	elif len(sys.argv) < 2:
		log.critical("Command-line needs an name input")
		