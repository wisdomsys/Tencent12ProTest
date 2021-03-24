#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-24 11:13
"""
import shelve
from time import sleep
from selenium.webdriver.common.by import By
from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # 点击添加成员
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMember(self._driver)

    def goto_menu_contacts(self):
        self.find(By.ID, 'menu_contacts').click()

        # locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # self.wait_for_click(locator)

        # 方法二：
        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len < 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0

        self.wait_for_element(wait_add_member)

        return AddMember(self._driver)
