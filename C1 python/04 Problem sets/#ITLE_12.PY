class calc_area():
    # 定义主参数：长和宽
    def __init__(self,long,wide):
        self.long = long
        self.wide = wide

    # 定义方法：面积计算
    def calc(self):
        # 计算
        area = self.long * self.wide
        # 结果输出
        print(str(self.long)+'乘以'+str(self.wide)+'得到的面积等于'+str(area))

if __name__ == '__main__':

    # 用户输入长和宽
    long = int(input("请输入长度:\n"))
    wide = int(input("请输入宽度:\n"))

    # 实例化类
    calcObj = calc_area(long,wide)
    # 调用方法
    calcObj.calc()