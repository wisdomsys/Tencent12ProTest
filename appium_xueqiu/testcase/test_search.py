from appium_xueqiu.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    def test_search(self):
        self.search.search('alibaba')
        assert self.search.is_choose('阿里巴巴')

