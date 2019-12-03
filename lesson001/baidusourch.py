
from selenium import webdriver
# 引入Keys类包 发起键盘操作
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# 访问百度
driver.get('http://www.baidu.com')

# 输入框输入内容
driver.find_element_by_id('kw').send_keys('python')
# 3s
time.sleep(3)

# 删除多输入的一个m  (删除操作 模拟键盘的Backspace)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(3)



# 退出
driver.quit()
