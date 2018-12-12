# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileAlreadyExist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
    def run(self, Url):
        self.choice = 1
        self.fileurl = Url
        Dialog = QtGui.QDialog()
        self.dlg = Dialog
        self.setupUi(Dialog)
        Dialog.show()
        if (Dialog.exec_()):
            Dialog.close()
            self.choice = -1
            return self.choice

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(460, 280)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(460, 280))
        Dialog.setMaximumSize(QtCore.QSize(460, 280))
        Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Extras/Icons/alert-box.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 12, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 421, 31))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 441, 121))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.choice_1 = QtGui.QRadioButton(self.groupBox)
        self.choice_1.setGeometry(QtCore.QRect(10, 10, 361, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.choice_1.setFont(font)
        self.choice_1.setChecked(True)
        self.choice_1.setObjectName(_fromUtf8("choice_1"))
        self.choice_2 = QtGui.QRadioButton(self.groupBox)
        self.choice_2.setGeometry(QtCore.QRect(10, 40, 421, 16))
        self.choice_2.setChecked(False)
        self.choice_2.setObjectName(_fromUtf8("choice_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(32, 60, 371, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.choice_3 = QtGui.QRadioButton(self.groupBox)
        self.choice_3.setGeometry(QtCore.QRect(10, 90, 291, 20))
        self.choice_3.setObjectName(_fromUtf8("choice_3"))
        self.lbl_filename = QtGui.QLabel(Dialog)
        self.lbl_filename.setGeometry(QtCore.QRect(90, 10, 351, 51))
        self.lbl_filename.setFrameShape(QtGui.QFrame.Box)
        self.lbl_filename.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbl_filename.setScaledContents(True)
        self.lbl_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_filename.setWordWrap(True)
        self.lbl_filename.setObjectName(_fromUtf8("lbl_filename"))
        self.btn_ok = QtGui.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(240, 240, 93, 28))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(350, 240, 93, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.groupBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lbl_filename.raise_()
        self.btn_ok.raise_()
        self.btn_cancel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.choice_1, self.choice_2)

    def Choice(self):
        if self.choice_1.isChecked():
            self.choice = 1
        elif self.choice_2.isChecked():
            self.choice = 2
        elif self.choice_3.isChecked():
            self.choice = 3

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "File Already Exists!", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">File Url:</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">is already present in the download list. please select an option from below.</span></p></body></html>", None))
        self.choice_1.setText(_translate("Dialog", "Download the file again with numbered name.", None))
        self.choice_2.setText(_translate("Dialog", "If existing download is complete then show the download is complete", None))
        self.label_3.setText(_translate("Dialog", "then show the download complete dialog other wise resume it.", None))
        self.choice_3.setText(_translate("Dialog", "Redownload the file from the beginning.", None))
        self.lbl_filename.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#00007f;\">TextLabel</span></p></body></html>", None))
        self.btn_ok.setText(_translate("Dialog", "OK", None))
        self.btn_cancel.setText(_translate("Dialog", "Cancel", None))

        # Manual Values
        self.lbl_filename.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#00007f;\">"+self.fileurl+"</span></p></body></html>", None))

        #Connections
        self.choice_1.toggled.connect(self.Choice)
        self.choice_2.toggled.connect(self.Choice)
        self.choice_3.toggled.connect(self.Choice)
        self.btn_ok.clicked.connect(self.ok)
        self.btn_cancel.clicked.connect(self.close)

    def ok(self):
        self.dlg.close()

    def close(self):
        self.choice=-1
        self.dlg.close()
