import subprocess

# 打开windows程序
calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# 打开windows程序并传入参数
# subprocess.Popen([
#     'D:\\AppFiles\\Notepad++\\notepad++.exe',
#     'C:\\Users\\kxl666\\Desktop\\1.txt'
# ])
# 打开python程序

calcProc.wait()

calcProc.poll()
