import time

# 时间戳
print(time.time())
print(time.localtime())

# Sat Jul 24 18:47:11 2021-asctime
print(time.asctime(time.localtime()))

# 格式化成2016-03-20 11:45:39形式-strftime
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳-mktime
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 推迟调用线程的运行
time.sleep(0.5)
