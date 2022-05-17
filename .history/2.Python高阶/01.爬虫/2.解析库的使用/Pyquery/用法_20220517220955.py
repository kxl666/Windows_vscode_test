# pyquery 的CSS选择器比 beautifulsoup更加强大

from pyquery import PyQuery as pq

html = '''
<div id='container'>
<h1>head1</h1>
<h2>head2</h2>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class=bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0" id='id-0'><a href="links.html">fifth item</a></li>
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

# 6.获取文本
# doc = pq(html)
# li = doc('.item-0.active a')
# print(li.text())

# 7.获取html
# doc = pq(html)
# li = doc('.item-0.active a')
# print(li.html())

# 8.获取属性,以下两种方式等价
doc = pq(html)
# li = doc('.item-0.active a')
# print(li.attr('href'))
# print(li.attr.href)

# 9.pyquery的特别使用
# print(doc('li[class=item-0]').text())
# print(doc('li[class=item-1] a').text())  # 获取子孙节点中的文本
# print(doc('li[class=item-1] > a').text())  # 获取子节点中的文本
# print(doc('h1, h2').text())  # 属性或的匹配
# print(doc('li.item-0').text())  #获取class为item-0的节点的文本
# print(doc('li.item-0.active').text())  # 获取class为item-0,active的节点的文本,多个属性的匹配
# print(doc('li[class=item-0][id=id-0]').text()) # 获取class为item-0,id为id-0的节点的文本,多个属性的匹配
# print(doc('li[class=item-0],li[class=item-1]').text())  # 或的关系,多个属性的匹配,绝对匹配属性所以范围小
# print(doc('li.item-0,li.item-1').text())  # 或的关系,多个属性的匹配,相对匹配属性所以范围大
print(doc('*'))

# print(doc('li').eq(1).text())  # 获取第二个li节点的文本
# print(doc('li').filter('.item-0').text())  # 获取class为item-0的节点的文本
# print(doc('li').not_('.active').text())  # 获取class不为active的节点的文本
# print(doc('li').slice(0, 2).text())  # 获取第一个到第二个节点的文本
# print(doc('li').eq(1).parent().text())  # 获取第二个li节点的父节点的文本

# 10.节点操作,它们和 jQuery的用法完全一致
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

# 10.1.添加节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.append('<li>append item</li>')
# print(li)

# 10.2.删除节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.remove()
# print(li)

# 10.3.替换节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.replaceWith('<li>replace item</li>')
# print(li)

# 10.4.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.insertAfter('<li>insert item</li>')
# print(li)

# 10.5.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.insertBefore('<li>insert item</li>')
# print(li)

# 10.6.插入节点
# doc = pq(html)
# li = doc('.item-0.active')
# li.wrap('<li>insert item</li>')
# print(li)

# 10.7.插入节点
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
