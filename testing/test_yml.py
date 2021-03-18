#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Tencent12ProTest 
@File    ：test_yml.py
@Author  ：joseph
@Date    ：2021-03-17 17:07 
'''
import yaml

with open('dates/work.yml') as f:
    print(yaml.safe_load(f))

