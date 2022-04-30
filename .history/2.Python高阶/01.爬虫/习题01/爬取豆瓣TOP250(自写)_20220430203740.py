import os
import re

import openpyxl
import requests
from requests.exceptions import RequestException


def get_Page(url):
    headers = {'User-Agent': 'BaiduSpider'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("请求失败！")
        return None


def parse_Page(html):
    pattern = re.compile(
        r'<span class="title">([^&].*?)</span>\s+<span class="title">(.*?)</span>.*?<span class="other">(.*?)</span>.*?<div class="bd">\s+<p class="">(.*?)</p>',
        re.S)
    result = pattern.findall(html)
    for i in result:
        yield {
            'name': i[0],
            'alias': i[1].strip('&nbsp;/&nbsp;') + i[2].strip('&nbsp;/&nbsp;'),
            'detail': re.sub('&nbsp;|<br>| ', '', i[3].strip('\n'))
        }  # 用法


def save_Page(find_Dir):

    if not os.path.exists('豆瓣电影TOP250.xlsx'):

        wb = openpyxl.Workbook()
        wb.guess_types = True
        ws = wb.active
        ws.append(['姓名', '别名', '简介'])
        for i in find_Dir:
            ws.append([i['name'], i['alias'], i['detail']])
        wb.save('豆瓣电影TOP250.xlsx')
    else:
        wb = openpyxl.load_workbook('豆瓣电影TOP250.xlsx')
        ws = wb.active
        for i in find_Dir:
            ws.append([i['name'], i['alias'], i['detail']])
        wb.save('豆瓣电影TOP250.xlsx')


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page)
    print(url)
    html = get_Page(url)
    find_Dir = parse_Page(html)
    save_Page(find_Dir)


if __name__ == "__main__":
    pool = Pool()
    pool.map(main, [(page - 1) * 25 for page in range(1, 11)])

    # 第一种
    # for page in range(1, 11):
    #     page = (page - 1) * 25
    #     main(page)

    # 第二种
    # 直接map会返回迭代器
    # list(map(main, [(page - 1) * 25 for page in range(1, 11)]))
