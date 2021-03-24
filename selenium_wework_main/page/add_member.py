#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-24 11:36
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        # send_keys
        sleep(1)
        self.find(By.ID, 'username').send_keys('alex')
        self.find(By.ID, 'memberAdd_acctid').send_keys('alex')
        self.find(By.ID, 'memberAdd_phone').send_keys('13788979100')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        return True

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
        lists = [element.get_attribute('title') for element in elements]
        print(lists)
        return lists
