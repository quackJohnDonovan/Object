'''
爬虫
已完成面向过程封装

版本：
1.0完成单条数据的抓取         2021/04/25
2.0使用循环抓取多页数据       2021/04/25
3.0将抓取数据写入txt文件      2021/04/25
4.0面向过程的封装            2021/04/27
5.0面向对象的封装            2021/04/28
6.0代码逻辑优化             2021/04/28

'''

# 6.0版本

import requests
from lxml import etree


# 定义类
class spider:

    # 全局函数
    def __init__(self, url, page):
        # 将参数传入
        self.url = url
        self.page = page

    # 连接网页
    def link(self):
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

    # 抓取内容
    def spider(self):
        # 获取指定xpath路径下的内容
        collect = ''
        for i in range(1, 11):
            ele = self.doc.xpath('/html/body/div[6]/div[1]/div[' + str(i) + ']/h3/a/text()')[0]
            collect = collect + ele + str('\n')
        self.final = collect

    # 将内容写入文件
    def file(self):
        # 创建文件(已有前提下就是打开文件)
        if self.page == 1:
            file = open('../spider.txt', 'w')
        else:
            file = open('../spider.txt', 'a')
        # 写入内容
        file.write('第' + str(self.page) + '页')
        file.write('\n')
        file.write(self.final)
        file.write('\n')
        # 关闭文件
        file.close()


if __name__ == '__main__':
    # 根据不同的URL变化规则制定算法
    for i in range(1, 11):
        if i == 1:
            url = 'http://www.51testing.com/html/90/category-catid-90.html'
        else:
            url = 'http://www.51testing.com/html/90/category-catid-90-page-' + str(i) + '.html'
        spiderObj = spider(url, i)
        spiderObj.link()
        spiderObj.spider()
        spiderObj.file()
