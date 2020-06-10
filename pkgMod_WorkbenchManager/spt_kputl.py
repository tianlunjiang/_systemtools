'''

Function to use package-wise

'''




import os
import re




def joinPath(*paths):
    '''joining path to fix windows and OSX symlink to '/' uniformly'''
    p = os.path.join(*paths).replace('\\', '/')
    return p


class ListVers(object):
    '''gets the list of versions
    @path: path to list (str)
    @PADDING_VER: version padding (str)
    @EXT: file extension (str)
    '''

    def __init__(self, path, PADDING_VER, EXT):
        self.PADDING_VER = PADDING_VER
        self.EXT = EXT
        start_pattern = re.compile('v'+'[0-9]'*int(self.PADDING_VER))
        end_pattern = re.compile('[.'+self.EXT+']$')
        # exclude = re.compile('[~]|autosave')

        ls = os.listdir(path)
        self.ls_versions = []

        for v in ls:
            s=start_pattern.search(v)
            e=end_pattern.search(v)
            if s and e:
                filename = os.path.splitext(s.string)[0]
                ver_display = s.group()
                ver_int = int(ver_display.strip('v'))
                this_type = re.split('_', re.sub(ver_display,'', filename))[2:4]
                self.ls_versions.append((filename, this_type[0],this_type[1], ver_display.strip('v'), ver_int))

        # return self.ls_versions

    def get_fulllist(self):
        '''get the full list
        return: [(filename (str), type (str), passname (str), version_display (str), version_int (int)),...] (list)
        '''
        return self.ls_versions

    def get_passnames(self):
        '''get list of passname'''
        _passnames = []
        for p in self.ls_versions:
            if p[2] !='':
                _passnames.append(p[2])
        _passnames = list(dict.fromkeys(_passnames))
        return _passnames

    def get_types(self):
        '''get list of types'''
        _types = [t[1] for t in self.ls_versions]
        _types = list(dict.fromkeys(_types))
        return _types

    def get_typePassnames(self, selType):
        '''get the passnames of selected type'''

        _typePassnames = []
        for t in self.ls_versions:
            if t[1]==selType:
                _typePassnames.append(t[2])
        _typePassnames = list(dict.fromkeys(_typePassnames))
        return _typePassnames

    def get_versions(self, fullType):
        '''get list of versions with given full type: type_passname
        return: list of display version number
        '''
        _versions = []
        for t in self.ls_versions:
            this_type = (t[1]+'_'+t[2]).strip('_')
            if this_type == fullType:
                _versions.append(t[3])
        _versions = list(dict.fromkeys(_versions))

        if len(_versions)==0:
            _versions=['1'.zfill(int(self.PADDING_VER))]
        else:
            # add new version
            _ver_new = max([int(v) for v in _versions])+1
            _versions.append(str(_ver_new).zfill(int(self.PADDING_VER)))

        return _versions


def reloadCSS(obj, cssName):
    '''reload stylesheet
    @obj: object to reload (obj)
    @cssName: objectname for this obj (str)
    '''

    file_css = joinPath(os.path.dirname(__file__), 'style.stylesheet')
    obj.setObjectName(cssName)
    obj.setStyleSheet(open(file_css).read())


def setAppStyle(obj):
    '''sets the window style'''
    from Qt import QtGui, QtWidgets
    obj.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    p=QtGui.QPalette()
    p = obj.palette()
    p.setColor(QtGui.QPalette.Window, QtGui.QColor(54, 54, 54))
    p.setColor(QtGui.QPalette.WindowText, QtGui.QColor(200, 200, 200))
    p.setColor(QtGui.QPalette.Text, QtGui.QColor(200, 200, 200))
    p.setColor(QtGui.QPalette.Button, QtGui.QColor(54, 54, 54))
    p.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 168, 38))
    p.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(200, 200, 200))
    p.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(130, 130, 130))
    obj.setPalette(p)
