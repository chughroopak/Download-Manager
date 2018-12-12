# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import csv
from Lib import AddUrl,DownloadInfo,Download,FileAlreadyExist,Complete
import ctypes,os
import sys
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

class Ui_MainWindow(object):
    def __init__(self, run=False):
        myappid = 'ironfist.MyDownloadManager.0.1'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.add_download = []
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        ret = app.exec_()
        self.csvupdate()
        sys.exit(ret)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(807, 715)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/DownloadManagerIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setRowCount(0)
        self.table.setColumnCount(8)
        self.table.setObjectName(_fromUtf8("table"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(7, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.horizontalHeader().setMinimumSectionSize(150)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_Download = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddUrl = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddUrl.setIcon(icon2)
        self.actionAddUrl.setObjectName(_fromUtf8("actionAddUrl"))
        self.actionResume = QtGui.QAction(MainWindow)
        self.actionResume.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/resume.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResume.setIcon(icon3)
        self.actionResume.setObjectName(_fromUtf8("actionResume"))
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionDelete_Selected = QtGui.QAction(MainWindow)
        self.actionDelete_Selected.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Selected.setIcon(icon4)
        self.actionDelete_Selected.setObjectName(_fromUtf8("actionDelete_Selected"))
        self.actionDeleteCompleted = QtGui.QAction(MainWindow)
        self.actionDeleteCompleted.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/delete-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteCompleted.setIcon(icon5)
        self.actionDeleteCompleted.setObjectName(_fromUtf8("actionDeleteCompleted"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon6)
        self.toolBar.addAction(self.actionAddUrl)
        self.toolBar.addAction(self.actionResume)
        self.toolBar.addAction(self.actionDelete_Selected)
        self.toolBar.addAction(self.actionDeleteCompleted)
        self.toolBar.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Manager", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File Name", None))
        item.setToolTip(_translate("MainWindow", "File Name", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "%Downloaded", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time Left", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "File Type", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "File Size", None))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date Added", None))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "File Url", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAddUrl.setText(_translate("MainWindow", "AddUrl", None))
        self.actionAddUrl.setToolTip(_translate("MainWindow", "Add Url To Download File", None))
        self.actionAddUrl.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionResume.setText(_translate("MainWindow", "Resume", None))
        self.actionResume.setToolTip(_translate("MainWindow", "Resume Selected Download", None))
        self.actionDelete_Selected.setText(_translate("MainWindow", "Delete Selected", None))
        self.actionDelete_Selected.setToolTip(_translate("MainWindow", "Delete Selected Files", None))
        self.actionDelete_Selected.setShortcut(_translate("MainWindow", "Del", None))
        self.actionDeleteCompleted.setText(_translate("MainWindow", "DeleteCompleted", None))
        self.actionDeleteCompleted.setToolTip(_translate("MainWindow", "Delete All Completed File Entries", None))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open Selected File", None))

        # Connections
        self.actionAdd_Download.triggered.connect(self.runAddUrl)
        self.actionAddUrl.triggered.connect(self.runAddUrl)
        self.table.itemSelectionChanged.connect(self.table_connect)
        self.actionResume.triggered.connect(self.resume)
        self.actionDelete_Selected.triggered.connect(self.deleteselected)

        # Pre-load
        self.loadCsv()

    def nongui(self):
        """Decorator running the function in non-gui thread while
        processing the gui events."""
        from multiprocessing.pool import ThreadPool
        from PyQt4.QtGui import QApplication

        def wrap(*args, **kwargs):
            pool = ThreadPool(processes=1)
            async = pool.apply_async(self, args, kwargs)
            while not async.ready():
                async.wait(0.5)
                QApplication.processEvents()
            return async.get()
        return wrap

    def table_connect(self):
        try:
            self.actionResume.setEnabled(False)
            self.actionDelete_Selected.setEnabled(False)
            self.actionOpen.setEnabled(False)
            row = self.table.currentItem().row()
            status = self.getrowcell(row,'Status')
            if status == 'Paused' or status== 'Connecting...':
                self.actionResume.setEnabled(True)
                self.actionDelete_Selected.setEnabled(True)
            elif status == 'Downloading':
                self.actionDelete_Selected.setEnabled(True)
            elif status == 'Completed':
                self.actionOpen.setEnabled(True)
                self.actionDelete_Selected.setEnabled(True)
            for i in range(self.table.rowCount()):
                if self.table.item(i, 2).text() == 'Downloading' or self.table.item(i,2).text() == 'Downloading(SingleConn.)':
                    self.actionDelete_Selected.setDisabled(True)
        except Exception as e:
            print(e)

    def getrowcell(self, row, columnname):
        # loop through headers and find column number for given column name
        headercount = self.table.columnCount()
        for x in range(headercount):
            headertext = self.table.horizontalHeaderItem(x).text()
            if columnname == headertext:
                matchcol = x
                break
        cell = self.table.item(row,matchcol).text()  # get cell at row, col
        return cell

    def setrowcell(self,row,columnname,value):
        # loop through headers and find column number for given column name
        headercount = self.table.columnCount()
        for x in range(headercount):
            headertext = self.table.horizontalHeaderItem(x).text()
            if columnname == headertext:
                matchcol = x
                break
        self.table.setItem(row, matchcol, QtGui.QTableWidgetItem(value))  # set cell value at the given column name

    def runAddUrl(self):
        self.csvupdate()
        dl = MainWorker(self)
        dl.updateTable.connect(self.tableupdate)
        dl.run()

    def resume(self):
        self.csvupdate()
        dl = MainWorker(self)
        dl.updateTable.connect(self.tableupdate)
        dl.resume()

    def loadCsv(self):
        rows = 0
        with open('./Extras/logs/fileDetails.csv', "r") as fileInput:
            for row in csv.reader(fileInput):
                column = 0
                items = [
                    QtGui.QTableWidgetItem(field)
                    for field in row
                    ]
                self.table.setRowCount(rows + 1)
                for item in items:
                    self.table.setItem(rows, column, item)
                    column += 1
                rows += 1
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def closewindow(self):
        self.csvupdate()
        print(1)
        sys.exit()

    def tableupdate(self, row, progress=None, status=None, time_left=None):
        if progress is not None and progress != '':
            self.table.setItem(row, 1, QtGui.QTableWidgetItem(progress+'%'))
        elif status is not None and status != '':
            self.table.setItem(row, 2, QtGui.QTableWidgetItem(status))
        elif time_left is not None and time_left != '':
            self.table.setItem(row, 3 , QtGui.QTableWidgetItem(time_left))

    def csvupdate(self):
        with open("./Extras/Logs/FileDetails.csv", 'w',newline='') as stream:
            writer = csv.writer(stream)
            for row in range(self.table.rowCount()):
                rowdata = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)

    def deleteselected(self):
        idx = self.table.currentRow()
        self.table.removeRow(idx)
        self.csvupdate()



class MainWorker(QtCore.QThread):
    # This is the signal that will be emitted during the processing.
    # By including int as an argument, it lets the signal know to expect
    # an integer argument when emitting.
    updateTable = QtCore.pyqtSignal((int, str, str, str))

    # You can do any extra things in this init you need, ensure to call the super's init
    all_downloads = []
    def __init__(self,parent):
        QtCore.QThread.__init__(self)
        self.table = parent.table

    def run(self):
        """Gets Url And Starts Download"""
        downloadtuple = None
        obj = AddUrl.Ui_Dialog()
        url = obj.url
        choice = 0
        count = 0
        row = 0
        if url is not None:
            for i in range(self.table.rowCount()):
                print(i)
                if self.getrowcell(i, 'File Url') == url:
                    count += 1
                    row += 1
            if count != 0:
                obj1 = FileAlreadyExist.Ui_Dialog()
                obj1.run(url)
                choice = obj1.choice
            if choice == -1:
                return
            else:
                print (choice)
                if choice == 3:
                    self.table.removeRow(row)
                obj = DownloadInfo.Ui_Dialog()
                complete = obj.run(url,choice,count)
                downloadtuple = obj.downloadtuple
                self.loadCsv()
                print(complete)
                print(downloadtuple)
            if complete == 1:
                Complete.Ui_Dialog(url,os.path.join(obj.download_location,obj.file_name))
            elif downloadtuple is not None:
                download = Download.Ui_Dialog(downloadtuple)
                download.worker.updateTable.connect(self.tu)
                MainWorker.all_downloads.append(download)
                download.run()

    def tu(self, row, progress, status, time_left):
        self.updateTable.emit(row, progress, status, time_left)

    def getrowcell(self,row, columnname):
        # loop through headers and find column number for given column name
        headercount = self.table.columnCount()
        for x in range(headercount):
            headertext = self.table.horizontalHeaderItem(x).text()
            if columnname == headertext:
                matchcol = x
                break
        cell = self.table.item(row,matchcol).text()  # get cell at row, col
        return cell

    def setrowcell(self,row,columnname,value):
        # loop through headers and find column number for given column name
        headercount = self.table.columnCount()
        for x in range(headercount):
            headertext = self.table.horizontalHeaderItem(x).text()
            if columnname == headertext:
                matchcol = x
                break
        self.table.setItem(row, matchcol, QtGui.QTableWidgetItem(value))  # set cell value at the given column name

    def loadCsv(self):
        rows = 0
        with open('./Extras/logs/fileDetails.csv', "r") as fileInput:
            for row in csv.reader(fileInput):
                column = 0
                items = [
                    QtGui.QTableWidgetItem(field)
                    for field in row
                    ]
                self.table.setRowCount(rows + 1)
                for item in items:
                    self.table.setItem(rows, column, item)
                    column += 1
                rows += 1
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def resume(self):
        row = self.table.currentItem().row()
        url = self.table.item(row,7).text()
        if url is not None:
            obj = DownloadInfo.Ui_Dialog()
            obj.run(url,dialog= False)
            obj.downloadnow()
            downloadtuple = obj.downloadtuple
            self.loadCsv()
            if downloadtuple is not None:
                download = Download.Ui_Dialog(downloadtuple)
                download.row = row
                download.worker.updateTable.connect(self.tu)
                download.run()

    def stopSelected(self,to_stop):
            for download in MainWorker.all_downloads:
                if to_stop == download.url:
                    download.cancel()
