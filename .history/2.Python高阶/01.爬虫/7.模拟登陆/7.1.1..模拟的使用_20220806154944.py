# 模拟登录常用的 3 种方法
import pytesseract
import requests
from lxml import etree
from PIL import Image
'''
1.POST 请求方法：需要在后台获取登录的 URL并填写请求体参数,然后 POST 请求登录，相对麻烦；
2.添加 Cookies 方法：先登录将获取到的 Cookies 加入 Headers 中，最后用 GET 方法请求登录，这种最为方便；
3.Selenium 模拟登录：代替手工操作，自动完成账号和密码的输入，简单但速度比较慢。
'''
'''
模拟登录古诗文网
'''

#  验证码识别平台 代码省略

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
    result = pytesseract.image_to_string(image)  # 识别图片
    return result


code_text = tranformImgCode('./code.jpg')
print(code_text)

logging_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE':
    'yHvjS3OWtJfNZJqfSYyYibXwvl0id5pVg2P3TQ3YtCK5ZL3njrlRb9NcnY94rlpOJ+aFe918VKulPdD8cYbiO3MXvZ3Wcsy5Y5RyXFTR+URHNe1bIKK1+hSaj8YhLdUDuYe1smZhEVlPBdU2cwysg1AdRsE=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2244951869@qq.com',
    'pwd': '197618nm',
    'code': code_text,  # 动态变化
    'denglu': '登录'
}

# 对点击登陆按钮发起请求:获取了登录成功后对应的页面源码数据
page_text_login = session.post(url=logging_url, data=data,
                               headers=headers).text

print(page_text_login)
# with open('./gushiwen.html', 'w', encoding='utf-8') as f:
#     f.write(page_text_login)
