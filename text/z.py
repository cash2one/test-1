# -*- coding: utf-8 -*-

from PyQt4.Qt import *
from PyQt4 import QtCore
from PyQt4 import QtGui
from t import Ui_MainWindow
import time,sys
class TimeThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str,int) # 信号

    def __init__(self, parent=None):
        super(TimeThread, self).__init__(parent)
        self.working = True

    def run(self):
        self.num=0
        while self.working:
            print "Working", self.thread()
            self.signal.emit("Running time:", self.num) # 发送信号
            self.num += 1
            self.sleep(1)
class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.go)     #open按钮被点击后跳到自定义函数file_dialog
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.go)
        #QtCore.QObject.connect(self.ui.button_save,QtCore.SIGNAL("clicked()"), self.file_save)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()    #getOpenFileName()函数   “打开”
        from os.path import isfile
        if isfile(self.filename):
            self.ui.lineEdit.setText(self.filename)
            s = open(self.filename,'r').readlines()
            for i in s:
                self.ui.textEdit.setText(i)
    global chuli
    def chuli(s,i):
        print s,i
        myapp.setWindowTitle(str(i))
    def go(self):
        self.d=TimeThread()
        print self
        self.d.signal.connect(chuli)
        self.d.start()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())