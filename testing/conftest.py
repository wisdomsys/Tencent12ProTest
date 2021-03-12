#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：conftest.py
@Author  ：joseph
@Date    ：2021-03-11 19:45 
'''
import pytest


def pytest_collection_modifyitems(session, config, items: list):
    # print(items)
    # print(type(items))
    # for item in items:
    #     print('这是item', item)
    #     if 'add' in item.nodeid:
    #         item.add_marker(pytest.mark.add)
    #     elif 'div' in item.nodeid:
    #         item.add_marker(pytest.mark.div)

    items.reverse()
