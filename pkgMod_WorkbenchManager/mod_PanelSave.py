'''

Main module for PanelSave

'''


#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import sys
import os
import re
from Qt import QtWidgets, QtCore, QtGui
from spt_kputl import *
from spt_GuiFuncs import gui_save

from spt_ui_PanelSave import Ui_PanelSave, __GUI__, __ACTION__



#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




import spt_Globals as glb
import spt_slate as slate




#------------------------------------------------------------------------------
#-Core
#------------------------------------------------------------------------------





class Core_PanelSave(QtWidgets.QWidget):
    def __init__(self):
        super(Core_PanelSave, self).__init__()

        self.ui = Ui_PanelSave()
        self.ui.setupUi(self)
        self.completer_passname = QtWidgets.QCompleter
        self.ui.selType.currentIndexChanged.connect(self.onSaveTypeChanged)
        self.ui.version.currentIndexChanged.connect(self.onVersionChanged)
        self.ui.passname.currentIndexChanged.connect(self.onPassnameChanged)
        self.ui.passname.editTextChanged.connect(self.onPassnameEdited)
        self.ui.IOButton.clicked.connect(self.IOAction)

        self.setDefaults()


    def setDefaults(self):
        '''set default values'''
        _defalutType = 'mastercomp'
        self.ui.selType.setCurrentIndex(self.ui.selType.findText(_defalutType))
        self.set_dirWorkbench()
        self.ui.passname.setEnabled(False)
        self.set_versionList()
        self.set_filename()
        self.ui.version_label.setObjectName('NewVersionStyle')

    def onSaveTypeChanged(self):
        '''when save type changed'''
        w = self.sender()

        if w.currentText() in glb.TYPE_NOPASSNAME[__GUI__]:
            self.ui.passname.setEnabled(False)
            self.ui.passname.clear()
        else:
            self.ui.passname.setEnabled(True)
            self.ui.passname.clear()
            self.set_passnameList()

        self.set_dirWorkbench()
        self.set_passnameList()
        self.set_versionList()
        self.set_filename()

    def onVersionChanged(self):
        '''when version number is changed'''
        c = self.sender()
        _versionList = [int(c.itemText(i)) for i in range(c.count())]
        _curVer = self.ui.get_selVersion()

        if _versionList:
            if _curVer == max(_versionList):
                self.ui.version_label.setText('version <font color="#00cc66">(new)</>')
                reloadCSS(self.ui.filename, "NewVersionStyle")
            else:
                self.ui.version_label.setText('version')
                self.ui.filename.setStyleSheet("")

        self.set_filename()

    def onPassnameChanged(self):
        '''when passname selection is changed'''
        self.set_versionList()
        self.set_filename()

    def onPassnameEdited(self):
        '''when passname is edited'''
        w=self.sender().lineEdit()
        w.setPlaceholderText('NewPassName')
        w.setText(w.text().strip(' '))

        if len(w.text())==0:
            w.setText('NewPassName')

        self.set_filename()

    def set_dirWorkbench(self):
        '''set workbench directory'''

        _selType = self.ui.get_selType()
        _dir = glb.TYPE_CONFIG[__GUI__][_selType]['DIR']
        self.ui.dir_workbench.setText(joinPath(*list(_dir.split('/')[-3:])))
        self.ui.dir_workbench.setToolTip(_dir)

        # print('workbench dir: '+_dir)

    def set_filename(self):
        '''set filename'''

        _filename = '{show}_{shot}_{verType}_v{ver}.{ext}'.format(
            show=       slate.SHOW,
            shot=       slate.SHOT,
            verType=    self.get_type()['type_full'],
            ver=        self.ui.get_selVersionDisplay(),
            ext=        self.ui.get_ext()
        )

        self.ui.filename.setText(_filename)
        # print('filename: '+_filename)

    def set_versionList(self):
        '''set the list of versions'''

        self.ui.version.clear()
        _ls=self.get_versionList()
        self.ui.version.addItems(_ls)

        # print('version list: '+', '.join(_ls))


    def get_versionList(self):
        '''get the list of versions with selected type, passname
        return: [list_of_versions] (list)
        '''
        _selType = self.ui.get_selType()
        _selPassname = self.ui.get_selPassname()
        _fullType = self.get_type()['type_full']
        _padding = glb.PADDING_VER
        _ext = self.ui.get_ext()

        return sorted(ListVers(self.ui.get_dir(), _padding, _ext).get_versions(_fullType), reverse=True)


    def set_passnameList(self):
        '''sets passname list with selected type'''

        _passnames = self.get_type()['pass_list']
        self.ui.passname.clear()
        self.ui.passname.addItems(_passnames)

        # print('passname list: '+', '.join(_passnames))

    def get_type(self):
        '''parse selected type with type and passname
        return {type_sel: just_selected_type (str),
                type_full: parsed_type (str),
                pass_list: [list_of_passnames_of_type_selected] (list)
                } (dict)
        '''
        _selType = self.ui.get_selType()
        _passname = self.ui.get_selPassname()

        _fullType = None
        if _selType in glb.TYPE_NOPASSNAME[__GUI__]:
            _fullType = _selType
        else:
             _fullType = '%s_%s' % (_selType, _passname)
        _fullType.replace('__', '_')

        _padding = glb.PADDING_VER
        _ext = self.ui.get_ext()

        _listPass = ListVers(self.ui.get_dir(), _padding, _ext).get_typePassnames(_selType)

        return {'type_sel': _selType, 'type_full': _fullType, 'pass_list': _listPass}

    def IOAction(self):
        '''when IO button is pressed'''
        _dir = self.ui.get_dir()
        _file = self.ui.get_filename()
        _filename = _dir+_file
        if __name__ == '__main__':
            print(_filename)
        else:
            gui_save(__GUI__, _filename)

    def run(self):
        '''run panel instance'''
        self.setDefaults()
        self.show()
        self.raise_()
        self.ui.selType.setFocus()




#------------------------------------------------------------------------------
#- Run
#------------------------------------------------------------------------------




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    setAppStyle(app)
    PanelSave = Core_PanelSave()
    PanelSave.run()
    app.exec_()
