# 在三种解析库中 Xpath的解析速度最快
from lxml import etree

text = '''
<div>
<ul>
<li class="item-O"><a href=”linkl. html”>first item</a><lli>
<li class=” item-1”>< a href=”link2.html”> second item</a><lli>
<li class=” item-inactive” >< a href="link3.html”>third item</ a></h>
<li class=” item-1 ”><a href="link4.html'’>fourth item</a><lli> 
'''