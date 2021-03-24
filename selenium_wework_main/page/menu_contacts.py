#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-24 15:36 
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.add_member import AddMember


class MenuContacts:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def menu_contacts(self):
        # self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()

        return AddMember(self._driver)
