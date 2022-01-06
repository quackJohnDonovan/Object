import time
import unittest2
from selenium.webdriver import ActionChains
from title_func_base import test_func_common


class addmember(test_func_common):

    def test_login(self):
        # 登录
        self.driver.get("http://localhost/admin.php")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("userpass").send_keys("password")
        self.driver.find_element_by_name("userverify").send_keys("1234")
        self.driver.find_element_by_class_name("Btn").click()

    def test_zadd_member(self):
        # 进入会员管理，点击添加会员
        self.driver.find_element_by_link_text("会员管理").click()
        self.driver.find_element_by_link_text("添加会员").click()
        time.sleep(1)
        # 用户名
        self.driver.switch_to.frame(self.driver.find_element_by_id("mainFrame"))
        ActionChains(self.driver).click(self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/dl/dd/div/div/dl/form/dd/ul/li[1]/input")).send_keys("test888").perform()
        # 手机号
        ActionChains(self.driver).click(self.driver.find_element_by_name("mobile_phone")).send_keys(
            "18255555555").perform()
        # 性别：男
        self.driver.find_element_by_css_selector("[value='1']").click()
        # 生日
        self.driver.find_element_by_id("birthday").click()
        self.driver.find_element_by_id("laydate_y").click()
        self.driver.find_element_by_css_selector(".laydate_tab.laydate_chtop").click()
        self.driver.find_element_by_css_selector(".laydate_tab.laydate_chtop").click()
        self.driver.find_element_by_css_selector("ul#laydate_ys > li[y='1996']").click()
        self.driver.find_element_by_id("laydate_m").click()
        self.driver.find_element_by_css_selector("div#laydate_ms > span[m='7']").click()
        self.driver.find_element_by_css_selector("[d='10']").click()

        # 邮箱与qq
        ActionChains(self.driver).click(self.driver.find_element_by_name("email")).send_keys(
            "13251256502@163.com").perform()
        ActionChains(self.driver).click(self.driver.find_element_by_name("qq")).send_keys(
            "13251256502").perform()
        # 确认
        self.driver.find_element_by_class_name("button_search").click()


if __name__ == '__main__':
    unittest2.addmember()
