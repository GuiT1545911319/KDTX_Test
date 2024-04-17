from api.login import loginAPI
from api.course import courseAPI
import pytest


class TestcourseAPI:
    token = None

    # 前置步骤
    def setup(self):
        # 接口实例化
        self.login_api = loginAPI()
        self.course_api = courseAPI()
        # 获取验证码
        res_v = self.login_api.get_code()
        # 登录成功
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get('uuid')
        }
        # 登录成功
        res_l = self.login_api.login(test_data=login_data)
        TestcourseAPI.token = res_l.json().get('token')

    def teardown(self):
        pass

    def test_delete_success(self):
        res_s = self.course_api.delete_course(test_data=6232, token=TestcourseAPI.token)
        print(res_s.json())
        assert 200 == res_s.status_code
        assert '成功' in res_s.text
        assert 200 == res_s.json().get('code')

    def test_delete_fail01(self):
        res_sf = self.course_api.delete_course(test_data=6122232, token=TestcourseAPI.token)
        print(res_sf.json())
        assert 200 == res_sf.status_code
        assert '失败' in res_sf.text
        assert 500 == res_sf.json().get('code')

    def test_delete_fail02(self):
        res_sf = self.course_api.select_course(test_data=6232, token='xxxxxxxxx')
        assert 200 == res_sf.status_code
        assert '失败' in res_sf.text
        assert 401 == res_sf.json().get('code')