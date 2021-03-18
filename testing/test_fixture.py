#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_fixture.py
@Author  ：joseph
@Date    ：2021-03-18 10:43 
'''
import pytest


@pytest.fixture()
def login():
    print('需要登录')
    username = ''
    yield username
    print('执行teardown')


class TestDemo:
    # def setup_class(self):
    #     # 第一步打开浏览器
    #     print('setup_class>>第一步打开浏览器')
    #
    # def setup(self):
    #     print('setup>>>')
    #
    # def teardown(self):
    #     print('teardown>>>')
    #
    # def teardown_class(self):
    #     # 关闭浏览器
    #     print('teardown_class>>>关闭浏览器')

    def test_a(self, login):
        # 输入网址
        # 定位
        # 操作
        # 关闭浏览器
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')
