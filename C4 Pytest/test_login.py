from selenium import webdriver
import pytest
# 1、创建测试类
class Test_baidu():

# 2、创建测试方法
    def test_login(self):
        url = "https://www.baidu.com"
        driver = webdriver.Chrome()
        driver.get(url)
# 3、通过断言进行明确