from service.wework_api import WeWork


class TestWeWork:
    # pytest识别是否是测试方法的时候，会排除带有初始化方法的类，所以不能加__init__
    # def __init__(self):
    #     self.token=""

    def setup_class(self):
        self.wework = WeWork()
        self.wework.get_token()
        raise Exception("error")

    def test_search(self):
        r = self.wework.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐） 2.使用时间戳代表唯一性
        r = self.wework.add(tag_name="tag_052001", group_name="tag_group_052001")
        assert r.json()['errcode'] == 0

        # todo：代码冗余
        r = self.wework.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # todo: 判断新增内容是否在search结果里

        r = self.wework.delete("xxxxx")
        assert r.json()['errcode'] == 0
        r = self.wework.search()
        # todo: 业务逻辑验证 判断删除的内容是否已经消失在search结果里
