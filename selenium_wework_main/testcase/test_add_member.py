#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-24 11:46 
'''
from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        assert 'joseph' in add_member.get_member()
