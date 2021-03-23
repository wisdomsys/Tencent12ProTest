#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Tencent12ProTest
@File    ：test_frame.py
@Author  ：joseph
@Date    ：2021-03-23 14:21

"""

# iframe处理
from selenium.webdriver.common.by import By

from web.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        self.driver.switch_to.parent_frame()  # 父级frame
        # self.driver.switch_to.default_content()  # 默认的frame
        print(self.driver.find_element(By.XPATH, '//*[@id="submitBTN"]').text)
