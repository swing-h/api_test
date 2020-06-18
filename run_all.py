import unittest
from api_test_framework.lib.HTMLTestReportCN import HTMLTestRunner
from api_test_framework.config.config import *
from api_test_framework.lib.send_email_m import send_email

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)   #从配置文件中读取用例路径

with open(report_file, 'wb') as f:  # 改为with open 格式，从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suite)

send_email(report_file)  # 发送邮件
logging.info("================================== 测试结束 ==================================")