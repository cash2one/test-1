# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import time

#继承 QThread 类
class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    finishSignal = QtCore.pyqtSignal(str)
    #构造函数里增加形参
    def __init__(self, par,kw,c,parent=None):
        super(BigWorkThread, self).__init__(parent)
        global c1,p1
        #储存参数
        c1 = c
        p1 = par
        self.kw=kw

        #重写 run() 函数，在里面干大事。
    def run(self):
        print 'www',self
        c1.p1(self.kw,c1)
        print 'ss'
        time.sleep(4)
        print 'se'
        #大事干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(t1)