'''

 3位水仙花数计算：“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。（编程题）

请按照从小到大的顺序输出所有的3位水仙花数
'''


# num1 = 4
# num2 = 5
# num3 = 6
# a = num1**3 + num2**3 + num3**3
# print(a)
# b = int(str(num1)+str(num2)+str(num3))
# print(b)


# 三位数轮巡检查
for num1 in range(1,10):
    for num2 in range(0, 10):
        for num3 in range(0, 10):

            # 定义参数
            a = num1 ** 3 + num2 ** 3 + num3 ** 3
            b = int(str(num1) + str(num2) + str(num3))

            # 判断是否相等
            if a == b:
                # 输出3位水仙花数
                print(b)
                print('\n')