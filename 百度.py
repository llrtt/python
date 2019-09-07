import os
import urllib.request
import re
import random
import urllib

def IP():
    ip=['182.92.11.84:1080']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(ip)})
    print('llll')
    opener=urllib.request.build_opener(proxy_support)
    print('llll')
    opener.addheaders=[{'User-Agent','Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}]
    print('llll')
    urllib.request.install_opener(opener)
    print('llll')
    x=urllib.request.urlopen(url)
    print('llll')
    return x

def visit(url):
    a=urllib.request.Request(url)
    a.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')
    x=urllib.request.urlopen(a)
    return x

def save(url,i,name):
    g=visit(url).read()
    with open(name+i+'.jpg','wb') as f:
        f.write(g)

def translate(html):
    llrt=html.read().decode('utf-8','ignore')
    return llrt

def search(name='雷姆',file='rem'):
    a = 'C:\\Users\\Joker Wang\\Desktop'+('\\'+file)
    os.mkdir(a)
    os.chdir(a)
    keyword = name
    keyword = urllib.parse.quote(keyword)
    url='https://image.baidu.com/search/flip?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&ps=1&pv=&fm=rs1&word='+keyword+'&oriquery=saber&ofr=saber&sensitive=0'
    h=visit(url)
    k=translate(h)
    llrt=re.findall(r'"pageNum":..+?"objURL":"(.+?)",',k)
    print(llrt)
    for i in range(len(llrt)):
     try:
        save(llrt[i],str(i+100),name)
        print(llrt[i])
     except:
         print('error')
         continue
          

              
