'''

Main UI class for RenameTool

'''




#------------------------------------------------------------------------------
#-Module Import
#------------------------------------------------------------------------------




import sys
import math
import os
from Qt import QtWidgets, QtCore, QtGui
import logging
from ..kplogger import log, col, add_FileHandler
from .. import utilities as utl




#-------------------------------------------------------------------------------
#-Logger
#-------------------------------------------------------------------------------




# log.setLevel(logging.DEBUG)




#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




PREVIEW_WIDTH=400
PREVIEW_HEIGHT=50
BTN_RENAME_HEIGHT=48




#------------------------------------------------------------------------------
#-UI
#------------------------------------------------------------------------------




class Ui_RenameTool(object):
	'''UI elements'''
	def __init__(self, parent, ls_items=[]):
		'''Custom View Object with QStringListModel
		@parent: (obj) parent widget of this ui
		@ls_items: (list) list of items for the model
		'''
		self.parent = parent
		self.ls_items = ls_items

	def setupUi(self, title):
		'''ui setup
		@title: (str) title string for the window
		return: (obj) parent object
		'''

		# Define Widgets and Properties
		## Listview and QStringListModel
		self.parent.listview = RT_ListView()
		## QStringListModel
		# self.parent.listmodel = QtCore.QStringListModel()
		# self.parent.listmodel.setStringList(self.ls_items)
		# self.parent.listview.setModel(self.parent.listmodel)
		# log.info("QStringListModel set")
		# log.debug(self.parent.listmodel.stringList())
		## RT_ListModel
		self.parent.listmodel = RT_ListModel(self.ls_items)
		self.parent.listview.setModel(self.parent.listmodel)
		log.info("ListModel set")
		log.debug("Confirm Items is ListModel:\n\t%s\n" % self.parent.listmodel.get_items())

		self.parent.dirbox = RT_DirBox(self.parent.listview)
		self.parent.dirbox.set_directory()
		clearWidgetMargins(self.parent.dirbox)

		## ModesBox
		self.parent.modesbox = QtWidgets.QTabWidget()
		self.parent.box_seq = RT_SequencialBox(self.parent.listview)
		self.parent.box_sub = RT_SubstitutionalBox(self.parent.listview)
		self.parent.box_ctn = RT_ConventionalBox(self.parent.listview)

		self.parent.modesbox.addTab(self.parent.box_seq, "Sequencial")
		self.parent.modesbox.addTab(self.parent.box_sub, "Substitutional")
		self.parent.modesbox.addTab(self.parent.box_ctn, "Conventional")
		
		# Define Layouts
		self.parent.layout_master = QtWidgets.QVBoxLayout()

		# Assign Widgets to Layouts
		self.parent.layout_master.addWidget(self.parent.dirbox)
		self.parent.layout_master.addWidget(self.parent.listview)
		self.parent.layout_master.addWidget(self.parent.modesbox)

		# Window
		self.parent.setLayout(self.parent.layout_master)
		self.parent.setWindowTitle(title)
		# self.self.parent.setWindowFlags()

		log.info("UI Set")
		return self.parent

	def get_listview(self):
		'''returns the listview object'''
		return self.parent.listview

	def get_listmodel(self):
		'''returns the model object'''
		return self.parent.listmodel

	def get_items(self):
		'''returns list of items in the model'''
		return self.parent.listmodel.stringList()

	def set_root_path(self, path):
		'''sets the root dectory in the field
		@path: (str) path to put in the box
		'''
		self.parent.dirbox.inputfield.setText(path)
		log.debug("set root inputfield to: %s" % path)

	def get_root_path(self):
		'''get the path in the dirbox'''
		return self.parent.dirbox.inputfield.text()

	def get_box_seq(self):
		'''get the Sequencial box object'''
		return self.parent.box_seq
	
	def get_box_sub(self):
		'''get the subsittutional box object'''
		return self.parent.box_sub
	
	def get_box_ctn(self):
		'''get the conventional box object'''
		return self.parent.box_ctn


	def run(self):
		'''main run function'''
		
		self.parent.show()
		self.parent.raise_()





#-------------------------------------------------------------------------------
#-Custom Widgets
#-------------------------------------------------------------------------------



