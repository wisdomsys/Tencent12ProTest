from appium_xueqiu.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search().search()

    def test_search(self):
        self.search.search()
        assert self.search.is_choose()

