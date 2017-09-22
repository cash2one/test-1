# -- coding: UTF-8 --
import lxml.etree as etree
import requests,urllib,urllib2
import sys,re,random,chardet,time
import socket,os
import useragent
socket.setdefaulttimeout(3)
reload(sys)
sys.setdefaultencoding('utf-8')
def search(req,html):
    text = re.search(req,html)
    if text:
        data = text.group(1)
    else:
        data = 'no'
    return data
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
def gettext(kw):
    def ismake(filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print 'file making'
    def errlog(kw,bf):
        with open('errfn.txt','a') as yc:
            yc.write(kw+'\terr:'+bf+'\n')
        yc.close()
    # program start
    s=kw.strip()
    ss='http://www.999mywine.com/search/'+s
    print ss
    try:
        html = getHTml(ss)
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
    except Exception,e:
        print '999 lose,err:',e
        errlog(s,'there is err')
        time.sleep(random.randint(10,20))
        return 0
    noresult = page.xpath("//div[@class='noresult']")
    if len(noresult) != 0:
        errlog(s,'num is 0')
        return 0
    else:
        pass
    bigitem = page.xpath("//table[@id='customers']")[0]
    miditem = bigitem.xpath("tbody/tr")
    totaln=len(miditem)
    if totaln == 1:
        randnl = [1]
    elif totaln>1 and totaln<=10:
        randnl = range(1,totaln)
    elif totaln > 10 and totaln <=25:
        clnn = range(1,totaln)
        crnum = random.randint(6,10)
        randnl = random.sample(clnn, crnum)
    else :
        clnn = range(1,25)
        crnum = random.randint(6,12)
        randnl = random.sample(clnn, crnum)
    global j
    j = 0
    gettext='<p>'+s.strip()+'价格表：</p>'
    getcon = ''
    for xx,item in enumerate(miditem,1):
        for xii in randnl:
            if xii == xx :
                j+=1
                title=item.xpath("td[1]/div/a/text()")[0]
                price=item.xpath("td[2]/text()")[0]
                cons = '<p>%s、%s\t价格：%s</p>'%(j,title,price)
                getcon+=cons
    if getcon=='':
        errlog(s,'gettext is null')
        return 0
    else:
        gettext+=getcon
    time.sleep(random.randint(4,9))
    return gettext
def getpic(kw):
#定义一个要提交的数据数组(字典)
    nstr=kw.strip()
    data = {}
    data['__VIEWSTATE'] = '/wEPDwULLTE1OTc1MDc1NThkZNkZd/JN5ZWaBbB/oA9edRnBrRni'
    data['__EVENTVALIDATION'] = '/wEWBQLOqfGMBALs0bLrBgL27ICIBAL37ICIBAKM54rGBmmifv+QoFfuoHNODth0o5bP3APY'
    data['TextBox1'] = nstr
    data['ddlList'] = '1'
    data['Button1'] = '搜索'

    #定义post的地址
    url = 'http://www.19888.tv/tools/searchbizandpro.aspx'
    post_data = urllib.urlencode(data)

    #提交，发送数据
    try:
        req = urllib2.urlopen(url, post_data)
        content = req.read()
        page = etree.HTML(content.lower().decode("utf-8", "replace"))
        if page.xpath("//table[1]/tr") >1:
            result = page.xpath("//table[1]")[0]
        elif page.xpath("//table[2]/tr"):
            result = page.xpath("//table[2]")[0]
        else:
            return 0
        #        with open('date','w') as f:
        #         	f.write(content)
        #        f.close()
        lnumb=random.choice(range(1,4))
        lll=result.xpath('tr/td[3]/text()')[lnumb]
        #print 'Suc!',kw,lll
    except Exception,e:
        print 'pic',nstr,e
        return 0
    return 'http://img2.19888.tv'+lll

def getrelate(kw):
    kw=kw.strip()
    url='http://www.19888.tv/tools/NewsSearch.aspx?id=0&title='+kw
    print url
    try:
        html =getHTml(url)
        page = etree.HTML(html.lower().decode("utf-8", "replace"))
    except Exception,e:
        print 'spzs getnews lose,err:',e
        time.sleep(random.randint(4,9))
        return 0
    results = page.xpath("//div[3]/ul/li")
    if len(results) == 0:
        print 'no related'
        return 0
    else:
        lista=results[0:4]
        listhref=''
        for l in lista:
            k=l.xpath("a/@href")[0]
            v=l.xpath("a/text()")[0]
            kv='<p><a href="%s">%s</a></p>'%(k,v)
            listhref+=kv
            #print len(listdict)
    return listhref

#print getrelate('劲酒')
