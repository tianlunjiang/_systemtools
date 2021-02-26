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
from ..RenameTool.ui import ui_styles
from ..RenameTool import utilities as utl
from qt_material import apply_stylesheet



#-------------------------------------------------------------------------------
#-Test Code
#-------------------------------------------------------------------------------




log.debug("Start testing UI for RenameTool")

app = QtWidgets.QApplication(sys.argv)
# ui_styles.setUIStyle(app)

# Test Widgets
parent = QtWidgets.QWidget()
log.debug("Setup widget as parent")

test_dir = r'D:/Dropbox/REPOSITORIES/_systemtools/RenameTool_pkg/tests/testfiles'
# Test Mod
test_items = [utl.joinPath(test_dir, i) for i in os.listdir(test_dir)]
log.debug("\nlist test items:\n\t%s" % test_items)
Ui_RenameTool = ui.Ui_RenameTool(parent, test_items)
Ui_RenameTool.setupUi("Test UI for RenameTool")
# log.debug("Data model set")
# log.debug("UI set")

test_format = '$show_$shot_$type_$res_$name_v$version'
test_constant = 'show, shot, type, res'
test_dynamic = 'name, version'

box_ctn = Ui_RenameTool.get_box_ctn()

box_ctn.format.setValue(test_format)
box_ctn.constant.setValue(test_constant)
box_ctn.dynamic.setValue(test_dynamic)

# model = Ui_RenameTool.get_listmodel()
# log.debug(model.data(model.index(0,0), QtCore.Qt.ToolTipRole))
# log.debug(model.ls_items[0])

# apply application theme
# apply_stylesheet(app, theme='dark_amber.xml')
# os.environ['QTMATERIAL_SECONDARYTEXTCOLOR'] = '#A6A6A6'
# log.debug("Apply color theme to app")

# Test Run
parent.show()
parent.raise_()

app.exec_()