#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Date    ：2021-03-23 16:01
"""
from time import sleep

from web.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('/Users/joseph/PycharmProjects/Tencent12ProTest/web/wechart.png')
        sleep(3)
