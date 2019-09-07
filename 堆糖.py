import urllib.request
import re
from 百度 import *
from 网页滚动 import *


def sugar(name = '雷姆',file='rem'):
    file_name = 'C:\\Users\\Joker Wang'+('\\'+file)
    os.mkdir(file_name)
    os.chdir(file_name)
    keyword = urllib.parse.quote(name)
    for x in range(29):
     url ='https://www.duitang.com/search/?kw='+keyword+'&type=feed#!s-p'+str(x)
     b = rollnet(url)
     c = re.findall('href="(/blog/\?id=.+?)"',b)
     d = []
     for i in range(len(c)):
        g = 'https://www.duitang.com' + c[i]
        e = visit(g)
        f = translate(e)
        h = re.findall('"vieworg" href="(.+?)"',f)
        print(h[0])
        k = x*1000+i
        save(h[0],str(k),name)
    
