

# 类代表是哪个接口资源，每个方法，代表对此资源的操作，比如 get、post等
# 在类服务中继承resource，表示使用flask-restful
from flask import request
from flask_restful import Resource

from backend.models.testcases import Testcase
from backend.server import app, db


class TestCaseService(Resource):
    """
    测试用例服务
    """

    # 方法名，对应 app.route中的methods
    def get(self):
        """
        查询接口，查询用例数据信息
        """
        # request 获取 接口发过来的请求信息
        case_id = request.args.get("id")
        if case_id:
            # 当传入caseID时，查询单条数据信息
            case_data = Testcase.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            # data = [{"id": case_data.id, "nodeid": case_data.nodeid, "remark": case_data.remark}]
            data = [case_data.as_dict()]
        else:
            # 反之查询所有的用例信息
            case_data = Testcase.query.all()
            # data = [{"id": i.id, "nodeid": i.nodeid, "remark": i.remark} for i in case_data]
            data = [i.as_dict() for i in case_data]
        return {"error": 0, "msg": {"data": data}}


    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口中拿到的字典数据进行解包，使用关键字传参传入Testcase
        testcase = Testcase(**case_data)
        # 如果数据字段存在列表，需要做一次转换
        # 每次如果dumps，那么字符串会添加""
        # testcase.nodeid = json.dumps(request.json.get("nodeid"))

        db.session.add(testcase)
        db.session.commit()
        # 关闭当前的session连接
        db.session.close()
        return {"error": 0, "msg": "post success"}

    def put(self):
        """
        修改接口信息
        :return:
        """
        app.logger.info(request.json)
        # 获取被修改的接口信息
        case_id = request.json.get("id")
        # 通过id 找到要修改的内容， 然后通过update修改对应的数据
        # 找到被修改的接口信息然后做修改操作
        case = Testcase.query.\
            filter_by(id=case_id).\
            update(request.json)
        app.logger.info(f"数据已修改，id{case}被修改为{request.json}")
        # 返回被修改数据的id
        # 修改之后commit到数据库
        db.session.commit()
        # 关闭当前的session连接
        db.session.close()

        return {"error": 0, "msg": {"id": case}}


    def delete(self):
        """
        删除操作
        :return:
        """
        case_id = request.args.get("id")
        if not case_id:
            return {"error": 40001, "msg": "Delete case_id can't be null"}
        # 返回一个主键
        case = Testcase.query.filter_by(id=case_id).delete()
        db.session.commit()
        db.session.close()

        app.logger.info(case)
        return {"error": 0, "msg": {"id": case}}
