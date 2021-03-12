def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


f = foo()
print(next(f))
print('**' * 20)
print(next(f))
