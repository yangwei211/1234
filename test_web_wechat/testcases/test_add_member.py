from test_web_wechat.page.add_member import AddMemberPage
from test_web_wechat.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """


    def test_add_member(self):
        main_page = MainPage()
               # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
        main_page.goto_add_member().add_member().get_contact_list()

    def test_xxx(self):
        main_page = MainPage()
        main_page.goto_add_member().add_xxx().add_member()