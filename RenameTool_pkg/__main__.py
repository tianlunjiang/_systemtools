'''

main executable as a package

'''




#-------------------------------------------------------------------------------
#-Import Modules
#-------------------------------------------------------------------------------




import sys
from .RenameTool import Core_RenameTool
from Qt import QtWidgets, QtGui, QtCore




#-------------------------------------------------------------------------------
#-Run Instance
#-------------------------------------------------------------------------------




print("""
================================================
Copyright (c) 2021 Tianlun Jiang - jiangovfx.com
All Rights Reserved.
================================================
""")


app = QtWidgets.QApplication(sys.argv)
RenameTool = Core_RenameTool()
RenameTool.run()
app.exec_()