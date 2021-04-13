from test_app.page.app import App


class TestContact:
    def setup(self):
        # 实例化app 打开
        self.app = App()
        self.main = self.app.start().main()

    def test_add_contact(self):
        invite_page = self.main.goto_address_list().add_member().member_by_manul().input_name().input_mobile().\
            set_gender().click_save()
        assert '成功' in invite_page.get_toast()
