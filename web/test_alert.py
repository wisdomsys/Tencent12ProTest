#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-23 16:19 
'''
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from web.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        draggable = self.driver.find_element_by_id('draggable')
        droppable = self.driver.find_element_by_id('droppable')

        # ActionChains
        # 方法一
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable).perform()
        # 方法二
        # action.click_and_hold(draggable).release(droppable).perform()
        # 方法三
        # action.click_and_hold(draggable).move_to_element(droppable).release().perform()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.parent_frame()
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]').click()
        # action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
        # action.key_down(Keys.COMMAND).send_keys('x').key_up(Keys.COMMAND).perform()
        # action.send_keys('<h1>恭喜试验成功！</h1>').perform()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
        sleep(3)
