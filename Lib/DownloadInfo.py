# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadInfo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import cgi, shutil
import os, csv
import urllib.request
from time import strftime
import pickle, requests
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
    def run(self,url, choice=0, count=0, dialog=True):
        self.complete=0
        self.url = url
        self.dialog = dialog
        self.downloadtuple = None
        if choice == 1:
            self.getvalues()
            temp_name = self.file_name.split('.')
            temp_name[-2] = temp_name[-2] + '_' + str(count)
            self.ext = temp_name[-1]
            temp_name[-1] = '.'+ temp_name[-1]
            self.file_name = ''.join(temp_name)
        elif choice == 2:
            self.getvalues()
            self.dialog = False
        elif choice == 3:
            self.getvalues()
            self.complete=0
            shutil.rmtree(self.tmpdirname)
            file_path = os.path.join(self.download_location, self.file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
            self.dialog = False
            self.getvalues()
            self.downloadnow()
        else:
            self.getvalues()
        if self.dialog is True:
            self.showdialog()
        return self.complete

    # Draws the download options dialog on the screen
    def showdialog(self):
        Dialog = QtGui.QDialog()
        self.dlg = Dialog
        self.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            Dialog.close()

    # System Generated
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(575, 252)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(575, 207))
        Dialog.setMaximumSize(QtCore.QSize(2000, 2000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lbl_filename = QtGui.QLineEdit(Dialog)
        self.lbl_filename.setGeometry(QtCore.QRect(200, 30, 311, 22))
        self.lbl_filename.setObjectName(_fromUtf8("lbl_filename"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_Destination = QtGui.QLineEdit(Dialog)
        self.lbl_Destination.setGeometry(QtCore.QRect(200, 70, 281, 22))
        self.lbl_Destination.setObjectName(_fromUtf8("lbl_Destination"))
        self.btn_dnow = QtGui.QPushButton(Dialog)
        self.btn_dnow.setGeometry(QtCore.QRect(70, 200, 130, 28))
        self.btn_dnow.setObjectName(_fromUtf8("btn_dnow"))
        self.btn_cancel = QtGui.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(380, 200, 130, 28))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 55, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btn_Destination = QtGui.QToolButton(Dialog)
        self.btn_Destination.setGeometry(QtCore.QRect(480, 69, 31, 24))
        self.btn_Destination.setObjectName(_fromUtf8("btn_Destination"))
        self.lbl_size = QtGui.QLabel(Dialog)
        self.lbl_size.setGeometry(QtCore.QRect(200, 110, 55, 21))
        self.lbl_size.setObjectName(_fromUtf8("lbl_size"))
        self.btn_dlater = QtGui.QPushButton(Dialog)
        self.btn_dlater.setGeometry(QtCore.QRect(220, 200, 141, 28))
        self.btn_dlater.setObjectName(_fromUtf8("btn_dlater"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lbl_type = QtGui.QLabel(Dialog)
        self.lbl_type.setGeometry(QtCore.QRect(200, 150, 100, 21))
        self.lbl_type.setObjectName(_fromUtf8("lbl_type"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Download File", None))
        self.label.setText(_translate("Dialog", "File Name:", None))
        self.label_2.setText(_translate("Dialog", "Destination:", None))
        self.btn_dnow.setText(_translate("Dialog", "Download Now", None))
        self.btn_cancel.setText(_translate("Dialog", "Cancel", None))
        self.label_3.setText(_translate("Dialog", "File Size:", None))
        self.btn_Destination.setText(_translate("Dialog", "...", None))
        self.lbl_size.setText(_translate("Dialog", "Size", None))
        self.btn_dlater.setText(_translate("Dialog", "Download Later", None))
        self.label_5.setText(_translate("Dialog", "File Type:", None))
        self.lbl_type.setText(_translate("Dialog", "Type", None))

        # Setting Different Parameters To Different Fields
        self.lbl_filename.setText(self.file_name)
        self.lbl_size.setText(self.evaluatesize(self.file_size))
        self.lbl_Destination.setText(self.download_location)
        self.lbl_type.setText(self.file_type)

        # Connections
        self.btn_dnow.clicked.connect(self.downloadnow)
        self.btn_Destination.clicked.connect(self.open_dir)


    def getvalues(self):
        try:
        # Gets url and parses it to give file information
            self.urlinfo = requests.head(self.url, headers={'User-Agent': "Magic Browser"},timeout=15,allow_redirects = True)
            #self.urlinfo = urllib.request.urlopen(req, timeout=4)
            self.file_name = self.getfilename().decode()
            self.file_type = self.urlinfo.headers["Content-Type"]
            self.file_size = int(self.urlinfo.headers["Content-Length"]) if 'Content-Length' in self.urlinfo.headers else -1
            self.type_switch = self.file_type.split('/')[0]
            self.tmpdirname = os.path.join(os.path.expanduser(r"~\AppData\Roaming\MyDownloadManager"),
                                           "".join(x for x in urllib.request.urlsplit(self.url)[1] if
                                                   x.isalnum() or x == '.'))
            if os.path.exists(self.tmpdirname):
                if not os.path.exists(os.path.join(self.tmpdirname, self.file_name+'.temp0')):
                    self.complete = 1
                with open(os.path.join(self.tmpdirname, 'log.dat'), 'rb') as pickle_file:
                    self.downloadtuple = pickle.load(pickle_file)
                    self.download_location = self.downloadtuple[3]
            else:
                self.download_location = os.path.expanduser(r'~\Downloads')
                if self.type_switch == 'video' or self.ext == 'mp4' or 'mkv' or 'avi':
                    self.file_type = 'Video'
                    self.download_location += '\Video'
                elif self.type_switch == 'document':
                    self.file_type = 'Document'
                    self.download_location += '\Documents'
                elif self.type_switch == 'image':
                    self.file_type = 'Image'
                    self.download_location += '\Pictures'
                elif self.type_switch == 'application':
                    self.file_type = 'Application'
                    self.download_location += '\Programs'
                elif self.type_switch == 'audio':
                    self.file_type = 'Audio'
                    self.download_location += '\Music'
                elif self.type_switch == 'compressed':
                    self.file_type = 'Compressed'
                    self.download_location += '\Compressed'
                else:
                    self.file_type = 'General'
                if not os.path.exists(self.download_location):
                    os.mkdir(self.download_location)
        except Exception as e:
            print(e)


    def getfilename(self):
        # url = urllib.request.unquote(self.url).decode('utf8')
        if "Content-Disposition" in self.urlinfo.headers:
            value, params = cgi.parse_header(self.urlinfo.headers["Content-Disposition"])
            if 'filename' in params:
                filename = urllib.request.unquote(params['filename'])
                filename = ''.join(filename.split(','))
                return filename.encode('ascii','ignore')
        spliturl = urllib.request.urlsplit(self.url)
        print(spliturl)
        path = spliturl[2]
        filename = path.split('/')[-1]
        filename = ''.join(filename.split('%20'))
        filename = ''.join(filename.split(','))
        return filename.encode('ascii','ignore')

    def downloadnow(self):
        try:
            path = "".join(x for x in urllib.request.urlsplit(self.url)[1] if x.isalnum() or x == '.')
            self.tmpdirname = os.path.join(os.path.expanduser(r"~\AppData\Roaming\MyDownloadManager"), path)
            if os.path.exists(os.path.join(self.tmpdirname, 'log.dat')):
                with open(os.path.join(self.tmpdirname, 'log.dat'), 'rb') as pickle_file:
                    self.downloadtuple = pickle.load(pickle_file)
            else:
                if self.dialog==True:
                    self.file_name = self.lbl_filename.text()
                    self.download_location = self.lbl_Destination.text()
                    self.gendownloadlog()
                    with open('./Extras/logs/fileDetails.csv', "r") as fileInput:
                        rows = -1
                        for row in csv.reader(fileInput):
                            column = 0
                            items = [
                                QtGui.QTableWidgetItem(field)
                                for field in row
                                ]
                            if items[-1] == self.url:
                                break
                            rows += 1
                        print(rows)
                    self.downloadtuple = [rows, self.url, self.file_name, self.lbl_Destination.text(),
                                              self.file_size]
                else:
                    with open('./Extras/logs/fileDetails.csv', "r") as fileInput:
                        rows = 0
                        for row in csv.reader(fileInput):
                            column = 0
                            items = [
                                QtGui.QTableWidgetItem(field)
                                for field in row
                                ]
                            if items[-1]==self.url:
                                break
                            rows += 1
                        print(rows)
                    self.downloadtuple = [rows, self.url, self.file_name, self.download_location,
                                              self.file_size]
                if not os.path.exists(self.tmpdirname):
                    os.mkdir(self.tmpdirname)
                with open(os.path.join(self.tmpdirname, 'log.dat'), 'wb') as pickle_file:
                    pickle.dump(self.downloadtuple, pickle_file)
            if self.dialog == True:
                self.dlg.close()
        except Exception as e:
            print("Error Generated During Adding Download", e)

    def evaluatesize(self, bytesize):
        bytevalue = ('B', 'KB', 'MB', 'GB')
        i = 0
        file_size = bytesize
        while not (file_size < 1024):
            file_size /= 1024
            i += 1
        return "{} {}".format(round(file_size, 2), bytevalue[i])

    def gendownloadlog(self):
        file = open("./Extras/Logs/FileDetails.csv", 'a')
        file_data = """%s,%s%%,%s,%s,%s,%s,%s,%s\n""" % (
        self.file_name, '0', 'Connecting...', 'Undefined', self.file_type,
        self.evaluatesize(self.file_size), strftime("%d-%m-%Y %H:%M:%S"), self.url)
        file.write(file_data)
        file.close()

    def open_dir(self):
        dig = QtGui.QFileDialog()
        dig.setFileMode(QtGui.QFileDialog.Directory)
        direc = dig.getExistingDirectory(None, "Select Save Directory", r"C:/Users/Roopak Chugh/Downloads/")
        if direc != '':
            self.lbl_Destination.setText(direc)
