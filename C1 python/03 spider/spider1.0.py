'''
爬虫

版本：
1.0完成单条数据的抓取         2021/04/25

'''


import requests
from lxml import etree

# 定义url
url = 'http://www.51testing.com/html/index.html'
# 发送请求
response = requests.get(url)
# 确定编码格式
response.apparent_encoding
# 确定解码格式
response.encoding = 'gbk'
# 转换文本类型
content = response.text
# 转换json格式
doc = etree.HTML(content)


# 获取内容

ele = doc.xpath('/html/body/div[6]/div[2]/div/div[1]/h4/a/text()')[0]

print(ele)
