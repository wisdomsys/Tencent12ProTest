#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_calc.py
@Author  ：joseph
@Date    ：2021-03-11 09:55
"""
import sys

sys.path.append('..')
from python.calc import Calc
import unittest


class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
