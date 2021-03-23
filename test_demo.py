#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Date    ：2021-03-23 17:46 
'''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click() print(self.driver.get_cookies())
        # cookies = [ {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
        # 'secure': False, 'value': '1688851091831392'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
        # 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value':
        # 'h01SLDrllL-LhAA4HazmXfaGo1GP21A6lErkQbhkoucXJQm
        # -tXJ14AXSE10E3Tkq8PRtYUvXdjSFhGYxb2togHWvCSWMPKG47CCsZ5aStYgulkibKtQObuLcsM3ul
        # -E2vEPiZzxM86w7I8LKqWI3G4SRiU04nwAFYzljxsM32pyblWW9Ig_98S02tvlEwnm6DTT3LFsq3D27zlH15NaBt83ah1T8Wj
        # -0ZJysFy138Kn6kxTcRHHOxvRptcpStNziShHyv0RKRZ-3HYNyCa2QBA'}, {'domain': '.work.weixin.qq.com', 'httpOnly':
        # False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851091831392'}, {'domain':
        # '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        # 'value': '1970325033440310'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st',
        # 'path': '/', 'secure': False, 'value': 'a1905905'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
        # 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value':
        # 'lRyAdBpmRp08GRSzDyXtQee3gZ8DNpwh6SUeD0xs7-veWuGF04Rshnu31tn-RL5u'}, {'domain': '.work.weixin.qq.com',
        # 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain':
        # '.work.weixin.qq.com', 'expiry': 1648029440, 'httpOnly': False, 'name':
        # 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1616491295,1616493440'},
        # {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        # 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
        # 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1616493440'},
        # {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        # 'value': '26398760583435289'}, {'domain': '.qq.com', 'expiry': 1616579935, 'httpOnly': False,
        # 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1922624811.1616491295'}, {'domain':
        # 'work.weixin.qq.com', 'expiry': 1616522830, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        # 'secure': False, 'value': '21c9i07'}, {'domain': '.qq.com', 'expiry': 1679565535, 'httpOnly': False,
        # 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2061987086.1616491295'}, {'domain':
        # '.work.weixin.qq.com', 'expiry': 1648027294.123, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
        # 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1619086911, 'httpOnly': False,
        # 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 类似于数据库
        db = shelve.open('cookies')
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            # 这是解决报的 Message: invalid argument: invalid 'expiry',expiry参数有小数
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(2)
        db.close()


