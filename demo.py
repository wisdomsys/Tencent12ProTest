# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
#
# f = foo()
# print(next(f))
# print('**' * 20)
# print(next(f))


class A:
    def __init__(self):
        self.__name = 'python'


class B(A):
    def fun(self):
        print(self.__name)


b = B()
b.fun()

"""
其实，Python并没有真正的私有化支持，但可用下划线得到伪私有。   尽量避免定义以下划线开头的变量！
（1）_xxx      "单下划线 " 开始的成员变量叫做保护变量，意思是只有类实例和子类实例能访问到这些变量，
需通过类提供的接口进行访问；不能用'from module import *'导入
（2）__xxx    类中的私有变量/方法名 （Python的函数也是对象，所以成员方法称为成员变量也行得通。）,
" 双下划线 " 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
（3）__xxx__ 系统定义名字，前后均有一个“双下划线” 代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数
"""