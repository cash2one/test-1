# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
#从 ui.py 文件里 import ui类
from GUI import Ui_Dialog
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
class MyDialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        #调用内部的 setupUi() ，本身对象作为参数
        self.setupUi(self)
        #连接 QPushButton 的点击信号到槽 BigWork()
        self.pushButton.clicked.connect(self.BigWork)

    def BigWork(self):
        #把按钮禁用掉
        self.pushButton.setDisabled(True)
        print '1'
        kw=self.kw.text()
        #import 自己的进程类
        from threads import BigWorkThread
        #新建对象，传入参数
        print 'rrr',self
        self.bwThread = BigWorkThread('gos',kw,self)
        #连接子进程的信号和槽函数
        self.bwThread.finishSignal.connect(self.BigWorkEnd)
        #开始执行 run() 函数里的内容
        print 'go'
        self.bwThread.start()
    def gos(self,kw,c1):
        print '1'
        kw=c1.kw.text()
        #for i in range(5):
        i=2
        l="%s、%s"%(i,kw)
        return l
    def BigWorkEnd(self,ls):
        print 'get!'
        #使用传回的返回值
        self.setWindowTitle(ls)
        self.pushButton.setDisabled(False)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #新建类对象
    Dialog = MyDialog()
    #显示类对象
    Dialog.show()
    sys.exit(app.exec_())