#!/usr/bin/env python
#encoding: utf-8
from selenium import webdriver
import time,random,sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
def randomsleeps(ss,es):
    times=random.randint(ss,es)
    print 'I stop,and rest %s s '% times
    time.sleep(times)

#wds=[['7241505900042','rHL4gu'],['7041505900042','Z2BLfk'],['6441505900042','V4t3Xq'],['4681505900042','KcdQ97'],['1121505900042','6lBdwk'],['5211505900042','rKj376'],['8961505900042','3RRp60']]
#读取关键词,kw一行一个
#passport = '1094691457@qq.com' #帐号
#password = 'tian530329554.' #密码
wds=open('user.txt','r').readlines()
for li in wds:
    #print li
    i=li.strip().split(',')
    passport =i[0]
    password =i[1]
    #print passport,password
    driver=webdriver.Chrome('Chrome\Application\chromedriver.exe')  #调用chrome浏览器
    driver.set_window_position(0,0)
    driver.set_window_size(1000, 250)
    driver.get('https://account.youku.com/')
    elem = driver.find_element_by_id("YT-ytaccount")
    elem.send_keys(unicode(passport, "utf-8"))
    elem2 = driver.find_element_by_id("YT-ytpassword")
    elem2.send_keys(unicode(password, "utf-8"))
    driver.find_element_by_id('YT-nloginSubmit').click()
    #driver.implicitly_wait(5)
    print '---------title:',driver.title
    randomsleeps(3,6)
    if u'用户登录' in driver.title:
        tiperr = driver.find_element_by_class_name("YT-errtips-box").text
        print u'%s，退出 %s-%s'%(tiperr,passport,password)
        driver.close()
    elif u'优酷首页' in driver.title:
        print u'-----------------------帐号可用！%s-%s'%(passport,password)
    else:
        print driver.title
    os.system('taskkill /f /im chromedriver.exe')

    #print driver.page_source
