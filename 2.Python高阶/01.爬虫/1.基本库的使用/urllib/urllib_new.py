# 01 爬取一张图片

import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_image = response.read()

with open('cat.jpg', 'wb') as f:
    f.write(cat_image)