class RT_ListModel(QtCore.QAbstractListModel):
	'''RenameTool Custom List Model'''
	def __init__(self, ls_items=[]):
		'''
		@ls_items: (list of str) list of urls
		'''
		super(RT_ListModel, self).__init__()

		self.ls_items = ls_items

	def rowCount(self, parent):
		return len(self.ls_items)
	
	def columnCount(self, parent):
		return 1

	def data(self, index, role):
		row = index.row()
		item = self.ls_items[row]

		if role == QtCore.Qt.DecorationRole:
			return self.get_os_icon(item)
		
		if role == QtCore.Qt.DisplayRole:
			return os.path.basename(item)

		if role == QtCore.Qt.ToolTipRole:
			return item


	def headerData(self, section, orientation, role):
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				return "%s" % row

	def flag(self, index):
		return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

	def setData(self, index, item, role = QtCore.Qt.EditRole):
		if role == QtCore.QtEditRole:
			row = index.row()
			self.data[row] = item
			self.dataChanged.emit(index, index)
			return True
		return False

	def removeRows(self, row, count, parent = QtCore.QModelIndex()):
		self.beginRemoveRows(parent, row, int(row+count-1))

		for i in range(count):
			item = self.ls_items[row]
			self.ls_items.remove(item)

		self.endRemoveRows()

	def clearList(self):
		'''clear all the rows'''
		log.info("Start Clearing Rows")
		log.debug("Start Clearing Rows")

		self.removeRows(0, len(self.get_items()))
		
		log.info(col.msg.DONE)
		log.debug("Clear Item Check: " + str(self.get_items()))

	def get_items(self):
		'''return current list of items'''
		return self.ls_items

	def get_item_at(self, idx):
		'''returns the item at index'''
		return self.ls_items[idx]

	def get_item_ToolTip(self, idx):
		'''returns the item's tooltip at index'''
		return self.data(self.index(idx,0), QtCore.Qt.ToolTipRole)

	def get_item_Text(self, idx):
		'''returns the item's Display text at index'''
		return self.data(self.index(idx,0), QtCore.Qt.DisplayRole)

	def get_first_item(self):
		'''get the first item of items'''
		return self.data(self.index(0,0), QtCore.Qt.DisplayRole)

	def get_os_icon(self, path):
		'''returns the system icon for this file
		source: https://stackoverflow.com/questions/32795594/how-to-get-an-icon-associated-with-a-certain-file-type-using-pyqt-pyside
		
		'''
		fileinfo = QtCore.QFileInfo(path)
		icon_provider = QtWidgets.QFileIconProvider()

		return icon_provider.icon(fileinfo)




class RT_ListView(QtWidgets.QListView):
	'''custom list view'''
	def __init__(self):
		super(RT_ListView, self).__init__()
		self.setAcceptDrops(True)
		self.setMinimumHeight(200)
		# self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
		self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

	# def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls:
    #         event.accept()
    #     else:
    #         event.ignore()

    # def dragMoveEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()
    #     else:
    #         event.ignore()

    # def dropEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.setDropAction(Qt.CopyAction)
    #         event.accept()

    #         links = []
    #         for url in event.mimeData().urls():
    #             # https://doc.qt.io/qt-5/qurl.html
    #             if url.isLocalFile():
    #                 links.append(os.path.basename(str(url.toLocalFile())))
    #             else:
    #                 links.append(os.path.basename(str(url.toString())))
    #         self.addItems(links)
    #     else:
    #         event.ignore()


class RT_DirBox(QtWidgets.QWidget):
	'''Box for displaying inputfieldectories'''
	def __init__(self, listview):
		'''
		@listview: (obj) listview object
		'''
		self.listview = listview
		self.listmodel = self.listview.model()
		super(RT_DirBox, self).__init__()

		# Create Widgets
		## Title
		self.title = QtWidgets.QLabel('Directory')
		## inputfieldectory LineEdit
		self.inputfield = QtWidgets.QLineEdit()
		self.inputfield.setMinimumWidth(300)
		self.inputfield.setReadOnly(True)
		## Clear Button
		self.btn_clear = QtWidgets.QPushButton('clear')
		self.btn_clear.setMinimumWidth(50)
		self.btn_clear.clicked.connect(self.onPressedClear)

		# Define Layouts
		self.layout_master = QtWidgets.QVBoxLayout()
		clearWidgetMargins(self.layout_master)
		self.layout_box = QtWidgets.QHBoxLayout()
		self.setLayout(self.layout_master)

		# Add Layouts and Widgets
		self.layout_master.addWidget(self.title)
		self.layout_master.addLayout(self.layout_box)
		self.layout_box.addWidget(self.inputfield)
		self.layout_box.addWidget(self.btn_clear)

	def onPressedClear(self):
		'''when clear button is pressed'''
		log.debug("Clear button presssed")
		log.debug(self.listmodel)
		self.listmodel.clearList()
		log.info("Clearing Directory Field")
		# self.listmodel.removeRows()
		self.inputfield.setText('')

		# log.info("Clearing List")

	def set_directory(self):
		try: 
			self.inputfield.setText(os.path.dirname(self.listmodel.get_item_at(0)))
		except:
			log.error("Can't find first item in the list or no model set")

	def __str__(self):
		'''string representation'''
		return "RenameTool DirBox, Directory Field: %s" % self.inputfield.text()


