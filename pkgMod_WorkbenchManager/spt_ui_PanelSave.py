'''

UI elements for WorkbenchSaver

'''


#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import sys, os
from Qt import QtWidgets, QtCore, QtGui
import platform
import datetime



#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




import spt_Globals as glb
import spt_slate as slate
from spt_kputl import joinPath

UNIT=24
__ACTION__='save'
__GUI__=os.getenv('KP_GUI')



#------------------------------------------------------------------------------
#-UI
#------------------------------------------------------------------------------




class Ui_PanelSave(object):
    '''UI elements'''

    def setupUi(self, core):
        '''ui setup'''

        self.core = core

        # Define Widgets
        self.title = QtWidgets.QLabel('<h2>%s</h2>' % glb.__TITLE__[__ACTION__])
        self.subtitle = QtWidgets.QLabel('%s %s panel' % (__GUI__, __ACTION__))
        self.slate = QtWidgets.QLabel()

        self.selType_label = QtWidgets.QLabel("type")
        self.selType = QtWidgets.QComboBox()
        self.passname = QtWidgets.QComboBox()
        self.version_label = QtWidgets.QLabel('version')
        self.version = QtWidgets.QComboBox()
        self.ext = QtWidgets.QComboBox()
        self.settings = QtWidgets.QPushButton('settings')
        self.dir_workbench = QtWidgets.QLabel('/pathto/workbench')
        self.filename = QtWidgets.QLabel('show_scene_selType_v###.nk')
        self.time = QtWidgets.QLabel('2020-05-24 3:53pm')
        self.notes = QtWidgets.QLineEdit()
        self.IOButton = QtWidgets.QPushButton(__ACTION__)

        self.div = QtWidgets.QFrame()
        self.div.setFrameShape(QtWidgets.QFrame.HLine)
        self.div.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        ## Widget Size
        _sizepolicy = QtWidgets.QSizePolicy.Expanding
        self.selType.setSizePolicy(_sizepolicy,_sizepolicy)
        self.selType.setMinimumWidth(UNIT*8)
        self.version.setMinimumHeight(UNIT)
        self.ext.setMinimumHeight(UNIT)
        self.version.setMaximumWidth(UNIT*4)
        self.ext.setMaximumWidth(UNIT*4)
        self.IOButton.setMinimumHeight(UNIT*2)

        ## Widget Settings
        self.passname.addItem('NewPassName')
        self.passname.setEnabled(False)
        self.passname.setEditable(True)
        self.notes.setPlaceholderText('notes to add on save')
        self.settings.setEnabled(False)
        self.slate.setText('show:scene:shot')

        # Layouts
        self.layout_title = QtWidgets.QVBoxLayout()
        self.layout_title.addWidget(self.title)
        self.layout_title.addWidget(self.subtitle)
        self.layout_title.addSpacing(UNIT/2)
        self.layout_title.addWidget(self.slate)

        self.layout_save = QtWidgets.QGridLayout()
        _row=0
        self.layout_save.addWidget(self.selType_label, _row, 0, 1, 2)
        self.layout_save.addWidget(self.version_label, _row, 2, 1, 1)
        _row=1
        self.layout_save.addWidget(self.selType, _row, 0, 2, 2)
        self.layout_save.addWidget(self.version, _row, 2, 1, 1)
        _row=2
        self.layout_save.addWidget(self.ext, _row, 2, 1, 1)
        _row=3
        self.layout_save.addWidget(self.passname, _row, 0, 1, 2)
        self.layout_save.addWidget(self.settings, _row, 2, 1, 1)

        self.layout_display = QtWidgets.QVBoxLayout()
        self.layout_display.addWidget(self.dir_workbench)
        self.layout_display.addWidget(self.filename)
        self.layout_display.addSpacing(UNIT/2)
        self.layout_display.addWidget(self.time)

        self.layout_bottom = QtWidgets.QVBoxLayout()
        self.layout_bottom.addWidget(self.notes)
        self.layout_bottom.addWidget(self.IOButton)

        ## Master Layout
        self.layout_master = QtWidgets.QVBoxLayout()
        self.layout_master.addLayout(self.layout_title)
        self.layout_master.addWidget(self.div)
        self.layout_master.addSpacing(UNIT/2)
        self.layout_master.addLayout(self.layout_save)
        self.layout_master.addSpacing(UNIT/2)
        self.layout_master.addLayout(self.layout_display)
        self.layout_master.addSpacing(UNIT/2)
        self.layout_master.addLayout(self.layout_bottom)

        # Window
        core.setLayout(self.layout_master)
        core.setWindowTitle('Workbench Manager')
        core.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.initilizeUi()

    def initilizeUi(self):
        self.selType.addItems(glb.TYPE_CONFIG[__GUI__].keys())
        self.slate.setText('%s:%s:%s' % (slate.SHOW,slate.SCENE,slate.SHOT))
        _ls_ext = [e['EXT'] for k, e in glb.TYPE_CONFIG[__GUI__].items()]
        _ls_ext = list(dict.fromkeys(_ls_ext))
        self.ext.addItems(_ls_ext)
        self.time.setText(self.get_currentTime())

    def get_currentTime(self):
        '''get current time'''
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

    def get_selType(self):
        '''get the selected version type'''
        return self.selType.currentText()

    def get_selVersion(self):
        '''get the selected version number
        return version number as integer (int)
        '''
        return int(self.version.currentText())

    def get_selVersionDisplay(self):
        '''get the selected version number
        return version number as string with padding (str)
        '''
        return self.version.currentText()

    def get_ext(self):
        '''get file extension'''
        return self.ext.currentText()

    def get_dir(self):
        '''get file extension'''
        return self.dir_workbench.toolTip()

    def get_filename(self):
        '''get the filename'''
        return self.filename.text()

    def get_selPassname(self):
        '''get just the passname'''
        return self.passname.currentText()

    def get_notes(self):
        '''get on save notes'''
        return self.notes.text()





#------------------------------------------------------------------------------
#-Debug Run
#------------------------------------------------------------------------------




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    core=QtWidgets.QWidget()
    Ui_PanelSave = Ui_PanelSave()
    Ui_PanelSave.setupUi(core)
    core.show()
    core.raise_()
    app.exec_()
