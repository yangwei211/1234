import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
# 解决跨域
CORS(app, supports_credentials=True)
username = "root"
pwd = "123456"
ip = "134.175.28.202"
port = "8888"
database = "test_ck18"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning 问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

def router():
    """
    路由管理
    :return:
    """
    from backend.apis.testcases import TestCaseService
    api.add_resource(TestCaseService, "/testcase")




if __name__ == '__main__':
    # 把服务添加到app flask 中
    # 第一个参数是添加的接口服务， 第二个参数，是指定对应接口服务使用的路由
    # db.create_all()
    # api.add_resource(TaskService, "/task")
    app.run(debug=True)
