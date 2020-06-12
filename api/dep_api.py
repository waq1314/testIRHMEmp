import requests
# 创建封装部门模块接口的类
class DepApi:
    def __init__(self):
        self.dep_url="http://ihrm-test.itheima.net"+"/api/company/department"
    # 查看组织架构列表
    def dep(self,headers):
        return requests.get(url=self.dep_url,headers=headers)
    # 添加部门
    def add_dep(self,name,code1,headers):
        jsonData = {
            "name": name,
            "code": code1,
            "manager": "苹果",
            "introduce": "日常解决员工的小要求",
            "pid": ""
        }
        return requests.post(url=self.dep_url,json=jsonData,headers=headers)
    # 查询部门
    def query_dep(self,dep_id,headers):
        query_url=self.dep_url+"/"+dep_id
        return requests.get(url=query_url,headers=headers)
    # 修改部门
    def modify_dep(self,dep_id,jsonData,headers):
        modify_url=self.dep_url+"/"+dep_id
        return requests.put(url=modify_url,json=jsonData,headers=headers)
    # 删除部门
    def delete_dep(self,dep_id,headers):
        delete_url=self.dep_url+"/"+dep_id
        return requests.delete(url=delete_url,headers=headers)



