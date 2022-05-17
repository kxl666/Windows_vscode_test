# pyquery 的CSS选择器比 beautifulsoup更加强大
from pyquery import PyQuery as pq

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1">< a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class=bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="links.html">fifth item</a></li>
</ul>
</div>
'''
# 字符串初始化
# doc = pq(html)
# print(doc('li'))

# URL初始化
# doc = pq(url='http://cuiqingcai.com/')
# print(doc('title'))

# 文件初始化
# doc = pq(filename='r"C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\2.解析库的使用\Xpath\example.html"')
# print(doc('li'))
