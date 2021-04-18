from test_web_wechat.page.add_member import AddMemberPage


class MainPage:
    """
    用公共方法代表UI所提供的功能
    """
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        pass

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 返回要跳转页面的实例对象
        return AddMemberPage()

