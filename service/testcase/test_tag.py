from jsonpath import jsonpath

from service.api.tag.tag import Tag
from service.api.wework_api import WeWork


class TestTag:
    # pytest识别是否是测试方法的时候，会排除带有初始化方法的类，所以不能加__init__
    # def __init__(self):
    #     self.token=""

    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear()
        # todo: 追加测试数据

    def teardown_class(self):
        # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定，尽量不要在teardown*中放入重要的逻辑。
        pass

    def test_search(self):
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group']) == 0

    def test_add(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐） 2.使用时间戳代表唯一性

        # data = {
        #     'group_name': "tag_group_052001",
        #     'tag_list': [
        #         {
        #             "name": "tag_052001"
        #         }
        #     ]
        # }
        # r=self.tag.add(data)

        tag_list = [{'name': 'tag_052001'}, {'name': 'tag_052002'}]
        r = self.tag.add(tag_list=tag_list, group_name="tag_group_052001")
        assert r.json()['errcode'] == 0

        # done：代码冗余
        r = self.tag.search()
        assert r.json()['errcode'] == 0
        assert 'tag_group_052001' in [group['group_name'] for group in r.json()['tag_group']]

        # 使用jsonpath
        tag_name_list = jsonpath(r.json(), '$..tag[*].name')
        print(tag_name_list)
        assert set(['tag_052001', 'tag_052002']) == set(tag_name_list)

    def test_order(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐） 2.使用时间戳代表唯一性

        # 明确需求，排序是后端负责还是前端（js）负责
        tag_list = [
            {'name': 'tag_0520011', 'order': 2},
            {'name': 'tag_0520012', 'order': 1},
            {'name': 'tag_0520013', 'order': 3},
        ]
        r = self.tag.add(tag_list=tag_list, group_name="tag_group_0520010")
        assert r.json()['errcode'] == 0

        # done：代码冗余
        r = self.tag.search()
        assert r.json()['errcode'] == 0

        # 使用jsonpath
        tag_name_list = jsonpath(r.json(), '$..tag[*].name')
        print(tag_name_list)

        # 前端工程师负责排序，所以不验证排序
        # assert ['tag_0520012', 'tag_0520011', 'tag_0520013'] == tag_name_list
        # 验证数据值就可以了

    def test_delete(self):
        # 删除数据与添加数据尽量区分开，失败的时候可以更好的直观看到feature失败

        # todo: 判断新增内容是否在search结果里

        r = self.tag.delete("xxxxx")
        assert r.json()['errcode'] == 0
        r = self.tag.search()
        # todo: 业务逻辑验证 判断删除的内容是否已经消失在search结果里
