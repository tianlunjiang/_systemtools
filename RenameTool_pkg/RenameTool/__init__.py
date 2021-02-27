'''

RenameTool Module

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import platform
import sys
import os
from ..Qt import QtWidgets, QtGui, QtCore
from .ui import ui_main as ui




#------------------------------------------------------------------------------
#-Header
#------------------------------------------------------------------------------




__VERSION__='1.0'
__OS__=platform.system()
__AUTHOR__="Tianlun Jiang"
__COPYRIGHT__="copyright %s" % __AUTHOR__

__TITLE__="RenameTool v%s" % __VERSION__


def _version_():
	ver='''

	version 1.0
    - Drag and Drop Files to rename
	- 3 renaming modes: Sequencial, Subsitutional and Conventional
	- live-update previews that also checks for protential error

	'''
	return ver




#-------------------------------------------------------------------------------
#-Core Class
#-------------------------------------------------------------------------------




class Core_RenameTool(QtWidgets.QWidget):
	def __init__(self):
		super(Core_RenameTool, self).__init__()

		# Add UI elements
		self.ui = ui.Ui_RenameTool(self)
		self.ui.setupUi(__TITLE__)
	
	def run(self):
		self.show()
		self.raise_()






#-------------------------------------------------------------------------------
#-Instancing
#-------------------------------------------------------------------------------




if __name__ == '__main__':
	print("Ran from RenameTool")
	app = QtWidgets.QApplication(sys.argv)
	RenameTool = Core_RenameTool()
	RenameTool.run()
	app.exec_()

