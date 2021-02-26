'''

testing UI modules

'''




#-------------------------------------------------------------------------------
#-Import Module
#-------------------------------------------------------------------------------




import sys
import os
from Qt import QtWidgets, QtGui, QtCore
from ..RenameTool.kplogger import log, col, add_FileHandler




#-------------------------------------------------------------------------------
#-Import UI Module
#-------------------------------------------------------------------------------




from ..RenameTool.ui import ui_main as ui



#-------------------------------------------------------------------------------
#-Test Code
#-------------------------------------------------------------------------------




log.debug("Start testing UI for RenameTool")

app = QtWidgets.QApplication(sys.argv)

# def test_main():
# 	log.debug("Main Function called")
# def test_cancel():
# 	log.debug("cancel Function called")

# widget = ui.RT_ButtonSet("Test Button")
# widget.connect_main(test_main)
# widget.connect_cancel(test_cancel)
test_format = '$show_$shot_$type_$res_$name_v$version'
test_constant = 'show, shot, type, res'
test_dynamic = 'name, version'

widget = ui.RT_ConventionalBox(test_format, test_constant)
widget.show()
app.exec_(sys.exit())

# _row = 0
# _col = 0
# for i, w in enumerate(test_constant.split(',')):
# 	print(i, i % 4)