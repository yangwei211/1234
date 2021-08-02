from flask import request
from flask_restful import Resource

from backend.models.task import Task
from backend.server import app, db
from backend.utils.execute_tools import ExecuteTools


class TaskService(Resource):
    def post(self):
        """
        1. 调用jenkins执行用例
        2. 执行用例之后，写入执行记录到数据库
        :return:
        """
        # 具体执行的用例从post请求的信息，请求体中获取
        data = request.json
        #从前端拿到的数据类型 [{'id': 2, 'nodeid': 'test_setup_teardow.py', 'remark': '0'}]
        nodeids = [i["nodeid"] for i in data]
        # ['test_setup_teardow.py', 'test_order.py']
        # 转换为"test_setup_teardow.py test_order.py"
        # 方便 pytest执行 test_setup_teardow.py test_order.py
        nodeids = " ".join(nodeids)
        app.logger.info(f"执行的用例为{nodeids}")
        # # 调用jenkins执行测试用例
        report = ExecuteTools.invoke(nodeids)
        # 对task 数据库做写入操作
        app.logger.info(f"添加一条task，报告为{report}，执行用例为{nodeids}")
        # 没有传主键， 因为主键会自动生成，所以不传递也可以，
        # 没有传创建时间， 因为创建时间有默认时间
        task = Task(remark=nodeids, report=report)
        db.session.add(task)
        db.session.commit()
        db.session.close()
        return {"error": 0, "msg": "ok"}

    def get(self):
        """
        获取任务列表
        :return:
        """
        # 查询task所有的数据
        tasks = Task.query.all()
        # as dict 把对象转为python 字典格式，后面flask好解析
        tasks_data = [task.as_dict() for task in tasks]
        app.logger.info(f"获取到的任务列表为{tasks_data}")
        # 接口的响应数据
        return {"error": 0, "msg": {"data": tasks_data}}
