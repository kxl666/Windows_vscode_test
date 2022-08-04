# 这个函数的作用是，返回传入字符串的表达式的结果。就是说：将字符串当成有效的表达式 来求值 并 返回计算结果
# eval函数就是实现list、dict、tuple与str之间的转化，同样str函数把list，dict，tuple转为为字符串
s = '1+2+3*5-2'
print(eval(s))

x = 1
print(eval('x+2'))

s = input("输入一个表达式")
print(eval(s))

# eval虽然方便，但是要注意安全性，可以将字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作。，比如用户恶意输入就会获得当前目录文件
eval("__import__('os').system('dir')")

print(type(eval("[1, 2, 3]")))  # <class 'list'>

type(eval("{'a': 1, 'b': 2}"))  # <class 'dict'>
