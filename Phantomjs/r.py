#-*- coding: utf-8 -*-

#尝试用正则过滤UA中的信息

import re
import useragent

#测试用数据


IE = re.compile('(?<=MSIE\s)\d+\.\d+')
Windows = re.compile('(?<=Windows\s)[^;)]+')
Chrome = re.compile('(?<=Chrome/)\d+\.\d+')


def test(uaStr):
  m = Windows.search(uaStr)
  if m:
    print('Windows',m.group())
  m = IE.search(uaStr)
  if m:
    print('IE',m.group())
  m = Chrome.search(uaStr)
  if m:
    print('Chrome',m.group())
  print(uaStr)


for i in range(10):
    test(useragent.pcualist())
