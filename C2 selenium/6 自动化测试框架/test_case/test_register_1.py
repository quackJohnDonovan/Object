import ddt
import unittest2

from test_func.test_func_common import test_func_common
from test_func.test_func_csv import test_func_csv



@ddt.ddt
class test_register_1(test_func_common):
    info = test_func_csv("register_data.csv")

    @ddt.data(*info)
    def test_register(self, row):
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=reg")
        self.driver.find_element_by_name("username").send_keys(row[0])
        self.driver.find_element_by_name("password").send_keys(row[1])
        self.driver.find_element_by_name("userpassword2").send_keys(row[2])
        self.driver.find_element_by_name("mobile_phone").send_keys(row[3])
        self.driver.find_element_by_name("email").send_keys(row[4])
        # self.driver.find_element_by_css_selector("[value='注册']").click()
        # self.driver.find_element_by_link_text("[退出]").click()


if __name__ == '__main__':
    unittest2.main()

# 日志：2021/05/06
# test_func_csv忘记写return了，数据没有返回也就获取不到
# 忘记把url移动到脚本中生成，导致无法进入注册页面
