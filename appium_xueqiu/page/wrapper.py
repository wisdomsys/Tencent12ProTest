import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, '//*[@text="确定"]'),
            (By.XPATH, '//*[@text="允许"]'),
            (By.XPATH, '//*[@text="确认"]'),
            (By.ID, 'com.xueqiu.android:id/tv_agree'),
            (By.XPATH, '//*[@text="下次再说"]'),
        ]
        _max_num = 3
        _error_num = 0
        from appium_xueqiu.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            logging.info('run' + func.__name__ + '\n args:\n' + repr(args) + '\n' + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            # 隐式等待恢复原来的设置
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            instance.screenshot('tmp.png')
            with open('tmp.png', 'rb') as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            logging.error('element not found,handle black list')
            # 出现异常，隐式等待时间设置小一点，快速的处理弹窗
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹窗
            for ele in _black_list:
                ele_list = instance.finds(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    # 处理完弹窗再去查找元素目标
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
