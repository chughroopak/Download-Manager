# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import threading
from multiprocessing.pool import ThreadPool
import os
import time, gc
import urllib.request
import requests
from Lib import Complete
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
    def __init__(self, downloadtuple):
        # self.up = QtCore.QObject()
        self.bytevalue = ('B', 'KB', 'MB', 'GB')
        # self.up.updateTable = QtCore.pyqtSignal((int, str, str))
        self.row = downloadtuple[0]
        print(self.row)
        self.url = downloadtuple[1]
        self.filename = downloadtuple[2]
        location = downloadtuple[3]
        self.filesize = downloadtuple[4]
        self.progress_old = 0
        self.tmpdir = os.path.join(os.path.expanduser(r"~\AppData\Roaming\MyDownloadManager"),
                                   "".join(x for x in urllib.request.urlsplit(self.url)[1] if x.isalnum() or x == '.'))
        if not os.path.exists(self.tmpdir):
            os.mkdir(self.tmpdir)
        self.tmpdirname = os.path.join(self.tmpdir, self.filename)
        self.location = "{}\{}".format(location, self.filename)
        self.worker = Worker(self.filesize, self.url, self.tmpdirname, self.location, self.tmpdir)
        self.worker.updateSpeed.connect(self.setSpeed)
        self.worker.updateProgress.connect(self.setProgress)
        self.worker.updateStatus.connect(self.setStatus)
        self.worker.close.connect(self.close)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(700, 305)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 305))
        Dialog.setMaximumSize(QtCore.QSize(700, 305))
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./Extras/Icons/down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 180, 131, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lbl_fname = QtGui.QLabel(Dialog)
        self.lbl_fname.setGeometry(QtCore.QRect(210, 20, 441, 31))
        self.lbl_fname.setTextFormat(QtCore.Qt.RichText)
        self.lbl_fname.setWordWrap(True)
        self.lbl_fname.setObjectName(_fromUtf8("lbl_fname"))
        self.lbl_fsize = QtGui.QLabel(Dialog)
        self.lbl_fsize.setGeometry(QtCore.QRect(210, 60, 141, 21))
        self.lbl_fsize.setObjectName(_fromUtf8("lbl_fsize"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 661, 24))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btn_cancel = QtGui.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(430, 260, 150, 30))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_fdwn = QtGui.QLabel(Dialog)
        self.lbl_fdwn.setGeometry(QtCore.QRect(210, 140, 151, 21))
        self.lbl_fdwn.setObjectName(_fromUtf8("lbl_fdwn"))
        self.btn_pause = QtGui.QPushButton(Dialog)
        self.btn_pause.setGeometry(QtCore.QRect(110, 260, 150, 30))
        self.btn_pause.setObjectName(_fromUtf8("btn_pause"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 62, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 53, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 75, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 180, 84, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 55, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbl_status = QtGui.QLabel(Dialog)
        self.lbl_status.setGeometry(QtCore.QRect(210, 100, 141, 21))
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "FileNameDownload", None))
        self.label_8.setText(_translate("Dialog", "0 KB/s", None))
        self.lbl_fname.setText(_translate("Dialog", "Some File", None))
        self.lbl_fsize.setText(_translate("Dialog", "0.00 MB", None))
        self.btn_cancel.setText(_translate("Dialog", "Cancel", None))
        self.lbl_fdwn.setText(_translate("Dialog", "0.00 MB", None))
        self.btn_pause.setText(_translate("Dialog", "Pause", None))
        self.label.setText(_translate("Dialog", "File Name:", None))
        self.label_3.setText(_translate("Dialog", "File Size:", None))
        self.label_5.setText(_translate("Dialog", "Downloaded:", None))
        self.label_7.setText(_translate("Dialog", "Transfer Rate:", None))
        self.label_2.setText(_translate("Dialog", "Status:", None))
        self.lbl_status.setText(_translate("Dialog",
                                           "<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Connecting...</span></p></body></html>",
                                           None))

        # Manual Values
        self.progressBar.setValue(0)
        self.lbl_fname.setText(self.filename)
        self.lbl_fsize.setText(self.evaluatesize(self.filesize))

        # Connections
        self.btn_pause.clicked.connect(self.pause_resume)
        self.btn_cancel.clicked.connect(self.cancel)

    def run(self):
        Dialog = QtGui.QDialog()
        Dialog.setParent(None)
        self.dlg = Dialog
        self.worker.close.connect(self.dlg.close)
        Dialog.setWindowFlags(QtCore.Qt.Window)
        self.setupUi(Dialog)
        Dialog.show()
        self.worker.start()
        if (Dialog.exec_()):
            self.worker.pause = 1
            Dialog.close()

    def setProgress(self):
        progress = 0
        for i in range(8):
            tmp_file_path = self.tmpdirname + '.temp' + str(i)
            progress += os.path.getsize(tmp_file_path) if os.path.exists(tmp_file_path) else 0
        self.lbl_fdwn.setText(self.evaluatesize(progress))
        if self.filesize != 0:
            self.dlg.setWindowTitle(str(progress * 100 // self.filesize) + '% Completed-' + self.filename)
            self.progressBar.setValue(progress * 100 / self.filesize)
        self.worker.updateTable.emit(self.row, str(round(progress * 100 / self.filesize, 2)), None,None)

    def setStatus(self, status, tstatus):
        self.lbl_status.setText(_translate("Dialog", status, None))
        self.worker.updateTable.emit(self.row, None, tstatus, None)

    def setSpeed(self, speed, time_left):
        self.label_8.setText(self.evaluatesize(speed) + '/s')
        self.worker.updateTable.emit(self.row, None, None , time_left)

    def evaluatesize(self, bytesize):
        i = 0
        file_size = bytesize
        while not (file_size < 1024):
            file_size /= 1024
            i += 1
        return "{} {}".format(round(file_size, 2), self.bytevalue[i])

    def pause_resume(self):
        """Gives Functionality to cancel and resume buttons"""
        if self.btn_pause.text() == 'Pause':
            self.worker.pause = 1
            self.btn_pause.setText("Resume")
        elif self.btn_pause.text() == 'Resume':
            self.btn_pause.setText("Pause")
            self.worker.pause = 0
            self.worker.start()

    def cancel(self):
        self.worker.pause = 1
        self.setStatus(
            "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Paused!</span></p></body></html>",
            'Paused')
        self.dlg.close()

    def close(self):
        self.dlg.close()
        Complete.Ui_Dialog(self.url, self.location)

class Worker(QtCore.QThread):
    # This is the signal that will be emitted during the processing.
    # By including int as an argument, it lets the signal know to expect
    # an integer argument when emitting.
    updateSpeed = QtCore.pyqtSignal(int,str)
    updateProgress = QtCore.pyqtSignal()
    updateStatus = QtCore.pyqtSignal((str, str))
    updateTable = QtCore.pyqtSignal((int, str, str, str))
    close = QtCore.pyqtSignal()

    def __init__(self, file_size, url, tmpfiledir, location, tmpdir):
        QtCore.QThread.__init__(self)
        self.filesize = file_size
        self.url = url
        self.tmpdir = tmpdir
        self.tmpfiledir = tmpfiledir
        self.location = location
        self.timecheck = 0

    def run(self):
        """starts the QThread worker"""
        self.processes = []
        self.pause = 0
        self.complete = 0
        self.dwnsize = 0
        self.oldsize = 0
        # response = requests.head(self.url)
        # self.isRange = True if 'Accept-Ranges' in response.headers else False
        # if self.isRange == True:
        p = threading.Thread(target=self.multi_download)
        # else:
        #    p = threading.Thread(target=self.downloadsingle)
        q = threading.Thread(target=self.speed)
        r = threading.Thread(target=self.progress)
        q.start()
        p.start()
        r.start()
        p.join()
        q.join()
        r.join()

    def multi_download(self):
        """Creates Multiple part download threads and starts them"""
        import math
        block_size = math.ceil(self.filesize / 8)
        start = 0

        # creating and starting threads and
        # appending them to the processes list
        for i in range(8):
            end = start + block_size if i != 7 else self.filesize
            self.processes.append((i, start, end))
            start = end + 1
        p = ThreadPool(processes=8)
        p.starmap(self.download_file, self.processes)
        p.close()
        p.join()

    def download_file(self, i, start, end):
        """Downloads the File with range(start to end)"""

        # don't download if the file exists
        tmp_file_path = self.tmpfiledir + '.temp' + str(i)
        if os.path.exists(tmp_file_path):
            self.dwnsize = self.dwnsize + os.path.getsize(tmp_file_path)
            if os.path.getsize(tmp_file_path) >= end - start or os.path.getsize(tmp_file_path) >= self.filesize - start:
                self.updateProgress.emit()
                self.complete += 1
            if self.complete == 8:
                self.completed()
                return

        try:
            downloaded = 0
            # If Temp file already exists then resume the download.
            first_byte = start
            if os.path.exists(tmp_file_path):
                first_byte += os.path.getsize(tmp_file_path)

                # set the progress to correct value
                self.updateProgress.emit()

            # Request part file
            r = requests.get(self.url, stream=True, headers={'Range': 'bytes=%s-%s' % (first_byte, end)})
            self.updateStatus.emit(
                "<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Downloading...\
                </span></p></body></html>",
                'Downloading')
            if not os.path.exists(tmp_file_path):
                f = open(tmp_file_path, 'wb')
                f.close()
            # write chunks to temp file
            chunk_size = 1024 * 8
            with open(tmp_file_path, 'ab') as f:
                for chunk in r.iter_content(chunk_size):
                    if self.pause == 1:
                        f.close()
                        break
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        self.dwnsize += len(chunk)
                        downloaded += len(chunk)
                    if downloaded >= end - first_byte:
                        self.complete += 1
                        break
        except Exception as e:
            print(e)
        else:
            self.updateProgress.emit()
            if self.dwnsize >= self.filesize:
                self.completed()
            elif self.pause == 1:
                self.updateStatus.emit(
                    "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Paused!</span></p></body></html>",
                    'Paused')
            if self.filesize == -1:
                raise Exception('Error getting Content-Length from server: %s' % self.url)

    def completed(self, single=False):
        progress = 0
        self.updateStatus.emit(
            "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Joining Parts</span></p></body></html>",
            'Joining Parts')
        if single == True:
            progress = os.path.getsize(self.tmpfiledir + '.temp' + str(0))
            with open(self.location, 'ab', 0) as file:
                file1 = open(self.tmpfiledir + '.temp' + str(0), 'rb')
                file.write(file1.read())
                file1.close()
            os.remove(self.tmpfiledir + '.temp' + str(0))
        else:
            for i in range(8):
                tmp_file_path = self.tmpfiledir + '.temp' + str(i)
                progress += os.path.getsize(tmp_file_path)
            if progress == self.filesize:
                for i in range(8):
                    tmp_file_path = self.tmpfiledir + '.temp' + str(i)
                    with open(self.location, 'ab') as file:
                        file1 = open(tmp_file_path, 'rb')
                        file.write(file1.read())
                        file1.close()
                    os.remove(tmp_file_path)
                self.updateStatus.emit(
                    "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Completed</span></p></body></html>",
                    'Completed')
                # os.remove(self.tmpdir + '\log.dat')
                # os.rmdir(self.tmpdir)
                cmp = self.tmpdir + '\complete.dat'
                with open(cmp,'w') as file:
                    file.write(self.url + ',' + self.location)
                self.close.emit()

    def downloadsingle(self):
        tmp_file_path = self.tmpfiledir + '.temp0'
        try:
            # If Temp file already exists then resume the download.
            first_byte = 0
            if os.path.exists(tmp_file_path):
                first_byte = os.path.getsize(tmp_file_path)
                # set the progress to correct value
                self.updateProgress.emit()
            # Request part file
            r = requests.get(self.url, stream=True, headers={'Range': 'bytes=%s-' % first_byte})
            if r.status_code == requests.codes.ok:
                print(r)
                self.updateStatus.emit(
                    "<html><head/><body><p><span style=\" font-weight:600; color:#0000ff;\">Downloading...Single</span></p></body></html>",
                    'Downloading Single')
                if not os.path.exists(tmp_file_path):
                    f = open(tmp_file_path, 'wb', 0)
                    f.close()
                # write chunks to temp file
                with open(tmp_file_path, 'ab', 0) as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if self.pause == 1:
                            f.close()
                            for i in Worker.Url:
                                if self.Url == Worker.Url[i]:
                                    Worker.Url.remove(i)
                            break
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            # update progress
                            if self.dwnsize <= self.filesize:
                                self.updateProgress.emit()
                                self.sleep(0.1)
                                # check exit
        except Exception as e:
            print(e)
        else:
            self.updateProgress.emit()
            if self.pause != 1:
                self.updateProgress.emit()
                self.completed(single=True)
                self.updateStatus.emit(
                    "<html><head/><body><p><span style=\" font-weight:600; color:#00ff00;\">Completed</span></p></body></html>",
                    'Completed')
            elif self.pause == 1:
                self.updateStatus.emit(
                    "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Paused!</span></p></body></html>",
                    'Paused')
                for i in Worker.Url:
                    if self.Url == Worker.Url[i]:
                        Worker.Url.remove(i)
            if self.filesize == -1:
                raise Exception('Error getting Content-Length from server: %s' % self.url)

    def speed(self):
        averageSpeed = 0
        while self.pause != 1 and self.complete != 8:
            factor1 = self.dwnsize
            time.sleep(1.0)
            lastSpeed = self.dwnsize - factor1
            averageSpeed = 0.2 * lastSpeed + 0.8 * averageSpeed
            if averageSpeed != 0:
                time_left = (self.filesize-self.dwnsize)//averageSpeed
                if time_left<60:
                    time_left=str(time_left)+' s'
                elif time_left < 3600:
                    time_left=str(time_left // 60)+' min(s) ' + str(time_left % 60) + ' sec(s)'
                elif time_left > 3600:
                    time_left = str(time_left // 3600) + ' hr(s) ' + str((time_left % 3600) // 60) + ' min(s) ' \
                                + str((time_left % 3600) % 60) + ' sec(s)'
            else:
                time_left = 'Undefined'
            self.updateSpeed.emit(averageSpeed, time_left)

    def progress(self):
        while self.pause != 1 and self.complete != 8:
            self.updateProgress.emit()
            time.sleep(0.1)
