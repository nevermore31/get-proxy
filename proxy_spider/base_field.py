# 定义字段


class ProxyItem:
    """
    定义字段的基类
    """
    # 存放用于定义字段的
    field = {

    }

    def __init__(self, **kwargs):
        for k in kwargs:
            if k not in self.field:
                raise TypeError(
                    '未定义字段'
                )
        if len(self.field) == 0:
            raise TypeError('field 不能为空')
        self.kwargs = kwargs

    def __repr__(self):
        print(self.__module__)

    @property
    def item(self):
        return self.kwargs


class MyItem(ProxyItem):
    field = {
        'ip',                       # ip
        'port',                     # 端口
        'type',                     # 类型
        'adr',                      # 地址
        'olien_speed',              # 网上爬取速度
        'olien_last_valid_time',    # 最后验证时间
        'my_test_speend',           # 自己测试的ip延迟
        'my_test_time',             # 测试的时间
    }
