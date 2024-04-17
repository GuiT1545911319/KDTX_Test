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

    def test_select_success(self):
        res_s = self.course_api.select_course(test_data="?name=数据库原理", token=TestcourseAPI.token)
        assert 200 == res_s.status_code
        assert '数据库原理' in res_s.text
        assert 200 == res_s.json().get('code')

    def test_select_fail(self):
        res_sf = self.course_api.select_course(test_data="?name=数据库原理", token="xxxxxxxx")
        assert 200 == res_sf.status_code
        assert '失败' in res_sf.text
        assert 401 == res_sf.json().get('code')

