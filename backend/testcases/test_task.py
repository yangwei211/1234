import requests


class TestTask:
    """
    测试任务的接口测试用例
    """

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/task"

    def test_get_task(self):
        """
        获取任务列表的测试用例
        :return:
        """
        r = requests.get(self.base_url)
        assert r.status_code == 200

    def test_post_task(self):
        """
        新增测试任务的测试用例
        :return:
        """
        # 用例的信息
        data = [{'id': 2, 'nodeid': 'test_setup_teardow.py', 'remark': '0'}]
        r = requests.post(self.base_url, json=data)
        assert r.status_code == 200
