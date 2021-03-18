#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_yield.py
@Author  ：joseph
@Date    ：2021-03-18 10:56
"""


# yield + 函数 == 生成器

def provider():
    for i in range(5):
        print(f'before:{i}')
        yield i  # 生成器类似于return + 暂停 并且记住了上一步的操作
        print(f'after:{i}')


p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
