'''
M与N的数学运算：用户输入两个数 M 和 N，M，N是整数，计算M 和 N 的5种数学运算结果，并依次输出，（编程题）

5种数学运算分别是：M 与 N 的和、M 与 N 的乘积、M 的 N 次幂、M除 N 的余数、M 和 N 中较大的值。
'''
class calc_MN():
    # 定义主参数：M和N
    def __init__(self,M,N):
        self.M = M
        self.N = N

    # 定义方法：5种数学运算
    def calc(self):
        # 计算
        result_add = self.M + self.N
        result_multiplication = self.M * self.N
        result_power = self.M ** self.N
        result_remainder = self.M % self.N
        result_compare = bool(self.M > self.N)
        if result_compare:
            result_compare = self.M
        else:
            if self.M == self.N:
                result_compare = 'M和N都比较大'
            else:
                result_compare = self.N

        # 结果输出
        print(str(self.M) + '与' + str(self.N) + '的和为' + str(result_add))
        print(str(self.M) + '与' + str(self.N) + '的乘积为' + str(result_multiplication))
        print(str(self.M) + '的' + str(self.N) + '次幂为' + str(result_power))
        print(str(self.M) + '与' + str(self.N) + '的余数为' + str(result_remainder))
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
