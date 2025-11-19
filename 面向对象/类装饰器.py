class Klass:
    @classmethod
    def funcs(cls):
        """
        classmethod 可以实例的方法定义为类的方法，用于类直接调用，不需要实例化
        :return:
        """
        print('class method')

    @staticmethod
    def func():
        """
        staticmehtod 不需要类的任何信息但又和类相关的一些方法
        为了方便维护代码并保持代码工整，可以将该函数定义到类中并
        使用staticmethod 装饰
        :return:
        """
        print('static')

    @property
    def funcsv(self):
        return self.__varName

    @funcsv.setter
    def funcsv(self, varValue):
        self.__varName = varValue


#
# demo1 = Klass()
#
# demo1.funcs()
#
# Klass.funcs()
#
# demo1.funcsv = '123'
#
# print(demo1.funcsv)


# 练习

class UserClass:

    def __init__(self):
        self.__userData = None

    @property
    def getUserInfo(self):
        if self.__userData is None:
            with  open('userData.txt', mode='r') as User:
                filedata = User.read()
                self.__userData = filedata

        return self.__userData

    @getUserInfo.setter
    def userData(self, _insertData):
        with open('userData.txt', mode='r+') as User:
            User.write(_insertData)
            printdata = User.read()
            print(printdata)


demo2 = UserClass()

print(demo2.userData)

demo2.userData = '123_user'

print(demo2.userData)
