# 导入包
import config
from api.login import loginAPI
from api.upload import upload_contractAPI


# 创建测试类
class TestContract_busniess:
    token = None

    # 前置处理 实例化接口对象
    def setup(self):
        self.login_api = loginAPI()
        self.upload_api = upload_contractAPI()

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
        print(res_l.status_code)
        print(res_l.json())
        TestContract_busniess.token = res_l.json().get('token')

    # 上传合同成功
    def test_upload_contract(self):
        f = open(config.base_path+'/data/test.pdf', 'rb')
        res_u = self.upload_api.upload(test_data=f, token=TestContract_busniess.token)
        print(res_u.json())
