# 不带参数的装饰器

def func(func1):
    def func2():
        func1()
        print('func2')

    return func2


@func
def func1():
    print('func1')


# 带参数的装饰器
def deco_va(func):
    def wrapper(user, pwd):
        if user == 'root' and pwd == 'root':
            func(user, pwd)
        else:
            print('用户名或密码错误')

    return wrapper


@deco_va
def baidu_index(username, password):
    print('welcome to 百度')


# 多层装饰器
def deco1(deco):
    print('你好不好？')

    def deco(func):
        def func2():
            print('你不好！')
            func()

        return func2

    return deco


@deco1
def deco(func):
    def func2():
        print('你不好！')
        func()

    return func2


@deco
def func1():
    print('你好！')


if __name__ == '__main__':
    func1()
