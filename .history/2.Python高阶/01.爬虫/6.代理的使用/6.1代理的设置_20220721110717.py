import zipfile

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
proxy = '127.0.0.1:1080'
chrome_options = webdriver.ChromeOptions()  # 创建一个ChromeOptions对象
chrome_options.add_argument('--proxy-server=proxy')  # 添加代理服务器
browser = webdriver.Chrome(chrome_options=chrome_options)  # 创建一个Chrome对象
browser.get('http://httpbin.org/get')  # 访问网站

# 代理认证
# 这里需要在本地创建一个 manifest.json 置文｛牛和 background 脚本来设置认证代理 运行代之后本 会生成一个 proxy auth __plugin.zip 文件来保存当前配置
ip = '127.0.0.1'
port = 9743
username = 'foo'
password = 'bar'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
          }
        }
      }

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
)
""" % {
    'ip': ip,
    'port': port,
    'username': username,
    'password': password
}

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension(plugin_file)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

# 03 phantom's
service_args = ['--proxy= 127.0.0.1:1080', '--proxy-type=http']
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
