import time
import unittest2
from selenium.webdriver import ActionChains
from title_func_base import test_func_common


class jd(test_func_common):

    def test_login(self):
        self.driver.get("https://www.jd.com/")
        self.driver.find_element_by_link_text("你好，请登录").click()
        self.driver.find_element_by_link_text("账户登录").click()

        # 这里就不告诉你密码了，我随便代替了
        position_username = self.driver.find_element_by_id("loginname")
        ActionChains(self.driver).click(position_username).send_keys("*").perform()

        position_password = self.driver.find_element_by_id("nloginpwd")
        ActionChains(self.driver).click(position_password).send_keys("*").perform()

        self.driver.find_element_by_id("loginsubmit").click()

        # 滑块暂时太复杂了，设置个等待时间手动滑滑块
        time.sleep(5)

    def test_search(self):
        position_text = self.driver.find_element_by_id("key")
        ActionChains(self.driver).click(position_text).send_keys("Python编程：从入门到实践").perform()
        self.driver.find_element_by_class_name("button").click()
