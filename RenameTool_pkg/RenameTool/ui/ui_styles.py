from Qt import QtWidgets, QtGui, QtCore



def setUIStyle(app):
	app.setStyle("fusion")

	dark_palette = QtGui.QPalette()

	dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
	dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
	dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
	dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
	dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
	dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
	dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
	dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
	dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
	dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
	dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
	dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
	dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
