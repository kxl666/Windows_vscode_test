import subprocess

# 打开windows程序
# calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# 打开windows程序并传入参数
# subprocess.Popen([
#     'D:\\AppFiles\\Notepad++\\notepad++.exe',
#     'C:\\Users\\kxl666\\Desktop\\1.txt'
# ])
# 打开python程序同理
subprocess.Popen(['python', '-m', 'pdb', r'C:\Users\kxl666\Desktop\sjx.py'])

# calcProc.wait()  # 等待程序结束,这里的wait()是等待程序结束,如果不等待,那么程序会一直运行,直到程序结束,才会继续执行下面的代码
# calcProc.poll()  # 检查程序是否结束,如果程序结束,返回0,如果程序没有结束,返回None
