from test_web_wechat.page.contact import ContactPage


class AddMemberPage:

    def add_member(self):

        # 页面的return 分成两个部分
        # 1. 其他页面的 实例
        # 2. 用例所需要的断言
        # 注意： 不要写成 ContactPage
        # 快捷导入  alt + 回车
        return ContactPage()

    def add_xxx(self):
        # 调用本身的实例
        # AddMemberPage()
        return self

