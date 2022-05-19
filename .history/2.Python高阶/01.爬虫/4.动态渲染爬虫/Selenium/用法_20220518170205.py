from selenium import webdriver

# 1.声明浏览器对象
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

# 2.访问界面
# get()方法，访问网页,page_source()方法，获取网页源代码
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# 3.查找节点
# 3.1 单个节点
