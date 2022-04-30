from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
  <a href="http://example.com/elsie" class="sister" id= "linkl">
    <span> Elsie</span>
  </a>
  hello
  <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
  and
  <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
  and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 一.节点选择
# print(soup.prettify()) # 格式化输出所有内容
# print(soup.title)  # 获取标签
# print(soup.title.name)  # 获取标签名
# print(soup.title.string)  # 获取标签内容
# print(soup.p)  # 获取标签,返回第一个p标签内所有内容
# print(soup.p.attrs)  # 获取标签属性
# print(soup.p.attrs['class'])  # 获取标签属性值

# 嵌套选择
# print(soup.p.a.span.string)  # 嵌套选择标签内容

# 关联选择
# 1.获取标签内所有内容,返回结果是列表形式
# print(soup.p.contents)
# 2.获取标签内所有内容,返回结果是迭代器形式
# for i in soup.p.children:
#     print(i)
# 3.获取所有子孙节点,返回结果是迭代器形式
# for i in soup.p.descendants:
#     print(i)
# 4.获取直接父节点
# print(soup.a.parent)
# 5.获取所有祖先节点,返回结果是生成器形式
# print(list(soup.a.parents))
# 6.兄弟节点
# print('Next Silbng', soup.a.next_sibling)  # 获取下一个兄弟节点
# print('Prev Silbng', soup.a.previous_sibling)  # 获取上一个兄弟节点
# print('Next All Silbng', list(soup.a.next_siblings))  # 获取所有下一个兄弟节点,返回结果是列表形式
# print('Prev All Silbng', list(soup.a.previous_siblings))  # 获取所有上一个兄弟节点,返回结果是列表形式
# 获取内容
# print(soup.a.next_sibling.string)

# 二.方法选择器

# 三.CSS选择器
