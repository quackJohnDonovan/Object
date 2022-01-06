# 获取库
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

# 1、后台登录
# 1.1 打开后台登录页面


driver = webdriver.Chrome()
driver.get("http://127.0.0.1/admin.php")
driver.implicitly_wait(5)
driver.maximize_window()
# 1.2 输入用户名、密码、验证码
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
# 2、添加商品
# 2.1、点击商品管理
driver.find_element_by_link_text("商品管理").click()
# 2.2、点击添加商品
driver.find_element_by_link_text("添加商品").click()
# 2.3、输入商品名称
# 由于使用了iframe框架，需要先将以下框架转换为可识别的frame
iframe = driver.find_element_by_id("mainFrame")
driver.switch_to.frame(iframe)

driver.find_element_by_name("name").send_keys("iphone xs max")
# 2.4、选择商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 2.5、选择商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_value("1")
# 2.6、添加图片
driver.find_element_by_link_text("商品图册").click()
# driver.find_element_by_css_selector("#filePicker label").click()
driver.find_element_by_name("file").send_keys('C:/Users/John Donovan/Desktop/20180913021107676.jpg')
# 2.7、上传图片
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# 2.8、处理弹窗
# 设置当alert就绪后获取文本，再点击确定；如果一直没就绪则每0.5s检查一次，持续30s
WebDriverWait(driver, 30, 0.5).until(expected_conditions.alert_is_present())
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
# 2.6、点击提交按钮
driver.find_element_by_class_name("button_search").click()