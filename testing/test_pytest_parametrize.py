#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_pytest_parametrize.py
@Author  ：joseph
@Date    ：2021-03-17 14:40 
'''
import pytest

from python.calc import Calc
from decimal import Decimal


class TestParametrize:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    @pytest.mark.parametrize('data1,data2,expect', [(1, 2, 3), (0.1, 0.2, 0.3), (0, 1, 1)])
    def test_add_1(self, data1, data2, expect):
        result = self.calc.add(data1, data2)
        print(result)
        assert expect == Decimal(result)

    def test_div(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result
