# 装饰器原理
def extend(func):
    def hello(*args, **kwargs):
        print('hello')
        print(args)
        print(kwargs)
        func(*args, **kwargs)
        print('good bye')

    return hello


@extend
def tmp(a, b, c, d):
    print('tmp')


@extend
def tmp1(a):
    print('tmp1')


def test_wrapper():
    # tmp(1, 2, 3, d=10)
    tmp1(1)
