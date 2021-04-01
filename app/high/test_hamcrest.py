import pytest
from appium import webdriver
from hamcrest import assert_that, equal_to, close_to


class TestHamcrest:

    def test_hamcrest(self):
        # assert_that(10, equal_to(10),'这是一个提示')
        assert_that(13, close_to(10,2),'这是一个提示')   # 接近