class RT_SequencialBox(QtWidgets.QWidget):
	'''Sequncial Box'''
	def __init__(self, listview):
		'''
		@listview: (obj) listview object
		'''
		self.listview = listview
		self.listmodel = self.listview.model()
		self.PREVIEWOK = False
		super(RT_SequencialBox, self).__init__()

		# Create Widgets
		self.description = QtWidgets.QLabel("Reaneme with a incremental index")
		## Option Boxes
		self.prefix = RT_OptionBox('prefix', 'prefix')
		self.basename = RT_OptionBox('basename', 'filebasename')
		self.identifier = RT_OptionBox('identifier', '_')
		self.suffix = RT_OptionBox('suffix', 'v')
		self.start_idx = RT_OptionBox('start index', '1')
		self.padding = RT_OptionBox('padding', '3')

		self.prefix.setTextEditingFinished(self.onPreviewEdit)
		self.basename.setTextEditingFinished(self.onPreviewEdit)
		self.identifier.setTextEditingFinished(self.onPreviewEdit)
		self.suffix.setTextEditingFinished(self.onPreviewEdit)
		self.start_idx.setTextEditingFinished(self.onPreviewEdit)
		self.padding.setTextEditingFinished(self.onPreviewEdit)
		## Default Widgets
		self.previewbox = RT_PreviewBox()
		self.previewbox.set_preview(self.listmodel.get_first_item())
		self.btn_rename = QtWidgets.QPushButton('RENAME SEQUNCIALLY')
		self.btn_rename.setMinimumHeight(BTN_RENAME_HEIGHT)
		self.btn_rename.clicked.connect(self.onRename)

		# Define Layouts
		self.layout_master = QtWidgets.QVBoxLayout()
		self.setLayout(self.layout_master)
		self.layout_optionbox = QtWidgets.QGridLayout()

		# Add Layouts and Widgets
		self.layout_optionbox.addWidget(self.prefix, 0, 0, 1, 1)
		self.layout_optionbox.addWidget(self.basename, 0, 1, 1, 3)
		self.layout_optionbox.addWidget(self.identifier, 1, 0, 1, 1)
		self.layout_optionbox.addWidget(self.suffix, 1, 1, 1, 1)
		self.layout_optionbox.addWidget(self.start_idx, 1, 2, 1, 1)
		self.layout_optionbox.addWidget(self.padding, 1, 3, 1, 1)
		addModesBoxDefaultWidgets(self, self.previewbox)

	def onRename(self):
		'''when rename button is pressed'''
		log.debug(self.sender().text() + " clicked")

		ls_items = self.listmodel.get_items()

		# [item_name, item_fullpath]
		ls_items_full = []
		for idx in range(len(ls_items)):
			ls_items_full.append([self.listmodel.get_item_Text(idx), self.listmodel.get_item_at(idx)])

		log.debug("list item, item fullpath:\n%s"% ls_items_full)

		if self.PREVIEWOK:
			log.info("Start Renaming Sequencially")
			value_optionbox = self.get_optionbox_values()
			for idx, item in enumerate(ls_items_full):
				# log.debug("file: %s | fullpath: %s" % (item, fullpath))

				# Reconstruct New Item Name
				_item_dir = os.path.dirname(item[1])
				_item_name_new = self.rename_seq(item[0], value_optionbox, idx)
				_item_fullpath_new = utl.joinPath(_item_dir, _item_name_new)

				try:
					log.debug("Fullpath Reconstruct: %s -> %s" % (item[1], _item_fullpath_new))
					
					# OS Rename File

					# Edit Data in listmodel

					log.info("Renamed: %s -> %s" % (item[0], _item_name_new))
				except OSError as err:
					log.error("Fail to rename: %s | %s" % (item[0], err))

			log.info(col.msg.DONE)
		
		else:
			log.error("Fail to Rename, check optionbox")

	def onPreviewEdit(self):
		'''when option box is edited'''
		try:
			if self.sender().text() == '':
				log.error("Please enter a value in optionbox: %s" % self.sender().parent().get_label())
				self.PREVIEWOK = self.previewbox.error()
				log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")
			else: 
				item_renamed = self.rename_seq(
					self.listmodel.get_first_item(), 
					self.get_optionbox_values()
					)
				self.previewbox.set_preview(item_renamed)
				self.PREVIEWOK = True
				log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")
		except Exception as error:
			self.PREVIEWOK = self.previewbox.error()
			log.error("error generating preview, check option box inputs\n%s" % error)
			log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")

	def rename_seq(self, item, value_optionbox, idx=0):
		'''rename per item, meant to use within a loop
		@item: (str) original item name
		@value_optionbox: (dict) values to rename with
		@idx: (int) current index in a loop
		return: (str) renamed item
		'''

		item_basename, item_ext = os.path.splitext(item)
		cur_seq = str(value_optionbox['start index']+idx).zfill(value_optionbox['padding'])

		item_renamed = "{prefix}{idf}{basename}{idf}{suffix}{seq}{ext}".format(
			prefix=value_optionbox['prefix'],
			basename=value_optionbox['basename'],
			idf=value_optionbox['identifier'],
			suffix=value_optionbox['suffix'],
			seq=cur_seq,
			ext=item_ext
		)

		return item_renamed

	def get_optionbox_values(self):
		'''get the values inside the option box
		return: (dict) [label]: value
		'''
		
		_dict = {}
		for p in [self.prefix, self.basename, self.identifier, self.suffix, self.start_idx, self.padding]:
			_dict[p.get_label()] = p.value()

		return _dict

	def __str__(self):
		'''string prepresentation'''
		return "RenameTool Sequncial Box\n%s" % self.get_optionbox_values()


