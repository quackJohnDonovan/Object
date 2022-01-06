import unittest2
from selenium import webdriver


# 预置重复步骤，之后在其他脚本中调用
class test_func_common(unittest2.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # # 测试步骤，测试完成后注释
    # def test_test(self):
    #     self.driver.find_element_by_link_text("登录").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
