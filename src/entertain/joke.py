#coding=utf-8
import urllib.request
import gzip
import random
import re

def webresource():
    page=random.randint(0,10000)%20
    url='http://www.qiushibaike.com/textnew/page/'+str(page)+'/'
    aheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept':'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip',
            'Connection':'close'
            }    
    
    req=urllib.request.Request(url,headers=aheader)
    webdata=urllib.request.urlopen(req)
    fin=gzip.decompress(webdata.read()).decode('UTF-8')
    if not fin:
        print('Failure')
    else:
        return fin
    
def getjoke():
    res=webresource()
    sda=res.replace('<br/>','\n').split('\n')
    pat1=re.compile(r'^<div.*class="content".{,3}')
    pat2=re.compile(r'[0-9]{10}')
    flag=False
    data=[]
    num=0
    tem=''
    for wo in sda:
        #global sum
        if flag:
            #data.append(wo)
            #sum+=1
            searchres=pat2.search(wo)
            if searchres:
                data.append(tem)
                num+=1
                tem=''
            if not searchres:    
                tem+=wo  
            #print(wo)
        
        if pat1.search(wo):
            flag=True
        
        if pat2.search(wo):
            #break
            flag=False
    luckynum=random.randint(0,num-1)
    print(data[luckynum])        
 
def output():
    getjoke()
     
if __name__=='__main__':
    try:
        output()
    except Exception as e:
        try:
            output()
        except Exception as e:
            print('Sir, you seem have some problem with your network, try again later.')