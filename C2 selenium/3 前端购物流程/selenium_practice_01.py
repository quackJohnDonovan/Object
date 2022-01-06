'''
selenium练习：在京东网站搜索书籍，加车，结算
'''
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# 1、打开chrome浏览器
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# 1、进入京东官网
driver.get("https://www.jd.com/")
# 2、登录
# 进入登陆界面
driver.find_element_by_class_name("link-login").click()
# 切换账户登录
driver.find_element_by_link_text("账户登录").click()
# 输入用户名
driver.find_element_by_id("loginname").send_keys("13252026162")
# 输入密码
driver.find_element_by_id("nloginpwd").send_keys("xbd1231231230")
# 点击登陆
driver.find_element_by_id("loginsubmit").click()
# 拼图验证
time.sleep(7)
# 3、在首页搜索框搜索python书籍
# 输入python
driver.find_element_by_id("key").send_keys("P40 PRO")
# 点击查询
driver.find_element_by_class_name("button").click()
# 4、进入详情并添加购物车
# 点击图片进入详情
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img").click()
# 由于切换了新页面，需要切换句柄
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
# 点击添加购物车
driver.find_element_by_css_selector(".btn-append.btn-special1.btn-lg").click()
# 5、进入购物车，结算
# 点击”去购物车结算“
driver.find_element_by_class_name("btn-addtocart").click()
# 点击”去结算“
driver.find_element_by_class_name("common-submit-btn").click()
# 6、添加收货地址
# 点击”新增收货地址“
driver.find_element_by_link_text("新增收货地址").click()
# 切换Iframe
iframe = driver.find_element_by_id("dialogIframe")
driver.switch_to.frame(iframe)
# 鼠标悬停
position = driver.find_element_by_class_name("ui-area-text")
ActionChains(driver).move_to_element(position).perform()
# 选择浙江省
driver.find_element_by_link_text("浙江").click()
# 选择杭州市
driver.find_element_by_link_text("杭州市").click()
# 选择滨江区长河街道
driver.find_element_by_link_text("滨江区").click()
driver.find_element_by_link_text("长河街道").click()
# 填写收货人
driver.find_element_by_id("consignee_name").send_keys("何冰")
# 填写详细地址
driver.find_element_by_id("consignee_address").send_keys("滨兴西苑")
# 填写手机号码
driver.find_element_by_id("consignee_mobile").send_keys("13252026162")
# 点击保存
driver.find_element_by_id("saveConsigneeTitleDiv").click()
