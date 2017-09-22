# -*- coding: utf-8 -*-

from PyQt4.Qt import *
from PyQt4 import QtCore
from PyQt4 import QtGui
from biModel import Ui_MainWindow
import useragent
import time,sys,random
import getkw
reload(sys)
sys.setdefaultencoding('utf-8')
def randomsleeps(ss,es):
    times=random.randint(ss,es)
    time.sleep(times)
class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.go)     #open按钮被点击后跳到自定义函数file_dialog
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.seeurl)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.go)
        #self.connect(self.ui.pushButton2, QtCore.SIGNAL("clicked()"), self.gop)
        #QtCore.QObject.connect(self.ui.button_save,QtCore.SIGNAL("clicked()"), self.file_save)
    def seeurl(self):
        fr=open('usr/keywords.txt','r').read()
        QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))
        self.ui.textEdit.setText(fr)
    global ssprint
    def ssprint(self,con):
        self.ui.listWidget_2.addItem(con)
        QtGui.QApplication.processEvents()
    def go(self):
        fro=open('usr/keywords.txt','r')
        frows=fro.readlines()
        fro.close()
        t = time.strftime('%Y%m%d')
        fwxl=open('result/xiala_%s.txt'%t,'w')
        fwxg=open('result/xiangguan_%s.txt'%t,'w')
        ysy=0
        ysl=0
        wsy=0
        wsl=0
        ysys=0
        wsys=0
        wsws=0
        for x,row in enumerate(frows,1):
            kw = row.strip()
            xls=getkw.get_sug(kw)
            xl='\n'.join(xls)
            ssprint(self,'-----%s、%s的下拉：'%(x,kw))
            ssprint(self,xl)
            fwxl.write(xl)
            xgs=getkw.relatewords(kw)
            xg='\n'.join(xgs)
            ssprint(self,'-----%s、%s的相关搜索：'%(x,kw))
            ssprint(self,xg)
            fwxg.write(xg)
            randomsleeps(3,6)
        ssprint(self,u'关键词查询完毕')
        fwxl.close()
        fwxg.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
