# 用于链接数据库, 创建数据库

from pymongo import MongoClient


class BaseMonGo:
    def __init__(self, basename, formname, **kwargs):
        """
        :param basename: 数据库名称
        :param formname: 数据库表单名称
        :param kwargs:   account  账号
                         password 密码
                         host 远端地址
                         port 远端端口
        """
        self.formname = formname
        account = kwargs.get('account')
        password = kwargs.get('password')
        host = kwargs.get('host')
        port = int(kwargs.get('port')) if kwargs.get('port') else None
        k = [i for i in kwargs if kwargs[i]]
        if len(k) == 4:
            self.client = MongoClient(host=host, port=port)
            self.db = self.client[basename]
            self.db.authenticate(account, password)
        elif 0 < len(k) < 4:
            raise ValueError('使用远程链接, account, password, host, port 都不能为空')
        else:
            self.client = MongoClient('127.0.0.1', 27017)
            self.db = self.client[basename]

    def login_base(self):
        """
        链接数据库
        :return: 数据库实例
        """
        db = self.db
        return db[self.formname]


# 所有数据库在此下方创建实例
pass