


from flask import Flask, request


app = Flask(__name__)

# 查询接口
@app.route("/testcase", methods = ["get"])
def get_case():
    # flask 内部自带的日志打印
    app.logger.warning("get success")
    app.logger.info("get success")
    return {"error": 0 , "msg": "get success"}
# 新增接口
@app.route("/testcase", methods = ["post"])
def post_case():
    return {"error": 0, "msg": "post success"}
# 修改接口
@app.route("/testcase", methods = ["put"])
def put_case():
    return {"error": 0, "msg": "put success"}

# 删除接口
@app.route("/testcase", methods = ["delete"])
def delete_case():
    return {"error": 0, "msg": "delete success"}

if __name__ == '__main__':
    app.run(debug=True)
