#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_frame.py
@Author  ：joseph
@Date    ：2021-03-23 10:40
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.base import Base


class TestFrame(Base):
    """
    打开百度
    点击登录
    弹框中点击立即注册，输入用户名和账号
    返回刚才的登录页面，点击登录
    输入用户名和密码，点击登录
    点击首页登录以后：CDwindow-96B22DA4330DAF2689D6EDA61C652676
    注册以后：CDwindow-96B22DA4330DAF2689D6EDA61C652676
    window_all:['CDwindow-96B22DA4330DAF2689D6EDA61C652676', 'CDwindow-A9962D71EDC9CA6B2B01CF1101A1530D']
    """

    def test_window(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()  # 登录
        print(f'点击首页登录以后：{self.driver.current_window_handle}')
        self.driver.find_element(By.XPATH, '//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()  # 注册
        print(f'注册以后：{self.driver.current_window_handle}')
        window_all = self.driver.window_handles
        print(f'window_all:{window_all}')
        self.driver.switch_to.window(window_all[-1])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys('register')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__password"]').send_keys('register_password')
        self.driver.switch_to.window(window_all[0])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys('1396871335@qq.com')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys('ych19951005')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(3)
