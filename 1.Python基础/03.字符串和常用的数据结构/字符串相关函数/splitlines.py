# Python splitlines() 按照行('\r', '\r\n', \n')分隔，
# 返回一个包含各行作为元素的列表，如果参数 keepends 为 False
# 不包含换行符，如果为 True，则保留换行符

str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())

str2 = 'ab c\n\nde fg\rkl\r\n'
print(str2.splitlines(True))