class RT_SubstitutionalBox(QtWidgets.QWidget):
	'''Substitutional Box'''
	def __init__(self, listview):
		'''
		@listview: (obj) listview object
		'''
		self.listview = listview
		self.listmodel = self.listview.model()
		self.PREVIEWOK = False
		super(RT_SubstitutionalBox, self).__init__()

		self.model = self.listview.selectionModel()
		self.model.selectionChanged.connect(self.onSelectionChange)

		# Create Widgets
		self.description = QtWidgets.QLabel("Reaneme with find and replace")
		## Option Box
		self.find = RT_OptionBox('find')
		self.find.setPlaceholderText("characters to find")
		self.find.setTextEditingFinished(self.onPreviewEdit)
		self.replace = RT_OptionBox('replace')
		self.replace.setPlaceholderText("characters to replace")
		self.replace.setTextEdited(self.onPreviewEdit)
		## Default Widgets
		self.previewbox = RT_PreviewBoxDouble()
		self.previewbox.set_orig(self.listmodel.get_first_item())
		self.btn_rename = QtWidgets.QPushButton('FIND AND REPLACE')
		self.btn_rename.setMinimumHeight(BTN_RENAME_HEIGHT)
		self.btn_rename.clicked.connect(self.onRename)
		self.btn_rename.setEnabled(False)

		# Define Layouts
		self.layout_master = QtWidgets.QVBoxLayout()
		self.setLayout(self.layout_master)
		self.layout_optionbox = QtWidgets.QGridLayout()

		# Add Layouts and Widgets
		self.layout_optionbox.addWidget(self.find, 0, 0)
		self.layout_optionbox.addWidget(self.replace, 1, 0)
		addModesBoxDefaultWidgets(self, self.previewbox)

	def onRename(self):
		'''when rename button is pressed'''
		log.debug(self.sender().text() + " clicked")

		ls_items = self.listmodel.get_items()

		# [item_name, item_fullpath]
		ls_items_full = []
		for idx in range(len(ls_items)):
			ls_items_full.append([self.listmodel.get_item_Text(idx), self.listmodel.get_item_at(idx)])

		log.debug("list item, item fullpath:\n%s"% ls_items_full)

		if self.PREVIEWOK:
			log.info("Start Finding and Replacing ")
			value_optionbox = self.get_optionbox_values()
			_num_renamed = 0
			for idx, item in enumerate(ls_items_full):

				# Reconstruct New Item Name
				_item_dir = os.path.dirname(item[1])
				_item_name_new = self.rename_sub(item[0], value_optionbox)
				_item_fullpath_new = utl.joinPath(_item_dir, _item_name_new)

				if _item_name_new == item[0]:
					log.info(col.fg.MAGENTA + "skipped: %s%s" % (col.RESET, item[0]))
				else:
					try:
						# log.debug("Fullpath Reconstruct: %s -> %s" % (item[1], _item_fullpath_new))
						
						# OS Rename File

						# Edit Data in listmodel

						log.info(col.fg.GREEN + "Renamed: %s%s -> %s" % (col.RESET+col.BOLD, item[0], _item_name_new) + col.ENDLN)
						_num_renamed += 1
					except OSError as err:
						log.error("Fail to rename: %s | %s" % (item[0], err))
						continue

			log.info(col.fg.GREEN + "\t\t%s Renamed" % _num_renamed + col.ENDLN)
			log.info(col.msg.DONE)
		
		else:
			log.error("Fail to Rename, check optionbox")

	def onPreviewEdit(self):
		'''when option box is edited'''
		_sender = self.sender()

		# Check if it's optionbox edit change or listview selection change
		if not isinstance(_sender, QtWidgets.QLineEdit):
			log.debug("No an OptionBox")
			self.PREVIEWOK = self.previewbox.reset()
		else:
			try:
				# Check if find text is in preview original item name
				# then, proceed if find text is not empty
				# then, check if input text is in original item name and 
				# When editing Find optionbox
				if _sender.parent() is self.find:
					log.debug("OptionBox: find")
					if _sender.text() == '':
						log.error("Please enter a value in optionbox: %s" % _sender.parent().get_label())
						self.PREVIEWOK = self.previewbox.error()
						log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")
					# Check if input text is in orginal preview
					elif _sender.text() not in self.previewbox.get_previews()[0]:
						self.PREVIEWOK = self.previewbox.error()
						log.error("Can't find %s in file name" % _sender.text())
					else:
						self.PREVIEWOK = True
						log.debug("%s in file name" % _sender.text())
				# Preview will genrated if input text is in orginal preview and not empty
				elif _sender.parent() is self.replace and self.find.value() in self.previewbox.get_previews()[0]:
					log.debug("OptionBox: replace")
					item_renamed = self.rename_sub(
						self.previewbox.get_previews()[0], 
						self.get_optionbox_values()
						)
					self.previewbox.set_preview(item_renamed)
					self.PREVIEWOK = True
					log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")
			except Exception as error:
				self.PREVIEWOK = self.previewbox.error()
				log.error("error generating preview, check option box inputs\n%s" % error)
				log.debug("generated preview: " + "successful" if self.PREVIEWOK else "fail")
		
		if self.PREVIEWOK: self.btn_rename.setEnabled(True)
		else: self.btn_rename.setEnabled(False)

	def rename_sub(self, item, value_optionbox):
		'''rename per item, meant to use within a loop
		@item: (str) original item name
		@value_optionbox: (dict) values to rename with
		@idx: (int) current index in a loop
		return: (str) renamed item
		'''

		item_basename, item_ext = os.path.splitext(item)

		item_renamed = ''.join([
				item_basename.replace(value_optionbox['find'], value_optionbox['replace']),
				item_ext
				])

		return item_renamed

	def get_optionbox_values(self):
		'''get the values inside the option box
		return: (dict) [label]: value
		'''
		
		_dict = {}
		for p in [self.find, self.replace]:
			_dict[p.get_label()] = p.value()

		return _dict

	def onSelectionChange(self):
		'''when selection is changed'''
		cur_item_selected = self.sender().currentIndex().data()
		self.previewbox.set_orig(cur_item_selected)
		# self.PREVIEWOK = self.previewbox.reset()
		self.onPreviewEdit()
		if not self.PREVIEWOK:
			self.previewbox.reset()
		log.debug("selected item: " + col.BOLD + cur_item_selected + col.ENDLN)

	def __str__(self):
		'''string prepresentation'''
		return "RenameTool Substitutional Box \n%s" % self.get_optionbox_values()


