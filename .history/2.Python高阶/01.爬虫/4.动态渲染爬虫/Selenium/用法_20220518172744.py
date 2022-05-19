# sourcery skip: avoid-builtin-shadow
# import time

from selenium import webdriver

# from selenium.webdriver.common.by import By
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
# find_element
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()

# browser.get('https://www.taobao.com')
# 以下两种方式等价
# input_first = find_element(By.ID, 'q')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()

# 3.2 多个节点
# find_elements
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

# 4.节点交互
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')  # 查找节点
# input.send_keys('iPhone')  # 输入内容
# time.sleep(1)
# input.clear()  # 清空输入框
# input.send_keys('iPad')  # 输入内容
# button = browser.find_element_by_class_name('btn-search')  # 查找节点
# button.click()  # 点击按钮
# browser.close()  # 关闭浏览器

# 5.获取属性
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# print(input.get_attribute('type'))
# browser.close()

# 6.获取文本
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# print(input.text)
# browser.close()

# 7.获取属性值
# browser.get('https://www.taobao.com')
# input = browser.find_element_by_id('q')
# print(input.get_attribute('value'))
# browser.close()