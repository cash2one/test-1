#!/usr/bin/env python
#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys,proxyip,os
reload(sys)
sys.setdefaultencoding('utf-8')

tip=proxyip.getip()
print tip
proxy = Proxy(
        {
        'proxyType': ProxyType.MANUAL,
        'httpProxy':tip  # 代理ip和端口
    }
)
# 新建一个“期望的技能”，哈哈
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
# 把代理ip加入到技能中
proxy.add_to_capabilities(desired_capabilities)
driver = webdriver.PhantomJS(
    executable_path="usr\phantomjs\\bin\phantomjs.exe",
    desired_capabilities=desired_capabilities
)
print desired_capabilities
driver.get('http://www.360jizhang.com')
print('1: ',driver.session_id)
print('2: ',driver.page_source)
print('3: ',driver.get_cookies())
driver.close()

os.system('taskkill /f /im Phantomjs.exe')
