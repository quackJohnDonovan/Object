# 面向对象

# 定义父类：登录界面
class login_interface():
    # 类函数
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 类方法
    def login(self):
        print("用户名：" + self.username)
        print("密码：" + self.password)


# 定义子类：简易注册界面
class register_low(login_interface):
    def __init__(self, username, password, email):
        login_interface.__init__(self, username, password)
        self.email = email

    def register(self):
        login_interface.login(self)
        print("邮箱：" + self.email)


# 定义二级子类：进阶注册界面
class register_high(register_low):
    def __init__(self, username, password, email, confirm_password, verification_code):
        register_low.__init__(self, username, password, email)
        self.confirm_password = confirm_password
        self.verification_code = verification_code

    def register(self):
        register_low.register(self)
        print('确认密码：' + self.confirm_password)
        print('验证码：' + self.verification_code)


# 调用子类
if __name__ == '__main__':
    # 定义参数
    username = 'user1'
    password = '123456'
    confirm_password = '123456'
    email = '1725439953@qq.com'
    verification_code = 'abcde'

    # 调用二级子类
    register_high_Obj = register_high(username, password, email, confirm_password, verification_code)
    register_high_Obj.register()
