# -*- coding: utf-8

# from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
from bs4 import BeautifulSoup

html = '''
<div class="tqshow1"><h3>苏州<font color="#0066cc">今日</font>天气</h3><p><font color="green">星期日</font></p><ul><li class="tqpng"><img align="absmiddle" class="pngtqico" style="border: 0px currentColor; width: 46px; height: 46px;" src="http://img.tianqi.com/static/images/tianqibig/b8.png"></li><li><font color="#f00">25℃</font>~<font color="#4899be">22℃</font></li><li>中雨</li><li style="height: 18px; overflow: hidden;">东北风 1级</li></ul></div>
<div class="tqshow1"><h3>苏州<font color="red">明日</font>天气</h3><p>星期一</p><ul><li class="tqpng"><img align="absmiddle" class="pngtqico" style="border: 0px currentColor; width: 46px; height: 46px;" src="http://img.tianqi.com/static/images/tianqibig/b8.png"></li><li><font color="#f00">26℃</font>~<font color="#4899be">23℃</font></li><li>中雨</li><li style="height: 18px; overflow: hidden;">东南风 3-4级</li></ul></div>
<div class="tqshow1"><h3>苏州<font color="red">后天</font>天气</h3><p>星期二</p><ul><li class="tqpng"><img align="absmiddle" class="pngtqico" style="border: 0px currentColor; width: 46px; height: 46px;" src="http://img.tianqi.com/static/images/tianqibig/b3.png"></li><li><font color="#f00">29℃</font>~<font color="#4899be">25℃</font></li><li>阵雨</li><li style="height: 18px; overflow: hidden;">西北风 3-4级</li></ul></div>
'''

soup = BeautifulSoup(html,"lxml")
for div in soup.find_all('div'):
    print soup.h3.get_text()
    print  soup.p.string
    print  soup.find_all("li")[1].get_text()
    print  soup.find_all("li")[2].string
    print  soup.find_all("li")[3].string
    print soup.find_all("li")[0].img['src']
    print '\n'


