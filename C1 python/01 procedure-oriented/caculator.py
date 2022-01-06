'''
简易计算器
面向过程已封装

版本：
1.0完成流程设计         2021/04/27
2.0完成面向过程封装      2021/04/27
'''

'''
1.0版本

#绘制界面


def calc_GUI():

    print('***************************')
    print('*        1   加法运算       *')
    print('*        2   减法运算       *')
    print('*        3   乘法运算       *')
    print('*        4   除法运算       *')
    print('***************************')


#输入两个数

x = int(input("请输入一个数"))
y = int(input('再输入一个数'))


#输入菜单编号
num = int(input('请输入菜单编号'))
#判断编号执行相应判断

if num == 1:
    sum = x+y
elif num == 2:
    sum = x-y
elif num == 3:
    sum = x*y
elif num == 4:
    sum = x/y
else:
    print('输入菜单编号错误')
#输出结果
print('结果为'+str(sum))

'''


#2.0版本


#实现界面功能

def calc_GUI():
        #绘制计算器图形界面
    print('***************************')
    print('*        1   加法运算       *')
    print('*        2   减法运算       *')
    print('*        3   乘法运算       *')
    print('*        4   除法运算       *')
    print('***************************')


# 实现数据输入
def calc_DATA():
    list = []
        # 输入两个数
    x = int(input("请输入一个数"))
    y = int(input('再输入一个数'))
        # 输入菜单编号
    num = int(input('请输入菜单编号'))
    list.append(x)
    list.append(y)
    list.append(num)

    return list

# 实现运算并输出结果
def calc_result(x,y,num):
    # 判断编号执行相应判断

    if num == 1:
        sum = x + y
    elif num == 2:
        sum = x - y
    elif num == 3:
        sum = x * y
    elif num == 4:
        sum = x / y
    else:
        print('输入菜单编号错误')
    # 输出结果
    print('结果为' + str(sum))

# 通过主函数调用方法
if __name__ == '__main__':
    #调用绘制菜单方法
    a = []
    calc_GUI()
    a = calc_DATA()
    calc_result(a[0],a[1],a[2])
