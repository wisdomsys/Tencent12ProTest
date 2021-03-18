#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_hogwards.py
@Author  ：joseph
@Date    ：2021-03-18 17:01 
'''

from selenium import webdriver
from time import sleep


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/li[3]/a').click()
        self.driver.find_element_by_xpath('//*[@id="hot_teams"]/div[2]/div/div[9]/div/div[2]/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/a').click()
