# -*- coding: utf-8
import urllib2

#爬取网页
response = urllib2.urlopen('http://fanyi.youdao.com')
html = response.read()

#写入文件
f = open('youdao.html','w')
f.write(html)
f.close()



