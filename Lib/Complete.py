# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complete.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt4 import QtCore, QtGui

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
    def __init__(self, url, file):
        self.url = url
        self.folder = os.path.dirname(file)
        self.file = file
        Dialog = QtGui.QDialog()
        Dialog.setParent(None)
        self.dlg = Dialog
        Dialog.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(Dialog)
        Dialog.show()
        if (Dialog.exec_()):
            Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(530, 197)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(530, 197))
        Dialog.setMaximumSize(QtCore.QSize(530, 197))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 181, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Url = QtGui.QLineEdit(Dialog)
        self.Url.setGeometry(QtCore.QRect(20, 60, 491, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Url.sizePolicy().hasHeightForWidth())
        self.Url.setSizePolicy(sizePolicy)
        self.Url.setMinimumSize(QtCore.QSize(0, 22))
        self.Url.setMaximumSize(QtCore.QSize(641, 19))
        self.Url.setAutoFillBackground(False)
        self.Url.setAlignment(QtCore.Qt.AlignCenter)
        self.Url.setReadOnly(True)
        self.Url.setObjectName(_fromUtf8("Url"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.file_url = QtGui.QLineEdit(Dialog)
        self.file_url.setGeometry(QtCore.QRect(20, 110, 491, 22))
        self.file_url.setObjectName(_fromUtf8("file_url"))
        self.file_url.setReadOnly(True)
        self.open = QtGui.QPushButton(Dialog)
        self.open.setGeometry(QtCore.QRect(20, 150, 120, 28))
        self.open.setObjectName(_fromUtf8("open"))
        self.open_folder = QtGui.QPushButton(Dialog)
        self.open_folder.setGeometry(QtCore.QRect(200, 150, 131, 28))
        self.open_folder.setObjectName(_fromUtf8("open_folder"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(390, 150, 120, 28))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Download Complete", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Download Complete</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Address URL:", None))
        self.label_3.setText(_translate("Dialog", "File Saved As:", None))
        self.open.setText(_translate("Dialog", "Open", None))
        self.open_folder.setText(_translate("Dialog", "Open Folder", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))

        # Manual Initializations
        self.file_url.setText(self.file)
        self.Url.setText(self.url)

        # Connections
        self.open.clicked.connect(self.openfile)
        self.open_folder.clicked.connect(self.openfolder)
        self.cancel.clicked.connect(self.dlg.close)


    def openfile(self):
        self.dlg.close()
        os.startfile(self.file)

    def openfolder(self):
        self.dlg.close()
        os.startfile(self.folder)

