from backend.server import db


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {"id": self.id,
                "nodeid": self.nodeid,
                "remark": self.remark}

if __name__ == '__main__':
    db.create_all()
