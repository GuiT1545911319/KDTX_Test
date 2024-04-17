
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

    def test_change_success(self):
        change_data = {
            "id": 5991,
            "name": "数据库原理及其应用",
            "subject": "9",
            "price": 999,
            "applicablePerson": "5",
            "info": "专业相关课程"
        }
        res_c = self.course_api.change_course(test_data=change_data, token=TestcourseAPI.token)
        print(res_c.json())
        assert 200 == res_c.status_code
        assert '成功' in res_c.text
        assert 200 == res_c.json().get('code')

    def test_change_fail(self):
        change_data = {
            "id": 5991,
            "name": "数据库原理及其应用",
            "subject": "9",
            "price": 999,
            "applicablePerson": "5",
            "info": "专业相关课程"
        }
        res_cf = self.course_api.select_course(test_data=change_data, token="xxxxxxxx")
        assert 200 == res_cf.status_code
        assert '失败' in res_cf.text
        assert 401 == res_cf.json().get('code')

