from email.mime import image
import pytesseract
from PIL import Image
import requests

re = requests.get('http://my.cnki.net/elibregister/CheckCode.aspx')
with open(
        r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg',
        'wb') as f:
    f.write(re.content)

image = Image.open(
    r'C:\Users\kxl666\Desktop\Python\2.Python高阶\01.爬虫\5.验证码的识别\5.1图形验证码的识别\code.jpg'
)
image = image.convert('L')
thrsold