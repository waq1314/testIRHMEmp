# 导包
import time
import unittest
# 实例化测试套件
import HTMLTestRunner_PY3
import app
from script.test_dep_params import TestIHRMDepParams
from script.test_login_params import TestIHRMLoginParams

suite=unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLoginParams))
suite.addTest(unittest.makeSuite(TestIHRMDepParams))
# 定义测试目录和名称
report_path=app.BASE_DIR+"/report/ihrm{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 执行测试用例生成测试报告
with open(report_path,mode="wb")as f:
    # 实例化HTMLTestRunner_PY3
    runner=HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="ihrm系统部门的接口测试",description="我的IHRM部门模块的接口测试报告")
    # 运行测试套件，生成测试报告
    runner.run(suite)