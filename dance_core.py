import sys
from PyQt4 import QtGui, QtCore, uic
from audio_backend_so_copy import sliceWav

qtCreatorFile = "dance.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class core(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self): 
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.browse.clicked.connect(self.browseCallback)
        self.dance.clicked.connect(self.danceCallback)
    def browseCallback(self):
        filepath = QtGui.QFileDialog.getOpenFileNames(None, 'Select a WAV file:', 'C:\\')
        self.filePathEdit.setText(filepath[0])
        print(filepath[0])
    def danceCallback(self):
        if self.filePathEdit.text() != "":
            sliceWav(self.filePathEdit.text())
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = core()
    window.show()
    sys.exit(app.exec_())
