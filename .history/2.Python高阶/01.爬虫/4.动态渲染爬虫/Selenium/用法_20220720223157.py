# sourcery skip: avoid-builtin-shadow
# import time
# from selenium.webdriver import ActionChains
from selenium import webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

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
# print(input.location) # 获取节点的位置
# print(input.size) # 获取节点的大小
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
# print(browser.window_handles)  # 获取当前窗口句柄集合
# browser.switch_to.window(browser.window_handles[1])  # 切换到新窗口
# browser.get('https://www.jd.com')
# browser.switch_to.window(browser.window_handles[0])  # 切换到原窗口
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
# 还有另外一些操作,它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser) # 创建动作链
# 以下是动作链的一些操作，比如鼠标拖曳、键盘按键等
# actions.drag_and_drop(source, target) # 拖拽
# actions.click_and_hold(source).perform() # 按住拖动
# actions.move_by_offset(100, 100).perform() # 移动
# actions.move_to_element_with_offset(target, 100, 100).perform() # 移动到某个元素的位置
# actions.move_to_element(target).release().perform() # 鼠标移动到目标位置并释放
# actions.release(source).perform() # 释放鼠标
# actions.perform() # 执行动作链

# 16.执行JavaScript
# 所以说有了这个方法，基本上API没有提供的所有功能都可以用执行JavaScript的方式来实现
# browser.get('https://www.taobao.com')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(2)
# browser.close()

# 17.延时等待
# 在某些情况下，我们需要等待页面加载完成，这时候就需要使用 WebDriverWait 来实现。
# 17.1 隐式等待
# 隐式等待是指当查找节点而节点并没有立即出现的时候,隐式等待将等待一段时间再查找DOM，默认的时间是0。
# browser.implicitly_wait(10)
# browser.get('https://www.taobao.com')
# print(browser.find_element_by_id('q').get_attribute('value'))

# browser.close()
# 17.2 显式等待
# 显式等待是指它指定要查找的节点，然后指定个最长等待时间如果在规定时间内加载来了这个节点，就返回查找的节点
# 还有其他等待条件...
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# 以下是wait.until的查找节点的方式
# input = wait.until(EC.presence_of_element_located((By.ID, 'q'))) # 判断节点是否存在
# input = wait.until(EC.element_to_be_clickable((By.ID, 'q'))) # 判断节点是否可以点击
# input = wait.until(EC.visibility_of_element_located((By.ID, 'q'))) # 判断节点是否可见
# input = wait.until(EC.invisibility_of_element_located((By.ID, 'q'))) # 判断节点是否不可见
# input = wait.until(EC.text_to_be_present_in_element((By.ID, 'q'), 'taobao')) # 判断节点的文本是否包含某个字符串
# input = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframe-main'))) # 判断节点是否可以被加载出来并且切换到该节点
# input = wait.until(EC.title_is(' taobao')) # 判断页面的title是否包含某个字符串
# input = wait.until(EC.title_contains('taobao')) # 判断页面的title是否包含某个字符串
# ......
# print(input.get_attribute('id'))
# browser.close()

# 18.前进和后退
# 前进和后退的方法都是用 browser.forward() 和 browser.back() 来实现的。
# browser.get('https://www.taobao.com')
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.back()
# browser.forward()
# browser.close()

# 19.异常处理
# 在程序中，如果发生了异常，那么就需要处理异常，这时候就需要使用 try...except...finally...来处理异常。
# browser.get('https://www.taobao.com')
# try:
#     browser.find_element_by_id('hello')
# except TimeoutException:
#     print('没有找到元素')
# finally:
#     browser.close()

# 20.获取屏幕截图
# browser.get('https://www.taobao.com')
# time.sleep(3)
# browser.save_screenshot('taobao.png')
# browser.close()

# 21.获取屏幕截图
# browser.get('https://www.taobao.com')
# time.sleep(3)
# # 获取当前窗口的截图
# screenshot = browser.get_screenshot_as_png()
# # 保存截图
# with open('taobao.png', 'wb') as f:
#     f.write(screenshot)
# browser.close()

# 22.设置代理
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://ip:port')
