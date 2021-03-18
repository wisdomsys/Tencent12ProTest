#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_work.py
@Author  ：joseph
@Date    ：2021-03-17 17:42 
'''

# 使用测试数据的数据驱动(参数化) 完成加法和除法
# 修改运算规则，pytest.ini文件(只识别add_div_开头的方法)
# 自动添加mark标签，只运行add开头的方法
import pytest

from python.calc import Calc
import yaml


def steps():
    with open('dates/steps.yml') as f:
        return yaml.safe_load(f)


class Test_Work_add_div:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('dates/work.yml')))
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    # 测试步骤的数据驱动
    # @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('dates/work.yml')))
    # def test_add1(self, a, b, expect):
    #     steps1 = steps()
    #     for step in steps1:
    #         print(f'step ===>{step}')
    #         if 'add' == step:
    #             result = self.calc.add(a, b)
    #         elif 'add1' == step:
    #             result1 = self.calc.add(a, b)
    #         print(result)
    #     assert expect == result

    # def test_div(self, a, b, expect):
    #     result = self.calc.add(a, b)
    #     assert expect == result
