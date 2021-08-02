'''

Description of this module

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import nuke, nukescripts 
import platform
import os




#------------------------------------------------------------------------------
#-Header
#------------------------------------------------------------------------------




__VERSION__		= '1.0'
__OS__			= platform.system()
__AUTHOR__		= "Tianlun Jiang"
__WEBSITE__		= "jiangovfx.com"
__COPYRIGHT__	= "copyright (c) %s - %s" % (__AUTHOR__, __WEBSITE__)

__TITLE__		= "{MODULENAME} v%s" % __VERSION__


def _version_():
	ver='''

	version 1.0
    - Features

	'''
	return ver




#-------------------------------------------------------------------------------
#-Core Class
#-------------------------------------------------------------------------------




pass




#------------------------------------------------------------------------------
#-Run Instance
#------------------------------------------------------------------------------




if __name__ == '__main__':
	print("="*10)
	print("Ran as Main mdule")
	print("="*10)

	app = QtWidgets.QApplication(sys.argv)
	
	# Test Mod
	{MODULENAME} = {MODULENAME}()
	{MODULENAME}.run()
	
	sys.exit(app.exec_())
