'''

UI elements for {MODULENAME}

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import sys
from Qt import QtWidgets, QtCore, QtGui




#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




FIELD_SIZE=60




#------------------------------------------------------------------------------
#-UI
#------------------------------------------------------------------------------




class ui_{MODULENAME}(object):
	'''UI elements'''

	def setupUI(self,core):
		'''ui setup
		@core: (object) Input object for setting up
		'''

		self.core = core

		# Define Widgets and Properties

		# Define Layouts

		# Assign Widgets to Layouts

		# Window
		self.core.setLayout(self.layout_master)
		# core.setWindowTitle()
		# core.setWindowFlags()

	def run(self):
		'''main run function'''
		
		self.core.show()
		self.core.raise_()




#------------------------------------------------------------------------------
#-Run Instance
#------------------------------------------------------------------------------




if __name__ == '__main__':
	print("="*10)
	print("\nTest UI for {MODULENAME}\n")
	print("="*10)

	app = QtWidgets.QApplication(sys.argv)
	
	# Test Widgets
	core = QtWidgets.QWidget()
	# Test Mod
	ui_{MODULENAME} = ui_{MODULENAME}()
	ui_{MODULENAME}.setupUI(core)
	# Test Run
	core.show()
	
	sys.exit(app.exec_())
