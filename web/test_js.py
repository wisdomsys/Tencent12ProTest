#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-23 15:21 
'''
from time import sleep

from web.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('selenium')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(3)
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        # for code in [
        #     'return document.title',
        #     'return JSON.stringify(performance.timing)',
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)', ))

    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        sleep(3)
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
