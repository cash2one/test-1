# -- coding: UTF-8 --
import lxml.etree as etree
import requests,urllib,urllib2
import sys,re,random,chardet,time
import socket,os,json
import useragent
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')
'''
getContent:来自百度搜索
getnews:来自百度新闻
getbdsite:传入相关网站，搜索该网站在百度中的相关关键词收录信息
getzh:来源知乎
'''
def search(req,html):
    text = re.search(req,html)
    if text:
        data = text.group(1)
    else:
        data = 'no'
    return data
def errlog(kw,bf):
    with open('errfn.txt','a') as yc:
        yc.write(kw+'\terr:'+bf+'\n')
    yc.close()
def randomsleeps(ss,es):
    times=random.randint(ss,es)
    time.sleep(times)
def getHTml(url):
    host = search('^([^/]*?)/',re.sub(r'(https|http)://','',url))
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        #"Cookie":"__cfduid=df26a7c536a0301ccf36481a14f53b4a81469608715; BIDUPSID=E9B0B6A35D4ABC6ED4891FCC0FD085BD; PSTM=1474352745; lsv=globalTjs_97273d6-wwwTcss_8eba1c3-routejs_6ede3cf-activityControllerjs_b6f8c66-wwwBcss_eabc62a-framejs_902a6d8-globalBjs_2d41ef9-sugjs_97bfd68-wwwjs_8d1160b; MSA_WH=1433_772; BAIDUID=E9B0B6A35D4ABC6ED4891FCC0FD085BD:FG=1; plus_cv=1::m:2a9fb36a; H_WISE_SIDS=107504_106305_100040_100100_109550_104341_107937_108437_109700_109794_107961_108453_109737_109558_109506_110022_107895_107917_109683_109588_110072_107318_107300_107242_100457; BDUSS=XNNMTJlWEdDdzFPdU1nSzVEZ1REYn4tNWNwZk94NVducXpaaThjWjE4bU1TQXRZQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIy741eMu-NXQ; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BDRCVFR[C0p6oIjvx-c]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; rsv_jmp_slow=1474644236473; sug=3; sugstore=1; ORIGIN=0; bdime=21110; H_PS_645EC=60efFRJ1dM8ial205oBcDuRmtLgH3Q6NaRzxDuIkbMkGVXNSHmXBfW0GZL4l5pnj; BD_UPN=123253; BD_CK_SAM=1; BDSVRTM=110; H_PS_PSSID=17947",
        "Host":host,
        "Pragma":"no-cache",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":useragent.pcualist()
    }
    html = requests.get(url,headers=headers,timeout=30)
    code = html.encoding

    return html.content
def getnews(kw):
    ss='http://news.baidu.com/ns?word=%s&tn=news&from=news&cl=2&rn=20&ct=1'%kw.strip()
    try:
        html = getHTml(ss)
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
    except Exception,e:
        print '999 lose,err:',e
        errlog(kw.strip(),'there is err')
        time.sleep(random.randint(10,20))
        return 0
    hresult = page.xpath("//div[@class='result']")
    print len(hresult)
    if len(hresult) == 0:
        errlog(kw.strip(),'num is 0')
        return 0
    else:
        pass
    for x,item in enumerate(hresult,1):
        _title=item.xpath("h3/a")[0]
        _url=item.xpath("h3/a/@href")[0]
        title=_title.xpath('string(.)')
        _des=item.xpath("div")[0]
        des=_des.xpath('string(.)')
        print title
        print _url
        print des.strip()
        print '------'
    return 1
def getContent(word,sopage):
    global ysr
    srpage=str(sopage)+str(0)
    pcurl = 'http://www.baidu.com/s?q=&tn=json&ct=2097152&si=&ie=utf-8&cl=3&wd=%s&rn=%s' % (word,srpage)
    print pcurl
    #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ start crawl %s @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' % word
    html = getHTml(pcurl)

    html_dict = json.loads(html)
    for tag in html_dict['feed']['entry']:
        if tag.has_key('title'):
            title = tag['title']
            url = tag['url']
            abs = tag['abs']
            print title,url,abs

    return 1
def getbdsite(word,site,sopage):
    global ysr
    srpage=str(sopage)+str(0)
    pcurl = 'http://www.baidu.com/s?q=&tn=json&ct=2097152&si=&ie=utf-8&cl=3&wd=%s site:%s&rn=%s' % (word,site,srpage)
    print pcurl
    #print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ start crawl %s @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' % word
    html = getHTml(pcurl)

    html_dict = json.loads(html)
    for tag in html_dict['feed']['entry']:
        if tag.has_key('title'):
            title = tag['title']
            url = tag['url']
            abs = tag['abs']
            print title,url,abs

    return 1
def getzh(kw):
    ss='http://zhihu.sogou.com/zhihu?query=%s'%kw.strip()
    try:
        html = getHTml(ss)
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
    except Exception,e:
        print '999 lose,err:',e
        errlog(kw.strip(),'there is err')
        time.sleep(random.randint(10,20))
        return 0
    hresult = page.xpath("//div[@class='result-about-list']")
    print len(hresult)
    if len(hresult) == 0:
        errlog(kw.strip(),'num is 0')
        return 0
    else:
        pass
    for x,item in enumerate(hresult,1):
        _title=item.xpath("h4/a")[0]
        _url=item.xpath("h4/a/@href")[0]
        title=_title.xpath('string(.)')
        _des=item.xpath("div/p")[0]
        des=_des.xpath('string(.)')
        print title
        print _url
        print des.strip()
        print '------'
    return 1
getzh('茅台')