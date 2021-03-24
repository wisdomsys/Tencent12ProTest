#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-24 11:13
"""
import shelve
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage
from selenium_wework_main.page.menu_contacts import MenuContacts


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # 点击添加成员
        self._driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMember(self._driver)

    def goto_menu_contacts(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)
