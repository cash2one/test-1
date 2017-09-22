#!/usr/bin/env python
#encoding: utf-8
import urllib,urllib2,requests,useragent,sys,re
import lxml.etree as etree
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
    s=kw.strip()
    ss='http://tools.aizhan.com/api/ret/?sheng=none&shi=none&shou=baidu&ci=%s&yu=www.19888.tv&id=&t=0&callback=jQuery19106213087339841434_1505287085633&_=1505287085634'%s
    #print ss
    html = getHTml(ss)
    print html
    json_html = html.json()
    query_url = json_html['feed']

    return 1

gettext('葡萄酒')