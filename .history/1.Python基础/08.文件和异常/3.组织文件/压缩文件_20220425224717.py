# 用 zipfile 模块压缩文件
import os
import zipfile

os.chdir(r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp')
# 1. 创建压缩文件 和 追加文件到压缩文件
# 创建压缩文件 w
# 追加文件到压缩文件 a
# newZip = zipfile.ZipFile('new.zip', 'a')
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

# 2. 读取压缩文件
exampleZip = zipfile.ZipFile('new.zip')
print(exampleZip.namelist())
# ['spam1.txt', 'spam1.txt', 'spam.txt']
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.close()
