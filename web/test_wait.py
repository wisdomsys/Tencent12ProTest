#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_wait.py
@Author  ：joseph
@Date    ：2021-03-18 17:42 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_wait(self):
        self.driver.find_element_by_id('ember41').click()

        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="ember524"]/div[1]/table/thead/tr/th[2]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@id="ember535"]').click()
