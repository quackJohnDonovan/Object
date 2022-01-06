'''
折半查找
面向过程已封装

版本：
1.0完成流程设计         2021/04/25
2.0完成面向过程封装      2021/04/27
'''

#数据输入
def binary_DATA():
    #输入一个数
    a = int(input('请输入数字'))
    return a


#进行查找
def binary_execute(a):
    list = []

    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

    l = len(list2)
    left = 0
    right = l - 1
    mid = (left + right) // 2
    i = 0

    while (left <= right):
        i = i + 1
        if a > list2[mid]:
            left = mid + 1
        elif a < list2[mid]:
            right = mid - 1
        else:
            print('第', i, '次就找到了')

            a = 1
            list.append(a)
        mid = (left + right) // 2
#        print('新的中间位置为', mid, left, right, '元素值为', list2[mid])

    if left > right:

        b = 0
        list.append(b)

    return list


#输出结果
def binary_result(result):
    #结果判断
    if result == 1:
        print('找到该数字')
    else:
        print('这个数不存在')


#执行脚本
if __name__ == '__main__':
    a=binary_DATA()
    list = []
    list = binary_execute(a)
    binary_result(list[0])