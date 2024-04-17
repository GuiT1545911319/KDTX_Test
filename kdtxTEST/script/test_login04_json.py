
import pytest

import config
from api.login import loginAPI
import json


# 读数据
def build_data(json_file):
    test_data = []
    with open(config.base_path+"/data/data.json", 'r', encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get('message')
            code = case_data.get('code')
            test_data.append((username, password, status, message, code))
    return test_data


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
    @pytest.mark.parametrize("username, password, status, message, code", build_data(json_file="../data/data.json"))
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

