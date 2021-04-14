import pytest
import yaml

from UI自动化测试框架.page.app import App


class TestMAin:
    @pytest.mark.parametrize('value1,value2', yaml.safe_load(open('./test_main.yaml')))
    def test_main(self, value1, value2):
        app = App()
        app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_windows(self):
        app = App()
        app.start().main().goto_windows()
