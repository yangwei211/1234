from jenkinsapi.jenkins import Jenkins
class ExecuteTools:
    # jenkins的服务地址
    BASE_URL = "http://134.175.28.202:8081/"
    # 用户名
    USERNAME = "admin"
    # 使用Jenkins生成的token
    PASSWORD = "1178bda522b3ac867e4a2dbdfcb0cd590d"
    JOB_NAME = "ck18"
    @classmethod
    def get_jobs(cls):
        # 实例化jenkins
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 返回所有的job名称
        return jenkins.keys()

    @classmethod
    def invoke(cls, task):
        """
        调用执行器执行
        task: 指定执行的用例
        :return: 报告链接
        """
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 得到ck18job的实例对象
        job_ck18 = jenkins.get_job(cls.JOB_NAME)
        # 让你的job 进行构建, 需要和jenkins的job的参数名进行对应
        job_ck18.invoke(build_params={"task": task})
        # 1. Jenkins 自动生成Junit.xml 报告，拿到之后解析xml文件，获取用例执行的信息
        # 2. 拿到allure 的数据信息，解析json文件，获取用例的执行
        # 3. 直接拿到allure 的链接，就是allure的报告信息
        # http://134.175.28.202:8081/job/ck18/9/allure/
        # jenkins服务的信息/job/jobname/构建的数据/allure/
        # 构建完成立刻获取到的构建数
        # http://134.175.28.202:8081/job/ck18/43/allure/
        last_build_number = job_ck18.get_last_buildnumber()
        # print(last_build_number)
        while True:
            build_number = job_ck18.get_last_buildnumber()
            if last_build_number != build_number:
                # 拼接报告路径
                report_path = cls.BASE_URL+"job/"+cls.JOB_NAME+"/"+\
                              str(build_number)+"/allure"
                return report_path




