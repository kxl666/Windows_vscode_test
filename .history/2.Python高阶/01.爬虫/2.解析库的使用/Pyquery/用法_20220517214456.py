# pyquery 的CSS选择器比 beautifulsoup更加强大

from pyquery import PyQuery as pq

html = '''
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
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
# doc = pq(
#     filename=
#     r"C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\2.解析库的使用\Xpath\example.html"
# )
# print(doc('li'))

# 1.css选择器
# doc = pq(html)
# print(doc('#container .list li')) # 有空格递进关系

# 2.find查找子孙节点,children()查找子节点
# doc = pq(html)
# items = doc('.list')
# print(items)
# lis = items.find('li')
# print(lis)
# lis = items.children()
# print(lis)
# lis = items.children('.active')  # 只查找子节点中的active
# print(lis)

# 3.父节点/祖先节点
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(container)
# container = items.parents('#container')
# print(container)

# 4.兄弟节点 属性.属性 表示同级中与的关系,而隔开就是递进关系
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())

# 5.遍历
# doc = pq(html)
# lis = doc('li').items()
# for li in lis:
#     print(li)

# 6.获取属性,以下两种方式等价
doc = pq(html)
# li = doc('.item-0.active a')
# print(li.attr('href'))
# print(li.attr.href)
print(doc('li[class=item-0]').text())

# 7.获取文本
# doc = pq(html)
# li = doc('.item-0.active a')
# print(li.text())

# 8.获取html
# doc = pq(html)
# li = doc('.item-0.active a')
# print(li.html())

# 9.节点操作,它们和 jQuery的用法完全一致
# doc = pq(html)
# li = doc('.item-0.active')
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

# 9.1.添加节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.append('<li>append item</li>')
# print(li)

# 9.2.删除节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.remove()
# print(li)

# 9.3.替换节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.replaceWith('<li>replace item</li>')
# print(li)

# 9.4.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.insertAfter('<li>insert item</li>')
# print(li)

# 9.5.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.insertBefore('<li>insert item</li>')
# print(li)

# 9.6.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.wrap('<li>insert item</li>')
# print(li)

# 9.7.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.wrapAll('<li>insert item</li>')
# print(li)

# 10.伪类选择器
# doc = pq(html)
# li = doc('li:first-child')
# print(li)
# li = doc('li:last-child')
# print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li = doc('li:contains(second)')
# print(li)
