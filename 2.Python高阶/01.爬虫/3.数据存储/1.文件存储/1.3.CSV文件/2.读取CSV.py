import csv

with open(r'C:\Users\kxl666\Desktop\Python\1.Python基础\07.文件和异常\_temp\data.csv',
          'r',
          encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
