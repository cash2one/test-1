#!/usr/bin/env python
#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,random,sys,os,useragent
reload(sys)
sys.setdefaultencoding('utf-8')
def clla(dr,ys):
    actions = ActionChains(driver)
    actions.move_to_element(ys)
def randomsleeps(ss,es):
    times=random.randint(ss,es)
    print 'I stop,and rest %s s '% times
    time.sleep(times)
def click(driver,ems,site):
    iii=0
    while iii == 0 :
        ydj=random.choice(ems)
        qu=ydj.get_attribute('href')
        if site in qu and 'leave' not in qu and 'img2' not in qu:
            js="var q=document.body.scrollTop=200"
            driver.execute_script(js)
            time.sleep(3)
            print 'I will click url of %s'%qu
            clla(driver,ydj)
            try :
                ydj.click()
                iii = 1
            except Exception,e:
                print 'chaging a url'
                iii = 0
    ss=stop_time-random.randint(-2,2)
    print '---- I will sleep %s s'%ss
    time.sleep(ss)
wds=open("usr/mkw.txt",'r').readlines()
f=open('usr/setting.ini','r').readline()
ws=eval(f)
site=ws["site"]
pn=int(ws["pn"])
pages=int(ws["pages"])-random.randint(-2,2)
firstdir=ws["firstdir"]
stop_time=int(ws["stop_time"])
kwnum=len(wds)
clnum=input(u'total num:%s,How manay kws do you want to click?'%kwnum)
current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
datetime=time.strftime('%Y%m%d')
ft="Mrank_data%s.txt"%datetime
if os.path.exists('usr/res/'+ft):
    exf=random.randint(10,1000)
    #print 'rename file'
    ft = 'new_%s_%s'%(exf,ft)
#print ft
fres=open('usr/mres/'+ft,'w')
#fres.write(current_date+':\n')
print "I will Start...\nI will check the rank of %s\nI have %s(in %s) keywords to check\nI will find %s pages\nI will see %s pages of site,first url:%s(0 is no limited)\nafter I sleep %s s , I go on"%(site,clnum,kwnum,pn,pages,firstdir,stop_time)

randomsleeps(5,10)
wdss=random.sample(wds,clnum)
random.shuffle(wdss)
desired_capabilities= webdriver.DesiredCapabilities.CHROME.copy()
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; lsv=globalTjs_97273d6-wwwTcss_8eba1c3-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_eabc62a-framejs_902a6d8-globalBjs_2d41ef9-sugjs_97bfd68-wwwjs_8d1160b; MSA_WH=1433_772; BAIDUID=E9B0B6A35D4ABC6ED4891FCC0FD085BD:FG=1; plus_cv=1::m:2a9fb36a; H_WISE_SIDS=107504_106305_100040_100100_109550_104341_107937_108437_109700_109794_107961_108453_109737_109558_109506_110022_107895_107917_109683_109588_110072_107318_107300_107242_100457; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; rsv_jmp_slow=1474644236473; sug=3; sugstore=1; ORIGIN=0; bdime=21110; H_PS_645EC=60efFRJ1dM8ial205oBcDuRmtLgH3Q6NaRzxDuIkbMkGVXNSHmXBfW0GZL4l5pnj; BD_UPN=123253; BD_CK_SAM=1; BDSVRTM=110; H_PS_PSSID=17947",
    #"Host":host,
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":"1"
}
for key, value in headers.iteritems():

    desired_capabilities['phantomjs.page.customHeaders.{}'.format(key)] = value

for index,wd in enumerate(wdss,1):
    try:
        ua=useragent.wapualist()
        #print ua
        desired_capabilities['phantomjs.page.customHeaders.User-Agent'] =ua
        print '---------UserAgent:%s'%ua
        wd=wd.strip()
        #print desired_capabilities
        driver=webdriver.PhantomJS(executable_path="usr\phantomjs\\bin\phantomjs.exe",desired_capabilities=desired_capabilities)  #调用chrome浏览器
        #driver.set_window_position(20, 40)
        driver.get('https://m.baidu.com/')
        elem = driver.find_element_by_id("index-kw")
        elem.send_keys(unicode(wd, "utf-8"))
        elem.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)
        randomsleeps(3,6)
        print driver.title
        if u"- 百度" not in driver.title:
            continue
            #print driver.page_source
        i1=0
        i2=0
        rk=0
        while i1<pn and i2==0 :
            print 'I will check No.%s page'%(i1+1)
            print driver.current_url
            surl=driver.find_elements_by_xpath("//span[@class='c-showurl']")
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
                try:
                    np=driver.find_element_by_xpath("//a[contains(@class,'new-nextpage')]")
                except :
                    continue
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
        ress='%s/%s、kw:%s,rank:%s,url:%s'%(index,clnum,wd,rk,driver.current_url)
        print ress
        fres.write(ress+'\n')
        #print driver.page_source
        if firstdir != '0':
            print firstdir,'is fd'
            qwe=driver.find_elements_by_xpath("//a[contains(@href,'%s')]"%firstdir)
        else :
            print 'no fd'
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
            print 'will click',i
            print driver.current_url
            handles = driver.window_handles
            for handle in handles:
                if driver.current_window_handle != handle:
                    driver.switch_to.window(handle)
            try:
                qqq=driver.find_elements_by_xpath("//a[contains(@href,'/')]")
                click(driver,qqq,site)
                i+=1
            except Exception,e:
                print 'there is a err,I will go on'
                i+=1
                randomsleeps(8,20)
        driver.switch_to.window(handles[0])
        driver.close()
        os.system('taskkill /f /im phantomjs.exe')

    except :
        print 'err.theNextWord'
        continue
fres.close()

print 'get all !'



