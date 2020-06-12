# 导包
import requests
# 封装系统登录接口类
class LoginApi:
    def __init__(self):
        self.login_url="http://ihrm-test.itheima.net"+"/api/sys/login"
    def login(self,jsonData,headers):
        """
        :rtype:Response
        :param jsonData:
        :param headers:
        :return:
        """
        return requests.post(url=self.login_url,json=jsonData,headers=headers)
