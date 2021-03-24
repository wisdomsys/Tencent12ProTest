#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-23 20:23 
'''
from selenium import webdriver

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


# 首页
class Index:
    def __init__(self):
        # 初始化driver
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        #  去登录页面
        # click login
        self._driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self._driver)

    def goto_register(self):
        # 去注册页面
        # click register
        self._driver.find_element_by_xpath('//*[@id="tmp"]/div[1]/a').click()
        return Register(self._driver)
