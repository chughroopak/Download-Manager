# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddUrl.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from Lib import DownloadInfo

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self):
        self.url = None
        Dialog = QtGui.QDialog()
        self.setupUi(Dialog)
        Dialog.show()
        if (Dialog.exec_()):
            Dialog.close()

    def setupUi(self, Dialog):
        self.dlg = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(680, 64)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(680, 64))
        Dialog.setMaximumSize(QtCore.QSize(680, 64))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btn_add = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_cancel = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add File Url", None))
        self.label.setText(_translate("Dialog", "File Url:", None))
        self.btn_add.setText(_translate("Dialog", "Add", None))
        self.btn_cancel.setText(_translate("Dialog", "Cancel", None))

        #Connections
        self.btn_add.clicked.connect(self.onclickadd)    # Connects To onclickadd()
        self.btn_cancel.clicked.connect(self.dlg.close)  # Closes the Dialog Box

    def onclickadd(self):
        """Takes File Url"""
        try:
            self.url = self.lineEdit.text()
            self.dlg.close()
        except Exception as e:
            print("Error Generated During Resolving Url",e)
