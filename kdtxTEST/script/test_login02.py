from api.login import loginAPI


class Test_login:
    uuid = None

    # 前置处理
    def setup(self):
        self.login_api = loginAPI()
        # 获取验证码
        response = self.login_api.get_code()
        Test_login.uuid = response.json().get('uuid')

    # 后置处理
    def teardown(self):
        pass

    # 登录成功
    def test_001_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": Test_login.uuid
        }
        res_1 = self.login_api.login(test_data=login_data)
        print(res_1.json())

    # 登录失败，账户为空
    def test_002_fail(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": Test_login.uuid
        }
        res_2 = self.login_api.login(test_data=login_data)
        print(res_2.json())
    # 登录失败，账号未注册
    def test_003_fail(self):
        login_data = {
            "username": "admin1323",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": Test_login.uuid
        }
        res_3 = self.login_api.login(test_data=login_data)
        print(res_3.json())