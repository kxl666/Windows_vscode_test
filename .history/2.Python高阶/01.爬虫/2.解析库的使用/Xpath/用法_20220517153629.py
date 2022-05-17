# 在三种解析库中 Xpath的解析速度最快
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="linkl.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
# 1.解析
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
# 调用tostring()方法即可输出修正后的HTML代码

# 2.xpath 获取所有节点
# html = etree.HTML('example.html')
# result = html.xpath('//*')
# print(result)

# 3.xpath 获取指定节点
html = etree.HTML('example.html')
result = html.xpath('//ul')
print(result)
