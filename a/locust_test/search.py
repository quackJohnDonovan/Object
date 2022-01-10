import requests
from lxml import etree

file = open('searchdata.csv', 'w')

response = requests.get('http://localhost/iwebshop/index.php?controller=site&action=sitemap').text
# print(response)
doc = etree.HTML(response)

for table in range(1, 6):

    for tr in range(2, 4):
        if table == 5 & tr == 2:
            break
        keyword = doc.xpath(
            "/html/body/div[1]/div[6]/div[2]/div[3]/table[" + str(table) + "]/tbody/tr[" + str(tr) + "]/td/a/text()")
        print(keyword)
        for ele in keyword:
            file.write(str(ele) + '\n')


file.close()
