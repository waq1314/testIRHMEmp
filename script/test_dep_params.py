# 导包
import unittest, logging
from parameterized import parameterized
from api.dep_api import DepApi
from api.login_api import LoginApi
import app
from utils import assert_common, read_dep_data, read_dep_login_data


# 创建测试类
class TestIHRMDepParams(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化部门
        self.dep_api = DepApi()
    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type":"application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

        # 定义部门模块的文件路径
    dep_fp= app.BASE_DIR + "/data/dep_login.json"
    # 定义查看组织架构列表的函数
    @parameterized.expand(read_dep_login_data(dep_fp, 'dep_login'))
    def test02_dep_login(self,success,code,message,http_code ):
        response=self.dep_api.dep(app.HEADERS)
        # 打印查看组织架构列表的结果
        logging.info("查看组织架构列表的结果为:{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    # 定义部门模块的文件路径
    dep_filepath = app.BASE_DIR + "/data/dep_data.json"
    @parameterized.expand(read_dep_data( dep_filepath,'add_dep'))
    def test03_add_dep(self,name,code1,success,code,message,http_code):
        # 发送添加部门的接口请求
        response = self.dep_api.add_dep(name, code1,app.HEADERS)
        # 打印添加部门的结果
        logging.info("添加部门的结果为：{}".format(response.json()))
        # 提取部门中的令牌并把部门令牌保存到全局变量中
        app.DEP_ID = response.json().get('data').get('id')
        # 打印保存的部门ID
        logging.info("保存到全局变量的部门的ID为：{}".format(app.DEP_ID))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, 'query_dep'))
    def test04_query_dep(self,success,code,message,http_code):
        # 发送查询部门的接口请求:
        response = self.dep_api.query_dep(app.DEP_ID, app.HEADERS)
        # 打印查询部门的数据
        logging.info("查询部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, 'modify_dep'))
    def test05_modify_dep(self,name,success,code,message,http_code):
        # 发送修改部门的接口请求:
        response = self.dep_api.modify_dep(app.DEP_ID, {"name":name},app.HEADERS)
        # 打印修改部门的数据
        logging.info("修改部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dep_data(dep_filepath, 'delete_dep'))
    def test06_delete_dep(self,success,code,message,http_code):
        # 发送删除部门的接口请求:
        response = self.dep_api.delete_dep(app.DEP_ID,app.HEADERS)
        # 打印删除部门的数据
        logging.info("删除部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)