class RT_ConventionalBox(QtWidgets.QWidget):
	'''Naming Convention Box'''
	def __init__(self, listview):
		'''
		@listview: (obj) listview object
		'''
		self.listview = listview
		self.listmodel = self.listview.model()
		self.PREVEWOK = False
		super(RT_ConventionalBox, self).__init__()

		# Create Widgets
		self.description = QtWidgets.QLabel("Reaneme with a naming convention with token: <b>$[token]</b> (hover for tooltip)")
		## Option Boxs
		self.format = RT_OptionBox("format (name convention format)")
		self.format.setPlaceholderText("ie. $show_$shot_$type_$res_$name_v$version")
		self.format.setToolTip("ie. $show_$shot_$type_$res_$name_v$version")
		self.constant = RT_OptionBox("constant (define token that are not changed, seperated by ',' )")
		self.constant.setPlaceholderText("ie. show, shot, type, ...")
		self.constant.setToolTip("without '$' ie. show, shot, type, ...")
		self.dynamic = RT_OptionBox("dynamic (define tokens that are changed per item, seperated by ',')")
		self.dynamic.setPlaceholderText(" ie. name, ...")
		self.dynamic.setToolTip("without '$' ie. name, ...")
		## Default Widgets
		self.previewbox = RT_PreviewBoxDouble()
		self.btn_rename = QtWidgets.QPushButton('START ENTERING VARIABLES')
		self.btn_rename.setMinimumHeight(BTN_RENAME_HEIGHT)

		# Define Layouts
		self.layout_master = QtWidgets.QVBoxLayout()
		self.setLayout(self.layout_master)
		self.layout_optionbox = QtWidgets.QGridLayout()

		# Add Layouts and Widgets
		self.layout_optionbox.addWidget(self.format, 0, 0)
		self.layout_optionbox.addWidget(self.constant, 1, 0)
		self.layout_optionbox.addWidget(self.dynamic, 2, 0)
		addModesBoxDefaultWidgets(self, hasPreviewbox=False)

	def set_constants(self):
		'''open Constant Box'''
		ctn_constant = RT_ConstantBox(self.format.text(), self.constant.text())

	def __str__(self):
		'''string prepresentation'''
		return "RenameTool Conventional Box"


