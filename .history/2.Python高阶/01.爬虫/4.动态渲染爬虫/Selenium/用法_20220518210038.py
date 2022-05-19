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
# print(input.get_attribute('type'))
# print(input.get_attribute('name'))
# print(inout.get_attribute('placeholder'))
# print(input.get_attribute('class'))
# print(input.get_attribute('id'))
# print(input.id)
# print(input.location)
# print(input.size)
# print(input.tag_name)
# browser.close()

# 8.获取网页标题
# browser.get('https://www.taobao.com')
# print(browser.title)
# browser.close()

# 9.获取网页URL
# browser.get('https://www.taobao.com')
# print(browser.current_url)
# browser.close()

# 10.获取网页源代码
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# 11.1 获取cookie
# browser.get('https://www.taobao.com')
# print(browser.get_cookies())
# browser.close()
# 11.2 设置cookie
# browser.get('https://www.taobao.com')
# browser.add_cookie({'name': 'name', 'domain': 'taobao.com', 'value': 'value'})
# print(browser.get_cookies())
# browser.close()
# 11.3 删除cookie
# browser.get('https://www.taobao.com')
# browser.delete_all_cookies()
# print(browser.get_cookies())
# browser.close()

# 13.切换窗口
# browser.get('https://www.taobao.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# print(browser.title)
# browser.close()

# 14.1 切换frame
# Selenium打开页面后，它默认是在父级 Frame里面操作，而此时如果页面中还有子Frame，它是不能获取到子Frame里面的节点的。
# 这时就需要使用switch_to.frame()方法来切换 Frame。
# browser.get('https://www.taobao.com')
# browser.switch_to.frame(browser.find_element_by_id('iframe-main'))
# print(browser.find_element_by_id('q').get_attribute('value'))
# browser.close()

# 15.动作链
# browser.get('https://www.taobao.com')

# 16.执行JavaScript
# 所以说有了这个方法，基本上API没有提供的所有功能都可以用执行JavaScript的方式来实现
browser.get('https://www.taobao.com')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.close()

# 17.获取屏幕截图
# browser.get('https://www.taobao.com')
# time.sleep(3)
# browser.save_screenshot('taobao.png')
# browser.close()
