
# 1、打开浏览器

from selenium import webdriver
driver = webdriver.Chrome()

# 2、打开bing网站
driver.get('https://cn.bing.com/')
# 3、输入关键词
driver.find_element_by_id('sb_form_q').send_keys('51testing')
# 4、点击搜索按钮
driver.find_element_by_id('sb_form_go').click()



# 5、检查搜索结果