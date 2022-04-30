import requests

resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    # 通过Response对象的text属性获取服务器返回的文本内容
    with open('baidu.txt', 'w', encoding="utf-8") as file:
        file.write(resp.text)
