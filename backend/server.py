

from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


# 类代表是哪个接口资源，每个方法，代表对此资源的操作，比如 get、post等
# 在类服务中继承resource，表示使用flask-restful
class TestCaseService(Resource):
    """
    测试用例服务
    """
    # 方法名，对应 app.route中的methods
    def get(self):
        # flask 内部自带的日志打印
        app.logger.warning("get success")
        app.logger.info("get success")
        return {"error": 0, "msg": "get success"}

    def post(self):
        return {"error": 0, "msg": "post success"}

    def put(self):
        return {"error": 0, "msg": "put success"}

    def delete(self):
        return {"error": 0, "msg": "delete success"}

class TaskService(Resource):
    pass



if __name__ == '__main__':
    # 把服务添加到app flask 中
    # 第一个参数是添加的接口服务， 第二个参数，是指定对应接口服务使用的路由
    api.add_resource(TestCaseService, "/testcase")
    api.add_resource(TaskService, "/task")
    app.run(debug=True)
