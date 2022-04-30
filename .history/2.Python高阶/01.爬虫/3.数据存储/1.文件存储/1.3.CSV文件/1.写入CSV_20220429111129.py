# csv是特定字符分隔的纯文本，结构简单清晰
import csv

with open(r'data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
