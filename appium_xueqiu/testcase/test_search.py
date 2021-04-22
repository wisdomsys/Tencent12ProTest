import pytest

from appium_xueqiu.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    @pytest.mark.parametrize('name', ['阿里巴巴', '京东'])
    def test_search(self, name):
        self.search.search(name)
        assert self.search.is_choose(name)