class RT_ConstantBox(QtWidgets.QDialog):
	'''Constent Box for Conventional mode'''
	def __init__(self, str_format, str_constant):
		''' parse str_constant and build Optionbox
		@format: (str) name convention format input
		@str_constant: (str) raw string inputs for constants
		'''
		self.str_format = str_format
		self.str_constant = str_constant
		super(RT_ConstantBox, self).__init__()

		self.label = QtWidgets.QLabel("<b>Set Constant Values</b>")
		self.preview = RT_PreviewBox()
		self.buttonset = RT_ButtonSet("SET CONSTANT")
		self.buttonset.connect_main(self.set_dynamic)
		self.buttonset.connect_cancel(self.reject)

		self.layout_master = QtWidgets.QVBoxLayout()
		self.setLayout(self.layout_master)
		self.layout_optionbox = QtWidgets.QGridLayout()

		self.ls_constant = self.str_constant.split(',')
		populateGridWidgets(self.layout_optionbox, self.ls_constant)

		self.layout_master.addWidget(self.label)
		self.layout_master.addLayout(self.layout_optionbox)
		self.layout_master.addStretch(10)
		self.layout_master.addWidget(divider())
		self.layout_master.addWidget(self.preview)
		self.layout_master.addWidget(self.buttonset)

		self.preview.set_preview(self.str_format)

	def set_dynamic(self):
		'''sets the dynamic values'''
		self.ctn_constant = self.get_optionbox_values()

	def get_optionbox_values(self):
		'''get the values inside the option box
		return: (dict) [label]: value
		'''
		if self.sender():
			log.debug("%s pressed" % self.sender().text())

		_dict = {}
		_ls_optionbox = [self.layout_optionbox.itemAt(i).widget() for i in range(self.layout_optionbox.count())]
		for p in _ls_optionbox:
			_dict[p.get_label().strip()] = p.value().strip()
			log.debug("Get Constant box values | %s: %s" % (p.get_label(), p.value())) 
		
		return _dict

	def __str__(self):
		'''string prepresentation'''
		return "RenameTool Constant Box"


