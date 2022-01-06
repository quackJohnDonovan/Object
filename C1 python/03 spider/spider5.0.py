'''
爬虫
已完成面向过程封装

版本：
1.0完成单条数据的抓取         2021/04/25
2.0使用循环抓取多页数据       2021/04/25
3.0将抓取数据写入txt文件      2021/04/25
4.0面向过程的封装            2021/04/27
5.0面向对象的封装            2021/04/28

'''

# 5.0版本

import requests
from lxml import etree


# 定义类
class spider():
    def __init__(self,url):
        self.url = url

    # 定义方法：连接网页，获取内容
    def link(self):

        # 创建文件
        self.file = open('../spider.txt', 'w')
        # 发送请求
        response = requests.get(self.url)
        # 确定编码格式
        response.apparent_encoding
        # 确定解码格式
        response.encoding = 'gbk'
        # 转换文本类型
        content = response.text
        # 转换json格式
        self.doc = etree.HTML(content)


    # 定义字段：抓取网页中的内容
    def spider(self):

        for j in range(2, 4):
            for i in range(1, 11):
                ele = self.doc.xpath('/html/body/div[6]/div[1]/div[' + str(i) + ']/h3/a/text()')[0]
                self.file.write(ele)
                self.file.write('\n')

            # 定义url
            url = 'http://www.51testing.com/html/90/category-catid-90-page-' + str(j) + '.html'
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

        self.file.close()


if __name__ == '__main__':
    url = 'http://www.51testing.com/html/90/category-catid-90.html'
    spiderObj = spider(url)
    spiderObj.link()
    spiderObj.spider()