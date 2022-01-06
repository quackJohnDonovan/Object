import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

'''
1.设置同步等待时间/窗口最大化
driver.implicitly_wait(2)
driver.maximize_window()
2.使用顺序：id ---> name ---> Class name ---> 存在<a>标签使用link_text()
3.切换窗口
找到原来窗口名字
new_window = driver.window_handles[-1]
切换到新窗口
driver.switch_to.window(new_window)
'''

# 0、打开chrome浏览器/设置同步等待时间/窗口最大化
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
# 1、登录电商网站
driver.get('http://127.0.0.1/index.php?m=user&c=public&a=login')
# 2、登录
driver.find_element_by_id("username").send_keys("htest")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name('login_btn').click()
time.sleep(3)
# 3、进入商品界面
driver.find_element_by_link_text("进入商城购物").click()
# 4、搜索iphone
# 使用顺序：id ---> name ---> Class name ---> 存在<a>标签使用link_text()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
# 5、点击商品图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
time.sleep(2)
# 新窗口显示所有元素不能被操作NoSuchElementException: Message: no such element: Unable to locate element:
# 即使浏览器出现了新窗口，selenium任然工作在原来窗口
# 解决方案1、找到原来窗口名字
new_window = driver.window_handles[-1]
# 2、切换到新窗口
driver.switch_to.window(new_window)
# 6、添加购物车
driver.find_element_by_id("joinCarButton").click()
time.sleep(1)
# 7、点击”去购物车结算“
driver.find_element_by_class_name("shopCar_T_span3").click()
time.sleep(1)
# 8、点击”结算“
# driver.find_element_by_class_name("shopCar_btn_03").click()
# 第六中元素定位方法：css selector
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
# 9、添加新地址
driver.find_element_by_class_name("add-address").click()
# 10、输入信息
driver.find_element_by_name("address[address_name]").send_keys("何冰")
driver.find_element_by_name("address[mobile]").send_keys("13252026162")
# 选择省
province = driver.find_element_by_id("add-new-area-select")
Select(province).select_by_visible_text("甘肃省")
# 选择市
city = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(city).select_by_visible_text("兰州市")
# 选择区
area = driver.find_elements_by_tag_name("add-new-area-select")[2]
Select(area).select_by_visible_text("安宁区")