from selenium import webdriver

# 1.声明浏览器对象
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

# 2.访问界面
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
