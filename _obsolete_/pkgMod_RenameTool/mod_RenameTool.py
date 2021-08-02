'''
OS system module to rename files with drag and drop features from systems
'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------



import sys, os, platform
from Qt import QtWidgets, QtGui, QtCore
from Qt.QtCore import Qt



#-------------------------------------------------------------------------------
#-General Information
#-------------------------------------------------------------------------------





__VERSION__='1.0'
__OS__=platform.system()
__AUTHOR__="Tianlun Jiang"
__COPYRIGHT__="copyright %s" % __AUTHOR__

__TITLE__=os.path.basename(__file__).split('_')[1].split('.')[0]


def _version_():
	ver='''

	version 1.0
    - Drag and Drop files to view
	- rename files with series of index, parse original name from url
	- if file names are inregular, prompt an input box to enter names with a given string format

	'''
	return ver




#-------------------------------------------------------------------------------
#-Core Class
#-------------------------------------------------------------------------------




class Core_RenameTool(QtWidgets.QWidget):
	def __init__(self):
		super(Core_RenameTool, self).__init__()

		self.list = RT_ListBox()
		
		# Set Layouts
		self.layout_master = QtWidgets.QVBoxLayout()
		self.setLayout(self.layout_master)

		self.layout_master.addWidget(self.list)

		# Set Windows
		self.setWindowTitle(__TITLE__ + ' v%s' % __VERSION__)




#-------------------------------------------------------------------------------
#-Custom Widgets
#-------------------------------------------------------------------------------




class RT_ListBox(QtWidgets.QListWidget):

    def __init__(self, parent=None):
        super(RT_ListBox, self).__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 1200)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(os.path.basename(str(url.toLocalFile())))
                else:
                    links.append(os.path.basename(str(url.toString())))
            self.addItems(links)
        else:
            event.ignore()




#-------------------------------------------------------------------------------
#-Instancing
#-------------------------------------------------------------------------------




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    RenameTool = Core_RenameTool()
    RenameTool.show()

    sys.exit(app.exec_())