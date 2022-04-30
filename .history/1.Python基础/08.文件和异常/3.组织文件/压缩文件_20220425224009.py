# 用 zipfile 模块压缩文件
import os
import zipfile

os.chdir(r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp')
newZip = zipfile.ZipFile('new.zip', 'a')
newZip.write('spam1.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
