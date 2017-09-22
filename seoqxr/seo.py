# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)]
# Embedded file name: seoqx.py
# Compiled at: 2014-05-06 13:56:30
import pycurl
import StringIO
import urllib
import re
import datetime
import time
import os
import sys
import inspect
import random
import json
serp_area_reg = re.compile('<div class="result .+?>([\\s\\S]*?)</div>\\s*?</div>')
serp_url_reg = re.compile('style="text-decoration:none;">(.+?)&nbsp;')
VISITS_LOG_PATH = '/data/visits_log/'
RANK_SCORE = [
 2.856,
 1.923,
 1.02,
 0.814,
 0.75,
 0.572,
 0.401,
 0.441,
 0.553,
 0.67]
PATH = os.path.abspath(os.path.dirname(inspect.stack()[1][1]))

class dict_plus(dict):

    def sort(self, reverse=True):
        return sorted(self.iteritems(), key=lambda d: d[1], reverse=reverse)

    def add(self, key, value=1):
        self[key] = self.get(key, 0) + value


def root_domain(url):
    try:
        url = url.replace('http://', '')
        l = ['.com.cn', '.org.cn', '.net.cn', '.gov.cn']
        for suffix in l:
            if suffix in url:
                return re.search('^.*?([^.]+?\\.[^.]+?\\.[^.]+?)/', url).group(1)

        return re.search('^.*?([^.]+?\\.[^.]+?)/', url).group(1)
    except:
        return '-'


def log_file(date):
    s = '%s_' % date
    for f in os.listdir(VISITS_LOG_PATH):
        if s in f:
            count = int(f[f[3:].find('_') + 4:f.find('.')])
            f = '%s%s' % (VISITS_LOG_PATH, f)
            return (
             f, count)

    return False


def curl(url, debug=False, **kwargs):
    while 1:
        try:
            s = StringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, url)
            c.setopt(pycurl.REFERER, url)
            c.setopt(pycurl.FOLLOWLOCATION, True)
            c.setopt(pycurl.TIMEOUT, 60)
            c.setopt(pycurl.ENCODING, 'gzip')
            c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
            c.setopt(pycurl.NOSIGNAL, True)
            c.setopt(pycurl.WRITEFUNCTION, s.write)
            for k, v in kwargs.iteritems():
                c.setopt(vars(pycurl)[k], v)

            c.perform()
            c.close()
            return s.getvalue()
        except:
            if debug:
                raise
            continue


def baidu_serp(kw, rn=100, pn=0):
    """\xe8\x8e\xb7\xe5\x8f\x96SERP\xe6\xba\x90\xe4\xbb\xa3\xe7\xa0\x81"""
    kw = urllib.quote_plus(kw)
    while 1:
        html = curl('http://www.baidu.com/s?wd=%s&rn=%d&pn=%d' % (kw, rn, pn))
        if '<img src="http://verify.baidu.com/' in html:
            print 'captcha'
            time.sleep(600)
            continue
        else:
            break

    return html


def baidu_serp_urls(kw, rn=100, pn=0):
    """\xe8\x8e\xb7\xe5\x8f\x96SERP\xe4\xb8\x8a\xe7\x9a\x84\xe6\x89\x80\xe6\x9c\x89URL"""
    urls = []
    html = baidu_serp(kw, rn, pn)
    #print html
    areas = re.findall(serp_area_reg, html)
    for area in areas:
        #print area
        m = re.search(serp_url_reg, area)
        if m:
            url = m.group(1)
            url = url.replace('<b>', '').replace('</b>', '')
            url = 'http://' + url
        else:
            url = '-'
        urls.append(url)

    return urls


def baidu_rank(kw, host=None, lp=None, rn=100, pn=0):
    """\xe6\x8c\x87\xe5\xae\x9a\xe5\x9f\x9f\xe5\x90\x8d\xef\xbc\x88\xe6\x88\x96\xe5\x85\xb6\xe5\xae\x83\xe7\x89\xb9\xe5\xbe\x81\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xef\xbc\x89\xef\xbc\x8c\xe8\xbf\x94\xe5\x9b\x9e\xe6\x8e\x92\xe5\x90\x8d\xe4\xb8\x8e\xe7\x9d\x80\xe9\x99\x86\xe9\xa1\xb5
    \xe6\x88\x96
    \xe6\x8c\x87\xe5\xae\x9a\xe7\x9d\x80\xe9\x99\x86\xe9\xa1\xb5\xef\xbc\x8c\xe8\xbf\x94\xe5\x9b\x9e\xe6\x8e\x92\xe5\x90\x8d
    \xe5\x9b\xa0\xe4\xb8\xbaURL\xe4\xb8\xad\xe5\x8f\xaf\xe8\x83\xbd\xe5\x8c\x85\xe5\x90\xab...\xef\xbc\x8c\xe6\xad\xa4\xe6\x97\xb6\xe6\x97\xa0\xe6\xb3\x95\xe5\xae\x9a\xe4\xbd\x8d\xe5\x88\xb0URL\xe6\x9c\xac\xe4\xbd\x93\xef\xbc\x8c\xe6\x9c\x89\xe6\x9e\x81\xe5\xb0\x8f\xe5\x8f\xaf\xe8\x83\xbd\xe6\x80\xa7\xe4\xbc\x9a\xe5\xaf\xbc\xe8\x87\xb4\xe6\x8e\x92\xe5\x90\x8d\xe4\xb8\x8d\xe5\x87\x86\xe7\xa1\xae
    """
    if not host and not lp:
        return False
    urls = baidu_serp_urls(kw, rn, pn)
    if host:
        for pos, url in enumerate(urls, 1):
            if host in url:
                return (pos, url)

        return (-1, '-')
    if lp:
        for pos, url in enumerate(urls, 1):
            if '...' not in url:
                if lp == url:
                    return pos
            else:
                start, end = url.split('...')
                if lp.startswith(start) and lp.endswith(end):
                    return pos

        return -1


def baidu_index(url):
    html = baidu_serp(url)
    if '<div class="hit_top_new  res-border-bottom">' in html:
        return 0
    else:
        return 1


def date_range(start, end, only_monday=False, input_format='%y%m%d', output_format='%y%m%d'):
    """\xe5\xa6\x82print date_range(140130, 140202)
    \xe8\xbe\x93\xe5\x87\xba['140130', '140131', '140201', '140202']
    """
    start = str(start)
    end = str(end)
    start = datetime.datetime.strptime(start, input_format)
    end = datetime.datetime.strptime(end, input_format)
    one_day = datetime.timedelta(days=1)
    range_ = []
    d = start - one_day
    while 1:
        d = d + one_day
        if d > end:
            break
        if only_monday and d.strftime('%w') != '1':
            continue
        range_.append(datetime.datetime.strftime(d, output_format))

    return range_


def from_today(delta, output_format='%y%m%d'):
    today = datetime.datetime.today()
    delta = datetime.timedelta(days=delta)
    today += delta
    return datetime.datetime.strftime(today, output_format)


def date_format(date, input_format='%y%m%d', output_format='%Y-%m-%d'):
    date = str(date)
    date = datetime.datetime.strptime(date, input_format)
    return datetime.datetime.strftime(date, output_format)


def unix_timestamp(date, input_format='%y%m%d'):
    date = datetime.datetime.strptime(date, input_format)
    return date.timestamp()

