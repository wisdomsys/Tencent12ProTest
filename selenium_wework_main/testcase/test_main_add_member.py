#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-24 15:41 
'''
from time import sleep

from selenium_wework_main.page.main import Main


class TestMainAddMembers:
    def setup(self):
        self.main = Main()

    def test_main_addmember(self):
        sleep(2)
        add_member = self.main.goto_menu_contacts()
        add_member.add_member()
        assert 'alex' in add_member.get_member()
