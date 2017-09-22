#coding:utf-8
import requests,re,time,sys,json,datetime,random,threading
from lxml import etree
import useragent
reload(sys)
sys.setdefaultencoding('utf8')
def randomsleeps(ss,es):
    times=random.randint(ss,es)
    time.sleep(times)
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
#采集下拉
def get_sug(word):
    print  'the thread name is:%s   time:%s ' % (threading.currentThread().getName(),time.ctime())
    print '-----%s的下拉：'%(word)
    current_milli_time = int(round(time.time() * 1000))
    url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=%s&sugmode=2&json=1&p=3&sid=1427_21091_21673_22581&req=2&pbs=%%E5%%BF%%AB%%E6%%89%%8B&csor=2&pwd=%%E5%%BF%%AB%%E6%%89%%8B&cb=jQuery11020924966752020363_1498055470768&_=%s' % (word,current_milli_time)
    cont = getHTml(url)
    res = cont[41: -2].decode('gbk')  # 只取返回结果中json格式一段，并且解码为unicode
    res_json = json.loads(res)  # json格式转换
    js=res_json['s'] # 返回关键词列表
    wd=[]
    for w in js:
        wd.append(w+' xlroot:'+word)
    print '\n'.join(wd)
#采集相关
def append_list(l1, l2):
    '''
     一个辅助函数，作用是将一个列表合并到已知列表，并剔除已存在的元素
     '''
    for l in l2:
        if l not in l1:
            l1.append(l)
    return l1

def relatewords(word):
    '''
     主体函数
     '''
    print  'the thread name is:%s   time:%s ' % (threading.currentThread().getName(),time.ctime())
    print '-----%s的相关：'%(word)
    url = 'http://www.baidu.com/s?wd=%s' % word
    html=getHTml(url)
    #print html
    tree = etree.HTML(html)
    divrs = tree.xpath('//div[@id="rs"]/table/tr/th')  # 通过xpath路径提取元素
    rsword=[]
    for div in divrs:
        wor=div.xpath('a/text()')[0]
        rsword.append(wor+' xgroot:'+word)
    time.sleep(3)  # 等待3秒，防屏蔽
    print '\n'.join(rsword)
    return rsword

w=['酒','白酒','啤酒代理']

for i in w:
    threads = []
    t1 = threading.Thread(target=get_sug,args=(i,))
    threads.append(t1)
    t2 = threading.Thread(target=relatewords,args=(i,))
    threads.append(t2)
    randomsleeps(4,7)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
'''
relatewords('酒')
get_sug('白酒')
'''
print "all over %s" %time.ctime()
