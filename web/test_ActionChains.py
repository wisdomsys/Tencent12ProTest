#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_ActionChains.py
@Author  ：joseph
@Date    ：2021-03-22 17:15
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 参考
# https://blog.csdn.net/huilan_same/article/details/52305176

class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        element_double_click = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        element_right_click = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        action.perform()

    def test_moveto_element(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        dragdrop = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        dragdrop_to = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(dragdrop, dragdrop_to).perform()
        # action.click_and_hold(dragdrop).release(dragdrop_to).perform()
        action.click_and_hold(dragdrop).move_to_element(dragdrop_to).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        action = ActionChains(self.driver)
        ele.click()
        action.send_keys('joseph')
        action.send_keys(Keys.SPACE)  # 加入空格
        action.send_keys('beer')
        action.send_keys(Keys.BACK_SPACE).pause(1)  # 删除一格
        action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND)  # 全选
        action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND)  # 拷贝
        mv = self.driver.find_element(By.XPATH, '/html/body/label[2]/table/tbody/tr/td[2]/input')
        action.key_down(Keys.COMMAND, mv).send_keys('v').key_up(Keys.COMMAND).perform()  # 复制
        sleep(3)

# if __name__ == '__main__':
#     pytest.main('-v', '-s', 'test_ActionChains.py')
