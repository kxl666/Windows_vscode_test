# csv是特定字符分隔的纯文本，结构简单清晰
import csv

with open(r'C:\Users\kxl666\Desktop\Python\1.Python基础\07.文件和异常\_temp\data.csv',
          'w',
          encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
