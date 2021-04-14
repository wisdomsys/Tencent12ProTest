from UI自动化测试框架.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()
