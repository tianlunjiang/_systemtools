'''

main executable as a package

'''




#-------------------------------------------------------------------------------
#-Import Modules
#-------------------------------------------------------------------------------




import sys
from .RenameTool import Core_RenameTool, __TITLE__
from Qt import QtWidgets, QtGui, QtCore




#-------------------------------------------------------------------------------
#-Run Instance
#-------------------------------------------------------------------------------




print("""
================================================
%s
Copyright (c) 2021 Tianlun Jiang - jiangovfx.com
All Rights Reserved.
================================================
""" % __TITLE__)


app = QtWidgets.QApplication(sys.argv)
RenameTool = Core_RenameTool()
RenameTool.run()
app.exec_()