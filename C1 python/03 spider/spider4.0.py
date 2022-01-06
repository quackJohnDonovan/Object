'''
爬虫
已完成面向过程封装

版本：
1.0完成单条数据的抓取         2021/04/25
2.0使用循环抓取多页数据       2021/04/25
3.0将抓取数据写入txt文件      2021/04/25
4.0面向过程的封装            2021/04/27

'''

# 4.0版本

import requests
from lxml import etree


#通过url获取内容
def link():
    list = []

    # 创建文件
    file = open('../spider.txt', 'w')
    # 定义url
    url = 'http://www.51testing.com/html/90/category-catid-90.html'
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

    list.append(file)
    list.append(doc)

    return list


# 获取内容

def gain(file,doc):
    for j in range(2, 4):
        for i in range(1, 11):
            ele = doc.xpath('/html/body/div[6]/div[1]/div[' + str(i) + ']/h3/a/text()')[0]
            file.write(ele)
            file.write('\n')

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


    file.close()

if __name__ == '__main__':
    list = []
    list = link()
    gain(list[0],list[1])