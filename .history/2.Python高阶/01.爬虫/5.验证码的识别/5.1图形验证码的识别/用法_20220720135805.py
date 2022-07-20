from email.mime import image
from msilib.schema import tables
from unittest import result

import pytesseract
import requests
from PIL import Image

re = requests.get('http://my.cnki.net/elibregister/CheckCode.aspx')
with open(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg',
        'wb') as f:
    f.write(re.content)

image = Image.open(
    r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg'
)
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = pytesseract.image_to_string(image)
print(result)
