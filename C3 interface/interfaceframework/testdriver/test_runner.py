import csv
import operator

# list1 = [{"testA": "C:\cc\cc", "num": 3}, {"testC": "C:\cc\cc", "num": 1}, {"testB": "C:\cc\cc", "num": 2}]
# list2 = sorted(list1, key=operator.itemgetter("num"))
# print(list2)
#
# for i in range(0, 3):
#     # print(list2[i])
#     n = 0
#     for content in list2[i].items():
#         if n == 0:
#             print(content[0])
#             print(content[1])
#             n+=1

file = open(r"C:\Users\何冰\Desktop\Object\C3 interface\interfaceframework\config\config.csv", "r")
table = csv.reader(file)
dic = {}
list = []
n = 0
for row in table:
    # print(row)
    if n > 0:
        dic = {}
        dic[row[1]] = row[0]
        dic["num"] = row[3]
        n += 1
        # print(dic)
    else:
        n += 1
        pass

    if dic != {}:
        list.append(dic)
# print(list)

list1 = sorted(list, key=operator.itemgetter("num"))
print(list1)

for i in range(0, 2):
    # print(list2[i])
    n = 0
    for content in list1[i].items():
        if n == 0:
            print(content[0])
            print(content[1])
            n+=1