import datetime

from backend.server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 任务执行的相关数据信息
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
                        # 指定时间格式， 默认值为当前时间
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {"id": self.id,
                "remark": self.remark,
                "report": self.report,
                # 强转为字符串的格式
                "create_at": str(self.create_at)}

if __name__ == '__main__':
    db.create_all()
