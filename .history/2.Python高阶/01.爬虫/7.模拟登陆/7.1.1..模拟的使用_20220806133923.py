import pytesseract
import requests
from lxml import etree
from PIL import Image

### 验证码识别平台 代码省略

headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

# 定义一个session对象
session = requests.Session()

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = session.get(url=url, headers=headers).text

# 解析验证码图片的地址.
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[
    0]  # 这里我们可以利用浏览器工具复制

# 将验证码图片保存到本地
img_data = session.get(url=img_src, headers=headers).content
with open('./code.jpg', 'wb') as f:
    f.write(img_data)


# # 识别验证码
def tranformImgCode(image):
    image = Image.open(image)
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
    return result


code_text = tranformImgCode('./code.jpg')
print(code_text)

# logging_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
# data = {
#     '__VIEWSTATE': 'TYrcSZVBcsrK06o1w3zD9LM9zKm2tkckwnArGUc/bevM7LJgxzZZBzrDm7OFiUftVmdPWjlgAPQck3od+jCovr/m48jr816FNS/X/AG1QxQrJZh5VMFiw8k4Q6s=',
#     '__VIEWSTATEGENERATOR': 'C93BE1AE',
#     'from': 'http://so.gushiwen.cn/user/collect.aspx',
#     'email': 'xxx@163.com',
#     'pwd': 'xxx',
#     'code': code_text,  # 动态变化
#     'denglu': '登录'
# }

# # 对点击登陆按钮发起请求:获取了登录成功后对应的页面源码数据
# page_text_login = session.post(url=logging_url, data=data, headers=headers).text
# with open('./gushiwen.html', 'w', encoding='utf-8') as f:
#     f.write(page_text_login)
