from Lib import MainWindow
import os


if not os.path.exists(os.path.expanduser(r"~\AppData\Roaming\MyDownloadManager")):
    os.mkdir(os.path.expanduser(r"~\AppData\Roaming\MyDownloadManager"))

default_download_path = os.path.expanduser(r'~\Downloads')
if not os.path.exists(default_download_path+'\Video'):
    os.mkdir(default_download_path+'\Video')
if not os.path.exists(default_download_path+'\Programs'):
    os.mkdir(default_download_path+'\Programs')
if not os.path.exists(default_download_path+'\Compressed'):
    os.mkdir(default_download_path+'\Compressed')
if not os.path.exists(default_download_path+'\Audio'):
    os.mkdir(default_download_path+'\Audio')
if not os.path.exists(default_download_path+'\Documents'):
    os.mkdir(default_download_path+'\Documents')
if not os.path.exists(default_download_path+'\Pictures'):
    os.mkdir(default_download_path+'\Pictures')


ui = MainWindow.Ui_MainWindow(run=True)
