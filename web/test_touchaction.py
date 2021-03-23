#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_touchaction.py
@Author  ：joseph
@Date    ：2021-03-23 09:44
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_scroll_bottom(self):
        """
        打开浏览器
        打开url：https://www.baidu.com/
        向搜索框输入'selenium测试'
        通过TouchAction 点击搜索框
        滑动到底部，点击下一页
        关闭浏览器
        """
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('selenium测试')
        action = TouchActions(self.driver)
        search = self.driver.find_element(By.XPATH, '//*[@id="su"]')
        action.tap(search).perform()
        action.scroll_from_element(search, 0, 1400).perform()
        try:
            self.next_page = self.driver.find_element(By.CSS_SELECTOR, '#page > div > a.n')
        except AttributeError:
            self.next_page.click()
            sleep(3)
        else:
            return False
