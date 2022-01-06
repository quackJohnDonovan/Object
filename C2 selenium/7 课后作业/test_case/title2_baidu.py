from selenium.webdriver import ActionChains
from title_func_base import test_func_common


class search(test_func_common):

    def test_search(self):
        self.driver.get("https://www.baidu.com/")
        position = self.driver.find_element_by_css_selector(".bg.s_ipt_wr.quickdelete-wrap")
        ActionChains(self.driver).click(position).send_keys("天气").perform()
        self.driver.find_element_by_id("su").click()
