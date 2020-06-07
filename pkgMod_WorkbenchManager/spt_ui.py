import nuke, nukescripts, sys
from Qt import QtWidgets, QtGui, QtCore





class ui_WorkbenchManager(QtWidgets.QWidget):
    def __init__(self):
        super(ui_WorkbenchManager, self).__init__()


    def setDefault(self):
        '''set default value when instancing'''


    def run(self):
        '''run panel instance'''
        self.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    WorkbenchManager = ui_WorkbenchManager()
    WorkbenchManager.run()
    app.exec_()
else:
    WorkbenchManager = ui_WorkbenchManager()
    WorkbenchManager.run()
