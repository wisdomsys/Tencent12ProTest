#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-23 20:26
"""
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        # 为什么有WebDriver  语法注释的原因
        self._driver = driver

    def register(self):
        # send content
        # click element
        sleep(3)
        self._driver.find_element_by_id('corp_name').send_keys('robot')
        self._driver.find_element_by_id('manager_name').send_keys('robot_admin')
        sleep(5)
        self._driver.quit()
        return True
