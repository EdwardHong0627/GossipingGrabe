#-*- coding:utf-8 -*-
import sys
import requests
import time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def Filter(S1):
    if(S1.find('Re:')==-1):
        if(S1.find('[新聞]')!=-1):
            return True
        else:
            return False
    else:
        return False
agree={
'from':'/bbs/Gossiping/index.html',
'yes':'yes'
}
rs=requests.session()
res=rs.post('https://www.ptt.cc/ask/over18',verify=False, data=agree)
i=1
for R in range(10363,10358,-1):
    res=rs.get('https://www.ptt.cc/bbs/Gossiping/index'+str(R)+'.html',verify=False)
#res=rs.get('https://www.ptt.cc/bbs/Gossiping/index10363.html',verify=False)
    soup=BeautifulSoup(res.text,'html.parser')
    for entry  in soup.select('.r-ent'):
        for link in entry.find_all('a'):
            if Filter(link.text):
                url='https://www.ptt.cc/'+link.get('href')
                Grab=open('Gossiping/'+str(i)+'.txt','w')
                time.sleep(3)
                content=rs.post('https://www.ptt.cc/ask/over18',verify=False,data=agree)
                content=rs.get(url,verify=False)
                fil=BeautifulSoup(content.text,'html.parser')
                S=str(fil.text)
                j=S.find('作者')
                k=S.find('--')
                Grab.write(S[j:k])
                Grab.close()
                i+=1
