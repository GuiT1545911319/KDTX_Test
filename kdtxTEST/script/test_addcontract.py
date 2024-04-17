# 导入包
from api.login import loginAPI
from api.addcontract import add_ContractAPI


# 创建测试类
class Testadd_Contract:
    token = None

    # 前置处理 实例化接口对象
    def setup(self):
        self.login_api = loginAPI()
        self.contract_api = add_ContractAPI()

    # 后置处理
    def teardown(self):
        pass

    # 登录成功
    def test_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_code()
        print(res_v.status_code)
        print(res_v.json())
        # 提取uuid
        uid = res_v.json().get('uuid')
        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uid
        }
        res_l = self.login_api.login(test_data=login_data)
        Testadd_Contract.token = res_l.json().get('token')

    # 上传合同成功
    def test_add_contract(self):
        contract_data ={
            "name": "测试123",
            "phone": "13612344378",
            "contractNo": "HT10012069'",
            "subject": "8",
            "courseId": " 199",
            "channel": "0",
            "activityId": 67, "fileName": "xxx"
        }
        res_a = self.contract_api.add_contract(test_data=contract_data, token=Testadd_Contract.token)
        assert 200 == res_a.status_code
        assert '成功' in res_a.text
        assert 200 == res_a.json().get('code')


