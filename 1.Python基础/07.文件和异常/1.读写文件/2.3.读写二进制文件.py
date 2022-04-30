# 利用 shelve 模块，你可以将 Python 程序中的变量保存到二进制的 shelf 文件中
# shelve 是pickle的升级版，它可以将 Python 程序中的变量保存到二进制的 shelf 文件中
import shelve

# 们创建了一个列表cats，并写下shelfFile['cats'] =cats，将该列表保存在shelfFile 中，作为键'cats'关联的值（就像在字典中一样）。然后我们在shelfFile 上调用close()
shelfFile = shelve.open(
    r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open(
    r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp\mydata')
print(shelfFile['cats'])
# 结果：
# ['Zophie', 'Pooka', 'Simon']
shelfFile.close()

# 就像字典一样，shelf 值有 keys()和 values()方法，返回 shelf 中键和值的类似列
# 将它们传递给 list()函数
shelfFile = shelve.open(
    r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp\mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
# 结果：
# ['cats']
# ['Zophie', 'Pooka', 'Simon']
shelfFile.close()
