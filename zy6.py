# -*- coding: utf-8

# import urllib
# import urllib2


# url = 'http://fanyi.youdao.com'
# values = {'i':'hello'}
# data = urllib.urlenconde(values)
# req = urllib2.Request(url,data)
# response = urllib2.urlopen(req)
# the_page= response.read()
#
# print the_page

import urllib
import urllib2
url = 'http://fanyi.youdao.com'
values = {'i' : 'hello'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
