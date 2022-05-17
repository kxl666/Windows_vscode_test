# 在三种解析库中 Xpath的解析速度最快
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
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
parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse(
    r"C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\2.解析库的使用\Xpath\example.html",
    parser=parser)
# result = html.xpath('//li')
# print(result)

# 4.xpath 获取指定节点的属性
# result = html.xpath('//li/@class')
# result = html.xpath('//li/a/@href')
# print(result)

# 5.xpath 获取指定节点的文本, （子节点）
# result = html.xpath('//li/a/text()')
# print(result)

# 6.xpath 父节点
result = html.xpath('//a[@href="link4.html"] I .. /@class’) 

