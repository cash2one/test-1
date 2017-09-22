# -*- coding: utf-8 -*-
from seo import *
'''
baidu_rank(kw, host=None, lp=None, rn=100, pn=0)
查询百度关键词排名
指定某个域名，或是精确到某个着陆页
默认查询前100名，也可以通过设置rn, pn参数来遍历760个结果，或只查前10名
若查询过程中出现验证码，会自动间隔10分钟再次尝试查询
'''
reload(sys)
sys.setdefaultencoding('utf-8')
print baidu_rank('白酒招商', host='.19888.tv')
# 输出： (8, 'http://bj.ganji.com/zhaopin/')
print baidu_rank('招聘', lp='http://www.ganji.com/zhaopin/')
# 输出： 47
'''
baidu_index(url)
查询网页是否被百度收录
输出1为被收录，0为没有收录
若查询过程中出现验证码，会自动间隔10分钟再次尝试查询
'''
print baidu_index('http://bj.ganji.com/zhaopin/')
# 输出： 1
print baidu_index('http://bjbj.ganji.com/zhaopin/')
# 输出： 0
'''
root_domain(url)
通过URL获取根域名
'''
print root_domain('http://www.xxx.com.cn/sdfsfsf.html')
# 输出： xxx.com.cn