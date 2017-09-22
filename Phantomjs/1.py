#encoding=utf8
import urllib,urllib2,time,useragent
import BeautifulSoup
import winpexpect
import socket,sys,random,os
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(3)

def getip():
    #get proxy ip
    User_Agent = useragent.pcualist()
    header = {}
    header['User-Agent'] = User_Agent
    url = 'http://www.xicidaili.com/nt/'
    req = urllib2.Request(url,headers=header)
    res = urllib2.urlopen(req).read()

    soup = BeautifulSoup.BeautifulSoup(res)
    ips = soup.findAll('tr')
    f1 = open("proxy/proxy","w")
    ipitems=[]
    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ipis=tds[1].contents[0]+":"+tds[2].contents[0]
        proxy_host = "http://"+ipis
        proxy_temp = {"http":proxy_host}
        #print proxy_host,proxy_temp
        url = "http://ip.chinaz.com/getip.aspx"
        try:
            res = urllib.urlopen(url,proxies=proxy_temp).read()
            print 'YY',proxy_temp
            ipitems.append(ipis)
        except Exception,e:
            print 'NN',proxy_temp
            time.sleep(5)
            continue

    return ipitems

#print getip()



ip_items=getip()
for ip in ip_items:
    print ip




