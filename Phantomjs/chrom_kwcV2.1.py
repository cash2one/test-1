# -*- coding: utf-8 -*-

"""
a QtGui.QInputDialog dialog.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys,random,time,os,psutil
from PyQt4 import QtGui
from PyQt4 import QtCore
reload(sys)
sys.setdefaultencoding('utf-8')

class MyThread(QtCore.QThread):
    def __init__(self,cla,func):
        global name
        super(MyThread,self).__init__()
        self.func = func
        name= cla

    def run(self):
        self.func(name)

class Opensetting(QtGui.QDialog):
    def __init__(self,parent=None):
        global open
        f=open('usr/setting.ini','r').readline()
        ws=eval(f)
        site=ws["site"]
        pn=int(ws["pn"])
        pages=int(ws["pages"])-random.randint(-2,2)
        firstdir=ws["firstdir"]
        stop_time=int(ws["stop_time"])

        QtGui.QWidget.__init__(self)
        opens=QtGui.QPushButton('Save')
        self.resize(250,200)
        self.connect(opens,QtCore.SIGNAL('clicked()'),self.saveok)
        girdLayout=QtGui.QGridLayout()
        girdLayout.addWidget(opens,6,1,1,1)
        global text1,text2,text3,text4,text5
        label1= QtGui.QLabel('site')
        girdLayout.addWidget( label1, 0, 0)
        text1 = QtGui.QLineEdit(ws["site"])
        girdLayout.addWidget ( text1 , 0, 1)

        label2= QtGui.QLabel('firstdir')
        girdLayout.addWidget( label2, 1, 0)
        text2 = QtGui.QLineEdit(ws["firstdir"])
        girdLayout.addWidget ( text2 , 1, 1)


        label3= QtGui.QLabel('pn')
        girdLayout.addWidget( label3, 2, 0)
        text3 = QtGui.QLineEdit(ws["pn"])
        girdLayout.addWidget ( text3 , 2, 1)


        label4= QtGui.QLabel('stop_time')
        girdLayout.addWidget( label4, 3, 0)
        text4 = QtGui.QLineEdit(ws["stop_time"])
        girdLayout.addWidget ( text4 , 3, 1)


        label5= QtGui.QLabel('pages')
        girdLayout.addWidget( label5, 4, 0)
        text5 = QtGui.QLineEdit(ws["pages"])
        girdLayout.addWidget ( text5 , 4, 1)
        self.setLayout( girdLayout)
        self.setWindowTitle('Setting windows')
        self.show()
    def saveok(self):
        site=text1.text()
        firstdir=text2.text()
        stop_time=int(text3.text())
        pn=int(text4.text())
        pages=int(text5.text())
        ressave='''{'site': '%s', 'firstdir': '%s', 'pn':'%s', 'stop_time': '%s', 'pages': '%s'}'''%(site,firstdir,pn,stop_time,pages)
        try:
            with open('usr/setting.ini','w') as sf:
                sf.write(ressave)
            sf.close()

        except Exception,e:
            pass
    def ok(self):
        web=Web_Browser()
        web.setModal(False)
        self.resize(250,300)
        web.setWindowTitle('sub window')
        web.exec_()

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.kwl=QtGui.QLabel(self)
        self.kwl.setText(u"将要点击的关键词：")
        self.kwl.setGeometry(20,10,100,20)

        f=open('usr/kw.txt').read()

        self.kwlist=QtGui.QListWidget(self)
        self.kwlist.setGeometry(20,40,100,200)
        self.kwlist.addItem(f.decode('utf-8'))

        self.kwl=QtGui.QLabel(self)
        self.kwl.setText(u"已点击的关键词：")
        self.kwl.setGeometry(20,250,100,20)

        self.ykwlist=QtGui.QListWidget(self)
        self.ykwlist.setGeometry(20,280,100,200)

        self.listFile=QtGui.QListWidget(self)
        self.listFile.setGeometry(150,40,430,420)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("usr/img/l.ico"),QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.btn = QtGui.QPushButton(u'开始点击 GO！', self)
        self.btn.move(150, 10)
        self.btn.clicked.connect(self.gos)

        self.tipl=QtGui.QLabel(self)
        self.tipl.setGeometry(270,10,150,20)

        self.btnset = QtGui.QPushButton(u'点击配置', self)
        self.btnset.move(500, 10)
        self.btnset.clicked.connect(self.openset)

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(150,467,330,20)
        self.n1=QtGui.QLabel(self)
        self.n1.setText(u"内存：")
        self.n1.setGeometry(480,467,30,20)
        self.n2=QtGui.QLabel(self)
        self.n2.setGeometry(520,467,40,20)

        self.resize(600, 500)
        self.setWindowTitle(u'炽火点击软件 By Tian')
        self.setWindowIcon(icon)
        self.center()
        self.show()
    def openset(self):
        self.openwin=Opensetting()
    global ssprint
    def ssprint(self,con):
        self.listFile.addItem(con)
        QtGui.QApplication.processEvents()
    global kwprint
    def kwprint(self,con):
        self.ykwlist.addItem(con)
        QtGui.QApplication.processEvents()
    def gos(self):
        self.btn.setEnabled(False)
        self.btnset.setEnabled(False)
        self.thread1 = MyThread(self,stc)
        self.thread1.start() #此处开始自动调用线程的run函数
        self.thread1.wait()
    global stc
    def stc(self):

        def clla(dr,ys):
            actions = ActionChains(driver)
            actions.move_to_element(ys)
        def randomsleeps(ss,es):
            times=random.randint(ss,es)
            time.sleep(times)
        def click(driver,ems,site):
            iii=0
            while iii == 0 :
                ydj=random.choice(ems)
                qu=ydj.get_attribute('href')
                if site in qu and 'img2.' not in qu:
                    js="var q=document.body.scrollTop=200"
                    driver.execute_script(js)
                    time.sleep(3)
                    clla(driver,ydj)
                    try :
                        ydj.click()
                        iii = 1
                    except Exception,e:
                        iii = 0
            ss=stop_time-random.randint(-2,2)
            time.sleep(ss)
            #wds=[u"红酒招商",u"白酒招商",u"酒水招商",u"葡萄酒招商",u"名酒招商",u"酒水代理",u"啤酒招商",u"保健酒代理",u"葡萄酒代理"]
        #wds=[u"黑桃a香槟多少钱一瓶",u"杏花村散酒加盟"]
        #wds=[u"酒水",u"酒水招商",u"衡水老白干啤酒",u"红枣啤酒",u"黄金酒多少钱一瓶",u"赊店老酒",u"玛咖啤酒",u"法国红酒品牌有哪些"]
        #wds=[u"黄金酒多少钱一瓶",u"赊店老酒",u"玛咖啤酒",u"法国红酒品牌有哪些",u"梦之蓝多少钱一瓶",u"酒招商",u"酒水招商",u"酒水代理",u"名酒招商",u"名酒代理",u"白酒招商",u"酒水招商网",u"酒水代理网",u"啤酒招商",u"红酒招商",u"鸡尾酒招商",u"保健酒招商",u"葡萄酒招商",u"果酒招商",u"米酒招商",u"进口酒招商",u"黄酒招商",u"白酒代理",u"啤酒代理",u"红酒代理",u"鸡尾酒代理",u"保健酒代理",u"葡萄酒代理",u"果酒代理",u"米酒代理",u"进口酒代理",u"黄酒代理"]
        #读取关键词,kw一行一个

        wds=open("usr/kw.txt",'r').readlines()
        f=open('usr/setting.ini','r').readline()
        ws=eval(f)
        site=ws["site"]
        pn=int(ws["pn"])
        pages=int(ws["pages"])-random.randint(-2,2)
        firstdir=ws["firstdir"]
        stop_time=int(ws["stop_time"])
        kwnum=len(wds)
        self.pbar.setMinimum(0)
        self.pbar.setMaximum(kwnum)
        current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        datetime=time.strftime('%Y%m%d')
        ft="rank_data%s.txt"%datetime
        if os.path.exists('usr/res/'+ft):
            exf=random.randint(10,1000)
            #print 'rename file'
            ft = 'new_%s_%s'%(exf,ft)
            #print ft
        fres=open('usr/res/'+ft,'w')
        #fres.write(current_date+':\n')
        print '''I will Start...\nI will check the rank of %s\nI have %s keywords to check\nI will find %s pages\nI will see %s pages of site,first url:%s(0 is no limited)\nafter I sleep %s s , I go on'''%(site,kwnum,pn,pages,firstdir,stop_time)

        '''
        我将要查询网站%s的排名情况，有%s个关键词将要处理，每个关键词我会查询%s页.
        文件生成在usr/res/文件夹中，请根据相应日期查看。
        每个排名我会点击个%s左右的页面，每个页面大约停留%s秒左右。
        第一个页面我会优先点击包含%s的网址（若为0则为不限制），请确认存在，若不存在则不点击。
        点击马上开始！'''
        randomsleeps(5,10)
        random.shuffle(wds)
        self.tipl.setText(u"点击进行中……")
        info = psutil.virtual_memory()
        print info
        for index,wd in enumerate(wds,1):
            self.n2.setText('%s%%'%info.percent)
            try:
                wd=wd.strip()
                driver=webdriver.Chrome('usr\Chrome\Application\chromedriver.exe')  #调用chrome浏览器
                #driver.set_window_position(20, 40)
                driver.maximize_window()
                driver.get('https://www.baidu.com/')
                elem = driver.find_element_by_id("kw")
                elem.send_keys(unicode(wd, "utf-8"))
                elem.send_keys(Keys.RETURN)
                #driver.implicitly_wait(5)
                randomsleeps(3,6)
                if u"_百度搜索" not in driver.title:
                    continue
                i1=0
                i2=0
                rk=0
                while i1<pn and i2==0 :
                    print 'I will check No.%s page'%(i1+1)
                    surl=driver.find_elements_by_xpath("//div[@class='f13']/a")
                    for j,su in enumerate(surl,1):
                        at = su.text
                        if site in at:
                            su1=su
                            i2+=1
                            rk+=j
                            clla(driver,su1)
                            su1.click()
                            break
                        else:
                            continue
                    if i2 == 0:
                        np=driver.find_element_by_link_text(u"下一页>")
                        np.click()
                        i1+=1
                        randomsleeps(4,8)
                        rk+=10
                if i2 == 0:
                    print '%s,no rand'%wd
                    fres.write('%s,no rand \n'%wd)
                    continue
                time.sleep(stop_time)
                randomsleeps(7,13)
                handles = driver.window_handles
                for handle in handles:
                    if driver.current_window_handle != handle:
                        driver.switch_to.window(handle)
                ress='%s、kw:%s,rank:%s,url:%s'%(index,wd,rk,driver.current_url)
                print ress
                fres.write(ress+'\n')
                #print driver.page_source
                if firstdir != '0':
                    qwe=driver.find_elements_by_xpath("//a[contains(@href,'%s')]"%firstdir)
                else :
                    qwe=driver.find_elements_by_xpath("//a")
                if len(qwe) == 0 :
                    #print len(qwe)
                    continue
                print '----I get %s A'%len(qwe)
                click(driver,qwe,site)
                r=pages+random.randint(-3,3)
                print 'will %s clicks'%r
                i=0
                while i<r:
                    print 'will click %s'%i
                    handles = driver.window_handles
                    for handle in handles:
                        if driver.current_window_handle != handle:
                            driver.switch_to.window(handle)
                    try:
                        qqq=driver.find_elements_by_xpath("//a[contains(@href,'/')]")
                        click(driver,qqq,site)
                        i+=1
                    except Exception,e:
                        print 'there is a err,U will go on'
                        i+=1
                        randomsleeps(8,20)
                driver.switch_to.window(handles[0])
                driver.close()
                try:
                    os.system('taskkill /f /im chromedriver.exe')
                except Exception,e:
                    print 'kill dri faild'
            except Exception,e:
                print 'a err,check the next word'
            kwprint(self,wd.decode('utf-8'))
            self.pbar.setValue(index)

        fres.close()
        self.tipl.setText(u"点击完成！")
        self.btn.setEnabled(True)
        self.btnset.setEnabled(True)
    def center(self):  #主窗口居中显示函数
        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()