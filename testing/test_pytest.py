#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_pytest.py
@Author  ：joseph
@Date    ：2021-03-11 10:59
"""
from python.calc import Calc
import pytest


class TestCalc:
    def __init__(self):
        self.calc = Calc()

    def setUp(self) -> None:
        pass

    def test_add(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    def test_div(self):
        result = self.calc.div(2, 2)
        assert 1 == result


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])
