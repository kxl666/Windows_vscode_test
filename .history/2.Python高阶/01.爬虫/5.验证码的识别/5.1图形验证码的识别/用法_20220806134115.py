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
image = image.convert('L')  # 转换为灰度图
threshold = 127  # 阈值
table = []  # 定义一个存放转换后的像素值的列表
for i in range(256):
    if i < threshold:  # 小于阈值时，设置为0
        table.append(0)  # 小于阈值时，设置为0
    else:
        table.append(1)  # 大于阈值时，设置为1
image = image.point(table, '1')  # 转换为二值图
result = pytesseract.image_to_string(image)  # 识别图片
print(result)
