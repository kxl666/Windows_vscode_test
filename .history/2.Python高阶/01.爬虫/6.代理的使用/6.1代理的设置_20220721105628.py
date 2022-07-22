import requests
from selenium import webdriver

# 01 request
url = 'http://httpbin.org/get'
proxy = '127.0.0.1:1080'
proxies = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
response = requests.get(url, proxies=proxies)
print(response.text)
# 如果代理需要认证，同样在代理的前面加上用户名密码即可
# proxy = 'user:password@127.0.0.1:1080'

# 使用 SOCKS5 代理
# proxies = {'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'}

# 02 selenium
# chrome_options = webdriver.ChromeOptions() # 创建一个ChromeOptions对象
# chrome_options.add_argument('--proxy-server=proxy') # 添加代理服务器
# browser = webdriver.Chrome(chrome_options=chrome_options) # 创建一个Chrome对象
# browser.get('http://httpbin.org/get') # 访问网站
