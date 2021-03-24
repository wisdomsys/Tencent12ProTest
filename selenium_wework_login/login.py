#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-23 20:24
"""
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        # 为什么有WebDriver  语法注释的原因
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        self._driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        sleep(2)
        return Register(self._driver)
