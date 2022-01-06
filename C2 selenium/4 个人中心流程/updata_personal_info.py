#

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1、打开浏览器，设置全屏，设置等待时间最长10s
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# 2、登录
driver.get("http://127.0.0.1/index.php")
driver.find_element_by_link_text("登录").click()
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
driver.find_element_by_id("username").send_keys("htest")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
# 3.1、点击“账号设置”
driver.find_element_by_link_text("账号设置").click()
# 3.2、点击“个人资料”
# 使用部分文本匹配方式by_partial_link_text
driver.find_element_by_partial_link_text("人资").click()
# 3.3、修改“真实姓名”
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("何冰")
# 3.4、选择“性别”
driver.find_element_by_css_selector("[value='1']").click()
# 3.5、选择“生日”
# 3.5.1 删除readonly
script = 'document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(script)
# 3.5.2 输入新的生日
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1980-02-02")
# 3.6、选择“QQ”
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("222222")
# 3.7、点击“确定”
driver.find_element_by_css_selector("[value='确认']").click()
# 3.8 alert控件点击确定
# time.sleep(2)
WebDriverWait(driver, 30, 0.5).until(expected_conditions.alert_is_present())
update_status = driver.switch_to.alert.text
print(update_status)
driver.switch_to.alert.accept()
