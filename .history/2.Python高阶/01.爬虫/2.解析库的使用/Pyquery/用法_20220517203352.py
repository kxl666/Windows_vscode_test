# pyquery 的CSS选择器比 beautifulsoup更加强大
from pyquery import PyQuery as pq

html = '''
<div>
<ul>
<li class="item-0">first item<lli>
<li class="item-1">< a hre干＝＂ link2.html ”＞ eco nd item</a><lli>
<li class="item-0 active"><a href="link3.html"><span class ＝咄old ”＞ third item</span></a><lli>
<li class =“ item-1 active"><a href="link4 . html">fourth item</a><lli>
<li class="item －。”＞＜ href="links . html”>fifth item</a><lli>
</ul>
</div>
'''
# 字符串初始化
doc = pq(html)
