import sys


class calc_MN():
    # 定义主参数：M和N
    def __init__(self,M,N):
        self.M = M
        self.N = N

    # 定义方法：5种数学运算
    def calc(self):
        # 计算
        result_compare = bool(self.M > self.N)
        if result_compare:
            result_compare = self.M
        else:
            if self.M == self.N:
                result_compare = str(self.M)+'和'+str(self.N)+'一样大'
                print(result_compare)
                sys.exit()
            else:
                result_compare = self.N

        # 结果输出
        print(str(self.M) + '与' + str(self.N) + '较大的数是' + str(result_compare))


if __name__ == '__main__':

    # 用户输入M和N
    M = int(float(input("请输入一个整数:\n")))
    N = int(float(input("请再输入一个整数:\n")))

    # 判断类型
    if type(M) == int and type(N) == int:
        # 实例化类
        calcObj = calc_MN(M, N)
        # 调用方法
        calcObj.calc()
