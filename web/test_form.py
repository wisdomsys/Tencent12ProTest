#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_form.py
@Author  ：joseph
@Date    ：2021-03-23 10:30 
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrom:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element(By.XPATH, '//*[@id="user_login"]').send_keys('123')
        self.driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys('password')
        self.driver.find_element(By.XPATH, '//*[@id="user_remember_me"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="new_user"]/div[4]/input').click()
        sleep(3)