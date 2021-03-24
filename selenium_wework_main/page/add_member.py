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
        self.find(By.ID, 'username').send_keys('alex')
        self.find(By.ID, 'memberAdd_acctid').send_keys('alex')
        self.find(By.ID, 'memberAdd_phone').send_keys('13788979100')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, 'ww_pageNav_info_text').text  # 获取页码
        return [int(x) for x in content.split('/', 1)]  # 提取页码

    def get_member(self, value):
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))  # 显示等待，获取按钮是否加载成功，加载成功变相说明下面的用户信息加载完成
        cur_page, total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')  # 获取用户名字
            for element in elements:
                if value == element.get_attribute('title'):
                    return True
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, '.js_next_page').click()
