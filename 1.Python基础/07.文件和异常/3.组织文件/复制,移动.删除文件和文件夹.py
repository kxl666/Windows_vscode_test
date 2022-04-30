# shutil 模块
# shutil（或称为 shell 工具）模块中包含一些函数，让你在 Python 程序中复制、移动、改名和删除文件
import os
import shutil

import send2trash

# 1.复制
# 1.1.复制文件
os.chdir(r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp')
# shutil.copy('test.txt', 'test_copy.txt')
# 1.2.复制文件夹
# shutil.copytree('testtest', 'test_copy')

# 2.移动
# shutil.move('test.txt', 'test_move.txt')
# 同一目录改名，或移动到其他目录下

# 3.删除
# 3.1 删除文件
# 3.1.1 使用os.remove删除文件
# os.remove('test.txt')
# 3.1.2 使用os.unlink删除文件,二者区别不大
# os.unlink('test.txt')

# 3.2 删除文件夹
# 3.2.1 使用os.rmdir只能删除空文件夹
# os.rmdir('testtest')
# 文件夹有内容会报错
# 3.2.2 使用shutil.rmtree删除文件夹,它包含的所有文件和文件夹都会被删除
shutil.rmtree('testtest')
# 3.2.3 使用send2trash安全删除文件夹,它包含的所有文件和文件夹都会被移动到 [回收站]
baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
