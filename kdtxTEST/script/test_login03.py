import pytest
from api.login import loginAPI

# 测试数据
test_data = [
    ("admin", "HM_2023_test", 200, "成功", 200),
    ("", "HM_2023_test", 200, "错误", 500),
    ("admin123", "HM_2023_test", 200, "错误", 500)
]


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
    @pytest.mark.parametrize("username, password, status, message, code", test_data)
    def test_001_success(self, username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": Test_login.uuid
        }
        res_1 = self.login_api.login(test_data=login_data)
        assert status == res_1.status_code
        assert message in res_1.text
        assert code == res_1.json().get('code')

