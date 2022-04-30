# 不是让程序在异常发生时就崩溃，可以将反向跟踪信息写入一个日志文件，并让程序继续运行
import traceback

try:
    raise Exception('This is the error message.')
except Exception as e:
    errorFile = open(
        r'C:\Users\kxl666\Desktop\Python\1.Python基础\08.文件和异常\_temp\errorInfo.txt',
        'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
    print(e)
