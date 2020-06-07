from Qt import QtWidgets, QtGui, QtCore

def setTestValues(obj):
    obj.ui.showfullname.setText("Testing Project")
    obj.ui.kp_show.setText('tst')

    _data = obj.read_shotlist()
    if len(_data)>0:
        _headers = obj.ui.HEADERS
        for r_idx, r in enumerate(_data.keys()):
            for c_idx, c in enumerate(_headers):
                if c_idx == 0:
                    obj.table.setItem(r_idx, c_idx, QtWidgets.QTableWidgetItem(r))
                else:
                    obj.table.setItem(r_idx, c_idx, QtWidgets.QTableWidgetItem(str(_data[r][c_idx-1])))

def setTestShotList():
    shotlist = {
        'ism0010': [1001, 1094],
        'ism0020': [1001, 1045],
        'ism0030': [955, 1033]
    }
