'''

UI elements for ShowSetup

'''


#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import sys
from Qt import QtWidgets, QtCore, QtGui
import platform





#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------



import spt_GlobalVeriable as GV
FIELD_SIZE=60
DEFAULT_ROW_NUMBER = 3
COL_SIZE = 170




#------------------------------------------------------------------------------
#-UI
#------------------------------------------------------------------------------




class Ui_ShowSetup(object):
    '''UI elements'''
    HEADERS = ['shot', "cut start", "cut end"]

    def setupUi(self,core):
        '''ui setup'''
        self.showfullname_label = QtWidgets.QLabel("show full name")
        self.showfullname = QtWidgets.QLineEdit()
        self.showfullname.setToolTip("full name of the show")
        self.kp_show_label = QtWidgets.QLabel("codename")
        self.kp_show = QtWidgets.QLineEdit()
        self.kp_show.setMaximumWidth(FIELD_SIZE)
        self.kp_show.setInputMask('<aaa')
        self.kp_show.setToolTip("3 letter codename")
        self.kp_show.setMaxLength(3)
        self.fps_label = QtWidgets.QLabel("fps")
        self.fps = QtWidgets.QSpinBox()
        self.fps.setMaximumWidth(FIELD_SIZE)
        self.fps.setToolTip("show fps, default 24")
        self.format_label = QtWidgets.QLabel("format")
        self.format = QtWidgets.QLineEdit()
        self.format.setPlaceholderText('####:####')
        self.format.setInputMask('####:####')
        self.format.setMaximumWidth(FIELD_SIZE*2.5)
        self.format.setToolTip("show format:\n1920:1080 (HD)\n2048:1080 (DCI 2K)\n4096:2160 (4K)")
        self.handles_label = QtWidgets.QLabel("handles")
        self.handles = QtWidgets.QSpinBox()
        self.handles.setMaximumWidth(FIELD_SIZE)
        self.handles.setToolTip("frame handles, default 6")
        self.padding_label = QtWidgets.QLabel("padding")
        self.padding = QtWidgets.QLineEdit()
        self.padding.setInputMask('#,#')
        self.padding.setMaximumWidth(FIELD_SIZE)
        self.padding.setToolTip("number paddings\n[version, render]\ndefault: [3,4]")
        self.colorspace_label = QtWidgets.QLabel("OCIO path")
        self.colorspace = QtWidgets.QLineEdit()
        self.colorspace.setPlaceholderText('/your/ocio/config/file/path/with/config.ocio')
        self.colorspace.setToolTip("OCIO config file full path")
        self.shotlist_label = QtWidgets.QLabel("shotlist")

        ## Shotlist Widget
        self.shotlist = QtWidgets.QTableWidget()
        self.row_add = QtWidgets.QPushButton('+')
        # self.row_add.setMaximumWidth(40)
        self.row_add.setToolTip("add a shot")
        self.row_remove = QtWidgets.QPushButton('-')
        self.row_remove.setToolTip("remove a shot")
        # self.row_remove.setMaximumWidth(40)
        self.shotlist.setRowCount(DEFAULT_ROW_NUMBER)
        self.shotlist.setColumnCount(len(self.HEADERS))
        self.shotlist.setHorizontalHeaderLabels(self.HEADERS)
        self.shotlist.setMinimumWidth(350)
        self.shotlist.verticalScrollBar().setStyleSheet("QScrollBar:vertical {width: 12px;}")
        self.shotlist.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal {height: 12px;}")
        self.shotlist.setColumnWidth(1, COL_SIZE/2)
        self.shotlist.setColumnWidth(2, COL_SIZE/2)
        self.shotlist.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.dir_template = QtWidgets.QPushButton(GV.__DIR_TEMPLATE__)
        self.dir_template.setStyleSheet("Text-align:left")
        self.dir_template.setFlat(True)
        self.dir_template.setToolTip("Click to edit")
        self.dir_showRoot = QtWidgets.QPushButton(GV.__DIR_SHOW_ROOT__)
        self.dir_showRoot.setStyleSheet("Text-align:left")
        self.dir_showRoot.setFlat(True)
        self.dir_showRoot.setToolTip("Click to edit")
        self.previz = QtWidgets.QPushButton ('set previz')
        self.previz.setMinimumHeight(30)
        self.setup = QtWidgets.QPushButton('SET')
        self.setup.setMinimumHeight(60)


        # Layouts
        self.layout_top = QtWidgets.QGridLayout()
        ## Row 0 label
        self.layout_top.addWidget(self.showfullname_label, 0,0,1,3)
        self.layout_top.addWidget(self.kp_show_label, 0,3,1,1)
        ## Row 1
        self.layout_top.addWidget(self.showfullname, 1,0,1,3)
        self.layout_top.addWidget(self.kp_show, 1,3,1,1)
        ## Row 2 label
        self.layout_top.addWidget(self.format_label, 2,0,1,1)
        self.layout_top.addWidget(self.fps_label, 2,1,1,1)
        self.layout_top.addWidget(self.handles_label, 2,2,1,1)
        self.layout_top.addWidget(self.padding_label, 2,3,1,1)
        ## Row 3
        self.layout_top.addWidget(self.format, 3,0,1,1)
        self.layout_top.addWidget(self.fps, 3,1,1,1)
        self.layout_top.addWidget(self.handles, 3,2,1,1)
        self.layout_top.addWidget(self.padding, 3,3,1,1)
        ## Row 4,6
        self.layout_top.addWidget(self.colorspace_label, 4,0, 1,4)
        self.layout_top.addWidget(self.colorspace, 5,0, 1,4)

        self.layout_tableButtons = QtWidgets.QHBoxLayout()
        self.layout_tableButtons.addWidget(self.row_add)
        self.layout_tableButtons.addWidget(self.row_remove)

        self.layout_mid = QtWidgets.QVBoxLayout()
        self.layout_mid.addWidget(self.shotlist_label)
        self.layout_mid.addWidget(self.shotlist)

        self.layout_end = QtWidgets.QVBoxLayout()
        self.layout_end.addWidget(self.dir_template)
        self.layout_end.addWidget(self.dir_showRoot)
        self.layout_end.addWidget(self.previz)
        self.layout_end.addWidget(self.setup)

        # Set layouts
        separador = QtWidgets.QFrame()
        separador.setFrameShape(QtWidgets.QFrame.HLine)
        separador.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.layout_master = QtWidgets.QVBoxLayout()
        self.layout_master.addLayout(self.layout_top)
        self.layout_master.addLayout(self.layout_mid)
        self.layout_master.addLayout(self.layout_tableButtons)
        self.layout_master.addWidget(separador)
        self.layout_master.addLayout(self.layout_end)
        # self.layout_master.addWidget(QtWidgets.QLabel(GV.__COPYRIGHT__))
        core.setLayout(self.layout_master)

        # Window
        core.setWindowTitle(GV.__TITLE__+' v'+GV.__VERSION__)
        core.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

    def get_TableWidget(self):
        '''get the table widget'''
        return self.shotlist

    def get_showfullname(self):
        '''get showfullname'''
        return self.showfullname.text()

    def get_kp_show(self):
        '''get kp_show'''
        return self.kp_show.text()

    def get_fps(self):
        '''get fps'''
        return self.fps.value()

    def get_format(self):
        '''get format'''
        return self.format.text().split(':')

    def get_frameHandle(self):
        '''get format'''
        return self.handles.value()

    def get_padding(self):
        '''get padding'''
        return self.padding.text().split(',')

    def get_colorspace(self):
        '''get colorspace'''
        return self.colorspace.text()

    def get_dirTemplate(self):
        '''get template directory'''
        return self.dir_template.text()

    def get_dirShowRoot(self):
        '''get show directory'''
        return self.dir_showRoot.text()




#------------------------------------------------------------------------------
#-show
#------------------------------------------------------------------------------




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    core=QtWidgets.QWidget()
    Ui_ShowSetup = Ui_ShowSetup()
    Ui_ShowSetup.setupUi(core)
    core.show()
    core.raise_()
    app.exec_()
