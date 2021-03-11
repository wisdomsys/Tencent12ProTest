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
    def setup(self):
        self.calc = Calc()

    def test_cap(self):
        result = self.calc.add(2, 2)
        assert 4 == result

    # @pytest.mark.run(order=3)
    def test_add(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    # @pytest.mark.run(order=2)
    def test_div(self):
        result = self.calc.div(2, 2)
        assert 1 == result

    # @pytest.mark.run(order=2)
    def test_cap_1(self):
        result = self.calc.add(2, 2)
        assert 4 == result


# pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])
if __name__ == '__main__':
    pytest.main()
