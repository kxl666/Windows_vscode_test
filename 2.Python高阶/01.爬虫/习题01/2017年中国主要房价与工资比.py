# find与find_all的区别：
# - 1. find：找到第一个满足条件的标签就返回。说白了，就是只会返回一个元素
# - 2. find_all:将所有满足条件的标签都返回。说白了，会返回很多标签（以列表的形式）

import re

import bs4
import openpyxl
import requests


def open_url(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    return res


# 爬取数据
def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(id="Cnt-Main-Article-QQ")
    target = content.find_all("p", style="TEXT-INDENT: 2em")
    target = iter(target)
    for each in target:
        if each.text.isnumeric():  # isnumeric() 方法检测字符串是否只由数字组成
            data.append([
                re.search(r'\[(.+)\]',
                          next(target).text).group(1),
                re.search(r'\d.*',
                          next(target).text).group(),
                re.search(r'\d.*',
                          next(target).text).group(),
                re.search(r'\d.*',
                          next(target).text).group()
            ])
    return data


# 保存为Excel表格
def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市', '平均房价', '平均工资', '房价工资比'])
    for each in data:
        ws.append(each)

    wb.save('2017年中国主要城市房价工资比排行榜.xlsx')


def main():
    url = "http://news.house.qq.com/a/20170702/003985.htm"
    res = open_url(url)
    data = find_data(res)
    to_excel(data)


if __name__ == "__main__":
    main()
