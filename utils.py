# 导包
import json
import logging
from app import BASE_DIR
from  logging import handlers
def init_logging():
    # 定义日志器
    logger=logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置控制台处理器
    str=logging.StreamHandler()
    # 设置文件处理器
    log_path=BASE_DIR+"/log/ihrm.log"
    fh=logging.handlers.TimedRotatingFileHandler(filename=log_path,when="M",interval=1,backupCount=3,encoding="utf-8")
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter=logging.Formatter(fmt)
    # 给控制台和文件处理器添加格式化器
    str.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 给日志器添加控制台和文件处理器
    logger.addHandler(str)
    logger.addHandler(fh)
def assert_common(self,http_code,success,code,message,response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))
# 编写读取登录数据的函数
def read_login_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData: #type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    print("查看读取的登录数据为：", result_list)
    return result_list
# 编写读取部门增删改查数据的函数
def read_dep_data(filepath,interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        dep_data = jsonData.get(interface_name)  # type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(dep_data.values()))
        # 返回数据
    print("读取的{}部门数据为:{}".format(interface_name, result_list))
    return result_list
# 编写读取组织架构列表的函数
def read_dep_login_data(filepath,interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        dep_login_data = jsonData.get(interface_name)  # type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(dep_login_data.values()))
        # 返回数据
    print("读取的{}部门数据为:{}".format(interface_name, result_list))
    return result_list

