import requests
from bs4 import BeautifulSoup

res = requests.get(
    'https://www.wendangwang.com/doc/221ab7038fcbe3e98b0d0a13daed802520aca545/1',
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    })

soup = BeautifulSoup(res.text, 'lxml')
