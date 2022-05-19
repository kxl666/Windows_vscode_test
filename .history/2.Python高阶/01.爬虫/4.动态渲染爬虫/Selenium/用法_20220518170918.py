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
find_element_by_idfind element by namefind element by_xpathfind_element_by_link_text
find element_by_partial_link_textfind element_by_tag_name
find_element_by class _namefind_element_by_css_selector


browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
