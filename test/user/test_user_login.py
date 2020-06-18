import json  # 用来转化excel中的json字符串为字典
import unittest
import requests
import os  #增加一个os，需要用来组装路径
import sys
sys.path.append("../..")  #升级两级大项目根目录下
from api_test_framework.config.config import *
from api_test_framework.lib.case_log import log_case_info
from api_test_framework.lib.read_excel import *  # 导入read_excel中的方法

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  #整个测试类只执行一次
        cls.data_list = excel_to_list("D:/work/python/api_test_framework/data/test_user_data.xlsx", "TestUserLogin")  # 读取该测试类所有用例数
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_login_normal')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)
        self.assertEqual(res.text, expect_res)  # 改为assertEqual断言


if __name__ == '__main__':  # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)