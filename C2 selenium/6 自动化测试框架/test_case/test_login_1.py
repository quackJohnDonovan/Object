import time

from test_func.test_func_common import test_func_common


class login(test_func_common):
    def test_login(self):
        name = "htest"
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_css_selector(".login_btn.fl").click()

        # 用断言代替if else语句做判断
        time.sleep(3)
        self.assertEqual('我的会员中心 - 道e坊商城 - Powered by Haidao', self.driver.title)
        self.assertEqual("http://127.0.0.1/index.php?m=user&c=index&a=index", self.driver.current_url)
        self.assertEqual("您好 " + name,
                         self.driver.find_element_by_css_selector(".site-nav-right.fr > a:nth-child(1)").text)
        input1 = self.driver.find_element_by_css_selector(".btn1").get_attribute("value")
        out1 = "".join(input1.split())
        self.assertEqual("搜索", out1)
