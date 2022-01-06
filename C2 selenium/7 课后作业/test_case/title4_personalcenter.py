import time
import unittest2
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from title_func_base import test_func_common


class jd(test_func_common):

    def test_1_login(self):
        self.driver.get("https://www.jd.com/")
        # 进入登录页面
        self.driver.find_element_by_link_text("你好，请登录").click()
        self.driver.find_element_by_link_text("账户登录").click()

        # 这里就不告诉你密码了，老师检查的时候可以用自己的代替
        position_username = self.driver.find_element_by_id("loginname")
        ActionChains(self.driver).click(position_username).send_keys("*").perform()

        position_password = self.driver.find_element_by_id("nloginpwd")
        ActionChains(self.driver).click(position_password).send_keys("*").perform()

        self.driver.find_element_by_id("loginsubmit").click()

        # 滑块暂时太复杂了，设置个等待时间手动滑滑块
        time.sleep(5)

    def test_2_personal_UI(self):
        # 找到主界面中进入个人中心的元素位置
        position_personal = self.driver.find_element_by_css_selector(".dt.cw-icon")
        position_click = self.driver.find_element_by_class_name("nickname")

        # 悬浮位置1并点击位置2，以进入个人中心，新页面需要切换句柄
        ActionChains(self.driver).move_to_element(position_personal).click(position_click).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 进入资料修改页面，新页面需要切换句柄
        self.driver.find_element_by_class_name("user-name").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def test_3_submit(self):
        # 选择性别：男
        self.driver.find_element_by_css_selector("div.fl > input[value='0']").click()

        # 选择生日：1996年8月10日
        Select(self.driver.find_element_by_id("birthdayYear")).select_by_visible_text("1996")
        Select(self.driver.find_element_by_id("birthdayMonth")).select_by_visible_text("8")
        Select(self.driver.find_element_by_id("birthdayDay")).select_by_visible_text("10")

        # 选择兴趣爱好：运动健康
        # 注意：上面的性别与这里的爱好都有value，所以定位元素时最好把上层元素写进来，并用 > 链接
        self.driver.find_element_by_css_selector("ul.hobul > li[value='9']").click()
        # 点击提交
        # self.driver.find_element_by_link_text("提交").click()


if __name__ == '__main__':
    unittest2.jd()