class RT_OptionBox(QtWidgets.QWidget):
	'''Inputfield with Label'''
	def __init__(self, label, text=None):
		'''
		@label: (str) label string
		@text: (str) input text field
		'''
		super(RT_OptionBox, self).__init__()

		self.box_label = label
		self.box_text = text

		self.label = QtWidgets.QLabel(self.box_label)
		self.label.setContentsMargins(3,0,0,0)
		self.inputfield = QtWidgets.QLineEdit(self.box_text)
		self.inputfield.setAlignment(QtCore.Qt.AlignCenter)
		# clearWidgetMargins(self.inputfield)
		self.inputfield.setMinimumWidth(100)
		self.inputfield.setMinimumHeight(24)
		self.inputfield.installEventFilter(self)

		self.layout_master = QtWidgets.QVBoxLayout()
		clearWidgetMargins(self.layout_master)
		self.setLayout(self.layout_master)

		self.layout_master.addWidget(self.label)
		self.layout_master.addWidget(self.inputfield)

	def eventFilter(self, obj, event):
		'''emit textEdited Signal when tabbed out and nothing is changed
		source: https://stackoverflow.com/questions/26021808/how-can-i-intercept-when-a-widget-loses-its-focus
		'''
		if (event.type() == QtCore.QEvent.FocusOut 
			and obj is self.inputfield 
			and self.inputfield.text() == ''):
			log.debug("Optionbox focus out")
			self.inputfield.textChanged.emit(self.inputfield.text())
			self.inputfield.textEdited.emit(self.inputfield.text())
			# self.inputfield.editingFinished.emit(self.inputfield.text())
		return super(RT_OptionBox, self).eventFilter(obj, event)

	def value(self):
		'''get the text of the inputfield
		return: (str) or (int) based on label
		'''
		if 'index' in self.label.text() or 'padding' in self.label.text():
			try: 
				return int(self.inputfield.text())
			except ValueError:
				log.error("Can't convert '%s' to an integer" % self.inputfield.text())
		else:
			return self.inputfield.text().strip()

	def setValue(self, text):
		'''sets the value in side the inputfield'''
		self.inputfield.setText(text)

	def get_label(self):
		'''get the label text'''
		return self.label.text()

	def setPlaceholderText(self, text):
		'''sets the placehodler text for inputfield'''
		self.inputfield.setPlaceholderText(text)

	def setTextEditingFinished(self, func):
		'''set the TextEdit signel'''
		self.inputfield.editingFinished.connect(func)

	def setTextEdited(self, func):
		'''set the TextEdit signel'''
		self.inputfield.textEdited.connect(func)

	def setTextChanged(self, func):
		'''set the TextEdit signel'''
		self.inputfield.textChanged.connect(func)


class RT_PreviewBox(QtWidgets.QWidget):
	'''Single Preview box'''
	def __init__(self):
		super(RT_PreviewBox, self).__init__()

		self.main = QtWidgets.QLabel("NO PREVIEW")

		self.groupbox = QtWidgets.QGroupBox('preview')
		self.groupbox.setMinimumWidth(PREVIEW_WIDTH)
		self.groupbox.setMaximumHeight(PREVIEW_HEIGHT)
		self.layout_groupbox = QtWidgets.QVBoxLayout()
		self.layout_groupbox.setAlignment(QtCore.Qt.AlignHCenter)
		self.layout_groupbox.addWidget(self.main)
		self.groupbox.setLayout(self.layout_groupbox)

		self.layout_master = QtWidgets.QVBoxLayout()
		clearWidgetMargins(self.layout_master)
		self.setLayout(self.layout_master)
		self.layout_master.addWidget(self.groupbox)

	def set_preview(self, text):
		'''set preview text'''
		self.main.setText(text)

	def get_preview(self):
		return self.main.text()

	def error(self):
		'''set text when there is error generate preview'''
		self.main.setTest("""<b style="color:red;">FAIL TO GENERATE PREVIEW</b>""")
		return False

	def reset(self):
		'''set text when list viewselection is changed'''
		self.main.setTest("""<b style="color:blue;">PREVIEW RESET</b>""")
		return False


class RT_PreviewBoxDouble(QtWidgets.QWidget):
	'''Double Preview box'''
	def __init__(self):
		super(RT_PreviewBoxDouble, self).__init__()

		self.orig = QtWidgets.QLabel("NO PREVIEW")
		self.preview = QtWidgets.QLabel("NO PREVIEW")

		# Original Groupbox
		self.groupbox_orig = QtWidgets.QGroupBox('original')
		self.groupbox_orig.setMinimumWidth(PREVIEW_WIDTH)
		self.groupbox_orig.setMaximumHeight(PREVIEW_HEIGHT)
		self.layout_groupbox_orig = QtWidgets.QVBoxLayout()
		self.layout_groupbox_orig.setAlignment(QtCore.Qt.AlignHCenter)
		self.layout_groupbox_orig.addWidget(self.orig)
		self.groupbox_orig.setLayout(self.layout_groupbox_orig)
		# Preview Groupbox
		self.groupbox_preview = QtWidgets.QGroupBox('preview')
		self.groupbox_preview.setMinimumWidth(PREVIEW_WIDTH)
		self.groupbox_preview.setMaximumHeight(PREVIEW_HEIGHT)
		self.layout_groupbox_preview = QtWidgets.QVBoxLayout()
		self.layout_groupbox_preview.setAlignment(QtCore.Qt.AlignHCenter)
		self.layout_groupbox_preview.addWidget(self.preview)
		self.groupbox_preview.setLayout(self.layout_groupbox_preview)

		self.layout_master = QtWidgets.QVBoxLayout()
		clearWidgetMargins(self.layout_master)
		self.setLayout(self.layout_master)
		self.layout_master.addWidget(self.groupbox_orig)
		self.layout_master.addWidget(self.groupbox_preview)
		
	def set_orig(self, text):
		'''set preview text'''
		self.orig.setText(text)
	
	def set_preview(self, text):
		'''set preview text'''
		self.preview.setText(text)

	def error(self):
		'''set text when there is error generate preview'''
		self.preview.setText("""<b style="color:red;">FAIL TO GENERATE PREVIEW</b>""")

	def reset(self):
		'''set text when list viewselection is changed'''
		self.preview.setText("NO PREVIEW")
		return False

	def get_previews(self):
		'''get the original and new previews
		return: (original, preview)
		'''
		return (self.orig.text(), self.preview.text())


