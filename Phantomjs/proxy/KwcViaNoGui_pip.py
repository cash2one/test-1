#!/usr/bin/env python
#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import time,random,sys,os,useragent,proxyip

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
        if site in qu and 'img2.' not in qu and 'UPLOADFILES' not in qu:
            js="var q=document.body.scrollTop=200"
            driver.execute_script(js)
            time.sleep(3)
            print '-------------------I will click url of %s'%qu
            clla(driver,ydj)
            try :
                ydj.click()
                iii = 1
            except Exception,e:
                print '---chaging......'
                iii = 0
    ss=stop_time-random.randint(-2,2)
    print '---- I will sleep %s s'%ss
    time.sleep(ss)

def screenshot():
    ct=time.strftime('%Y%m%d%H%M%S')
    driver.save_screenshot('usr/screenshot/%s.png'%ct)
    print '-----screenshot_save success:usr/screenshot/%s.png'%ct
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

for index,wd in enumerate(wds,1):
        ua=useragent.pcualist()
        #print ua
        desired_capabilities['phantomjs.page.customHeaders.User-Agent'] =ua
        print '---------UserAgent:%s'%ua
        wd=wd.strip()
        #print desired_capabilities
        driver=webdriver.PhantomJS(executable_path="usr\phantomjs\\bin\phantomjs.exe",desired_capabilities=desired_capabilities)  #调用chrome浏览器
        #driver.set_window_position(20, 40)
        # 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
        proxy=webdriver.Proxy()
        proxy.proxy_type=ProxyType.MANUAL
        proxy.http_proxy=proxyip.getip()
        # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
        proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
        print('1: ',driver.session_id)
        print('2: ',driver.page_source)
        print('3: ',driver.get_cookies())

        driver.maximize_window()
        driver.get('https://www.baidu.com/')
        elem = driver.find_element_by_id("kw")
        elem.send_keys(unicode(wd, "utf-8"))
        elem.send_keys(Keys.RETURN)
        #driver.implicitly_wait(5)
        randomsleeps(3,6)
        print driver.title
        if u"_百度搜索" not in driver.title:
            continue
        #print driver.page_source
        i1=0
        i2=0
        rk=0
        while i1<pn and i2==0 :
            print '--I will check No.%s page'%(i1+1)
            print driver.current_url
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
            print '%s/%s、kw:%s,no rand'%(index,kwnum,wd)
            fres.write('%s,no rand\n'%wd)
            continue
        time.sleep(stop_time)
        randomsleeps(7,13)
        handles = driver.window_handles
        for handle in handles:
            if driver.current_window_handle != handle:
                driver.switch_to.window(handle)
        ress='--------%s/%s、kw:%s,rank:%s,url:%s'%(index,kwnum,wd,rk,driver.current_url)
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
        screenshot()
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
                print 'there is a err,U will go on'
                i+=1
                randomsleeps(8,20)
        driver.switch_to.window(handles[0])
        driver.close()
        os.system('taskkill /f /im Phantomjs.exe')
fres.close()
print '[finish all!]'
