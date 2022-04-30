# csv是特定字符分隔的纯文本，结构简单清晰
# 可以通过Excel等工具打开

import csv

# 1.写入
with open(r'C:\Users\kxl666\Desktop\Python\1.Python基础\07.文件和异常\_temp\data.csv',
          'w',
          encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])  # 单行写入
    writer.writerows([['10004', 'Jack', 24], ['10005', 'Rose', 26]])  # 多行写入
