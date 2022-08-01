import requests
from bs4 import BeautifulSoup

res = [
    requests.get(
        'https://www.wendangwang.com/doc/221ab7038fcbe3e98b0d0a13daed802520aca545/'
        + str(i),
        headers={
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }) for i in range(1, 6)
]

for i in res:
    i.encoding = 'gdk'
    soup = BeautifulSoup(i.text, 'lxml')
    results = soup.find_all('div',
                            attrs={
                                'class': 'contents',
                                'id': 'contents'
                            })
    for result in results:
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(result.get_text())
