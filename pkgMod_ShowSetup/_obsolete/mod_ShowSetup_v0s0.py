'''

set up show structure for kuhq
Setup kupipeline projects with manageable UI

'''




def _version_():
	ver='''

	version 0.0
    - Setup kupipeline projects with manageable UI

	'''
	return ver




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import shutil
import os
import sys
import platform
import collections
import json
from Qt import QtWidgets, QtCore, QtGui

from spt_ui import Ui_ShowSetup




#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




import spt_GlobalVeriable as GV




#------------------------------------------------------------------------------
#-Main class
#------------------------------------------------------------------------------




class Core_ShowSetup(QtWidgets.QWidget):
    def __init__(self):
        super(Core_ShowSetup, self).__init__()

        # Setup Ui
        self.ui = Ui_ShowSetup()
        self.ui.setupUi(self)

        # Setting table widget
        self.table = self.ui.get_TableWidget()

        # Buttons
        self.ui.row_add.clicked.connect(self.edit_row)
        self.ui.row_remove.clicked.connect(self.edit_row)
        self.ui.setup.clicked.connect(self.showSetup)

        self.setDefaults()

    def edit_row(self):
        '''add or remove rows'''
        btn = self.sender()
        if btn.text() == '+':
            self.table.setRowCount(self.table.rowCount()+1)
        elif btn.text() == '-':
            self.table.setRowCount(self.table.rowCount()-1)

    def showSetup(self):
        '''main function when set button is pressed'''

        # Get and filtering data
        _configData = {}
        _configData['showfullname'] = self.ui.get_showfullname()
        _configData['kp_show'] = self.ui.get_kp_show()
        _configData['fps'] = self.ui.get_fps()
        _configData['root_format'] = self.ui.get_format()
        _configData['frameHandle'] = self.ui.get_frameHandle()
        _configData['padding'] = self.ui.get_padding()
        _configData['colorspace'] = self.ui.get_colorspace()
        _configData['kp_shotlist'] = self.get_shotlist()

        _configData['dirTemplate'] = self.ui.get_dirTemplate()
        _configData['dirShowRoot'] = self.ui.get_dirShowRoot()

        _configShow={}
        for show in ['showfullname', 'kp_show', 'fps', 'root_format', 'padding', 'colorspace', 'kp_shotlist']:
            _configShow[show]=_configData[show]

        _configShot={}
        for shot in _configData['kp_shotlist'].keys():
            cur = _configData['kp_shotlist'][shot]
            frameStart = int(cur[0] - _configData['frameHandle'])
            frameEnd = int(cur[1] + _configData['frameHandle'])
            frameHandle = _configData['frameHandle']
            _configShot[shot]={
                'kp_shot': shot,
                'curStart': cur[0],
                'curEnd': cur[1],
                'frameHandle': frameHandle,
                'frameStart': frameStart,
                'frameEnd': frameEnd,
                'frameLen': int(cur[1]-cur[0]+frameHandle*2),
                'framerange': [frameStart, frameEnd]
                }

        # for k in _configData.keys():
        #     print (k,':', _configData[k])
        # for k in _configShow.keys():
        #     print (k,':', _configShow[k])
        # for k in _configShot.keys():
        #     print (k,':', _configShot[k])

        # Create Dirs
        dir_show = self.create_showDir(_configData['dirShowRoot'], _configData['dirTemplate'], _configShow)
        self.create_configShowJSON(dir_show, _configShow)
        dir_shots = self.create_shotDirs(dir_show, _configData['dirTemplate'], _configShot)
        self.create_configShotJSON(dir_shots, _configShot)




    def setDefaults(self):
        '''default value when instancing'''
        self.ui.fps.setValue(24)
        self.ui.format.setText('1920:1080')
        self.ui.colorspace.setText(GV.OCIO_PATH)
        self.ui.handles.setValue(6)
        self.ui.padding.setText('3,4')

        # Testing Values
        # self.ui.showfullname.setText("Testing Project")
        # self.ui.kp_show.setText('tst')

        # _data = self.read_shotlist()
        # if len(_data)>0:
        #     _headers = self.ui.HEADERS
        #     for r_idx, r in enumerate(_data.keys()):
        #         for c_idx, c in enumerate(_headers):
        #             if c_idx == 0:
        #                 self.table.setItem(r_idx, c_idx, QtWidgets.QTableWidgetItem(r))
        #             else:
        #                 self.table.setItem(r_idx, c_idx, QtWidgets.QTableWidgetItem(str(_data[r][c_idx-1])))

    def read_shotlist(self):
        '''get data from _configShow.json file'''
        pass

    def get_shotlist(self):
        '''get shotlist data from ui
        return: {'shot####': [cutStart, cutEnd]}
        '''
        _table = self.table
        _headers = self.ui.HEADERS
        _shotlist = {}

        for r in range(_table.rowCount()):
            curShot = _table.item(r,0).text()
            curCutStart = int(_table.item(r,1).text())
            curCutEnd = int(_table.item(r,2).text())
            _shotlist[curShot]=[curCutStart,curCutEnd]

        return _shotlist

    def create_showDir(self, dir_showRoot, dir_template, configShow):
        '''create show dir
        @dir_showRoot: root dir of the show (str)
        @dir_template: root dir of the show template (str)
        @configShow: variable storing show config data (dict)
        return: show dir full path (str)
        '''
        _tempShowDir = os.path.join(dir_template,'temp_show').replace('\\', '/')
        _showDir = os.path.join(dir_showRoot, configShow['kp_show']).replace('\\', '/')

        try:
            shutil.copytree(_tempShowDir, _showDir)
            print('%s --- created' % _showDir)
        except:
            print('%s --- exists' % _showDir)

        return _showDir

    def create_configShowJSON(self, dir_show, configShow):
        '''create _configShow.json file
        @dir_show: show dir (str)
        @configShow: show config file
        '''
        filename = os.path.join(dir_show,'_configShow.json').replace('\\', '/')
        with open(filename, 'w') as f:
            json_data = json.dumps(configShow, indent=2)
            f.write(json_data)

    def create_shotDirs(self, dir_show, dir_template, configShot):
        '''create shot dir within pre-defined dir_show
        @dir_show: show dir (str)
        @configShot: shot config data (dict)
        return: list of shot dirs (list)
        '''

        _kp_show = os.path.basename(dir_show)+'0000'
        _tempShotDir = os.path.join (dir_template, 'temp_shot').replace('\\', '/')
        _shotDirs = [os.path.join(dir_show, shot).replace('\\', '/') for shot in configShot.keys()]

        # Shot-level dir
        for s in _shotDirs:
            try:
                shutil.copytree(_tempShotDir, s)
                print('%s --- created' % s)
            except:
                print('%s --- exists' % s)

        # Show-level dir
        try:
            shutil.copytree(_tempShotDir, os.path.join(dir_show, _kp_show).replace('\\', '/'))
        except:
            print('%s --- exists' % _kp_show)

        return _shotDirs

    def create_configShotJSON(self, dir_shots, configShot):
        '''create _configShot.json file for each shot dir
        @dir_shots: list of shot dirs (str)
        @configShot: shot config config data (dict)
        '''

        for shot in dir_shots:
            thisShot = os.path.basename(shot)
            thisFilename = os.path.join(shot, '_configShot.json').replace('\\', '/')

            with open(thisFilename, 'w') as f:
                json_data = json.dumps(configShot[thisShot], indent=2)
                f.write(json_data)

    def run(self):
        '''run panel instance'''
        self.show()
        self.raise_()




#------------------------------------------------------------------------------
#- Run
#------------------------------------------------------------------------------




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ShowSetup = Core_ShowSetup()
    ShowSetup.run()
    app.exec_()
else:
    ShowSetup = Core_ShowSetup()
    ShowSetup.run()
