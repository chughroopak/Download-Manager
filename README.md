# Download-Manager
A basic python-PyQT based download manager.

### About the Project
•	This tool was prepared as Engineering minor project.

•	This project may be classified as a Desktop Application and it serves the purpose of downloading files from the Internet using HTTP or HTTPS protocols and managing them.

•	The project uses multithreading to download files in segments using multiple simultaneous connections, thus using the internet connection to its full potential, and then combining the segments to produce the original file.

•	A special care about what Python version is used should be kept in mind since the application in written in Python 3.4 using PyQt4 GUI implementation, it will not run on any other combination of Python and PyQt.

•	This application will only download files from the HTTP and HTTPS protocols.Hopefully, further attempt will be made to add support for file download through FTP and Torrent Downloads

### Requirements
1. Python 3.4
2. PyQT4 
> pip install pyqt4
3. Requests
> pip install requests
4. Download and install Qt version 4 from QT website.

### How to run?
Use start.bat to start the application after your system is set up with requirements.
