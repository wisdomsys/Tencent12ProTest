#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：base.py
@Author  ：joseph
@Date    ：2021-03-23 11:39 
'''
from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()