class RT_ButtonSet(QtWidgets.QWidget):
	'''Button group set for Conventional Mode, includes a main and a cancel button'''
	def __init__(self, btn_main='MAIN'):
		'''
		@btn_main: (str) the main button text
		'''
		super(RT_ButtonSet, self).__init__()
		self.MAIN_TEXT = btn_main
		self.main = QtWidgets.QPushButton(self.MAIN_TEXT)
		self.main.setMinimumWidth(200)
		self.main.setMinimumHeight(BTN_RENAME_HEIGHT)
		self.cancel = QtWidgets.QPushButton('CANCEL')
		self.cancel.setMaximumWidth(100)
		self.cancel.setMinimumHeight(BTN_RENAME_HEIGHT)
		self.layout_master = QtWidgets.QHBoxLayout()
		clearWidgetMargins(self.layout_master)
		self.setLayout(self.layout_master)
		self.layout_master.addWidget(self.main)
		self.layout_master.addWidget(self.cancel)

	def connect_main(self, func):
		'''set signal to connect main button
		@func: (function) function for main button
		'''
		try: self.main.clicked.connect(func)
		except: log.error("Fail to connect main button to %s" % func)

	def connect_cancel(self, func):
		'''set signal to connect main button
		@func: (function) function for cancel button
		'''
		try: self.cancel.clicked.connect(func)
		except: log.error("Fail to connect cancel button to %s" % func)

	def get_button_main(self):
		'''return main button object'''
		return self.main
		
	def get_button_cancel(self):
		'''return cancel button object'''
		return self.cancel




class divider(QtWidgets.QFrame):
	def __init__(self):
		super(divider, self).__init__()
		self.setFrameShape(QtWidgets.QFrame.HLine)
		self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)



#-------------------------------------------------------------------------------
#-Supporting Functions
#-------------------------------------------------------------------------------




def clearWidgetMargins(obj):
	'''clear QWidget Margins'''
	try: obj.setContentsMargins(0,0,0,0)
	except: logging.error("%s is not a QWidget")

def addModesBoxDefaultWidgets(obj, preview_obj=None, hasPreviewbox=True):
	'''add default widgets for ModesBox'''

	obj.layout_master.addWidget(obj.description)
	obj.layout_master.addLayout(obj.layout_optionbox)
	obj.layout_master.addStretch(10)
	if hasPreviewbox and preview_obj != None: 
		obj.layout_master.addWidget(preview_obj)
	obj.layout_master.addWidget(divider())
	obj.layout_master.addWidget(obj.btn_rename)

def populateGridWidgets(layout, ls_widgetname, num_column=3):
	'''populating widgets in a grid layout
	@layout: (obj) layout object
	@ls_widgetname: (list of str) list of widget names
	@num_column=3: (int) max number of columns
	'''

	if isinstance(layout, QtWidgets.QGridLayout):
		num_row = math.ceil(len(ls_widgetname)/num_column)

		_row = 0
		_col = 0
		for i,w in enumerate(ls_widgetname):
			w=w.strip()
			if i % num_column == 0: 
				_row += 1

			log.debug("widget: %s; \tindex: %s; row: %s; col: %s" % (w, i, _row, i % num_column))
			exec("""ctn_optionbox_{0} = RT_OptionBox('{0}')""".format(w))
			layout.addWidget(eval("ctn_optionbox_{}".format(w)), _row, i % num_column)
	else:
		log.error("%s not a Grid Layout object")









