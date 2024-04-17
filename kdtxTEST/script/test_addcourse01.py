from api.login import loginAPI
from api.course import courseAPI


class TestAddcourse:

    token = None
    # 前置处理
    def setup(self):
        # 接口实例化
        self.login_api=loginAPI()
        self.add_course_api=courseAPI()
        # 获取验证码
        response1 = self.login_api.get_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": response1.json().get('uuid')
        }
        # 登录成功
        response2 = self.login_api.login(test_data=login_data)
        TestAddcourse.token = response2.json().get('token')

    # 后置处理
    def teardown(self):
        pass

    # 增加课程成功
    def test_add_course_success(self):
        course_data = {
            "name": "数据库原理",
            "subject": '7',
            "price": 900,
            "applicablePerson": "6",
            "info": "数据库原理"
        }
        # 登录成功
        response3 = self.add_course_api.add_coures(test_data=course_data,token = TestAddcourse.token)
        assert 200 == response3.status_code
        assert '成功' in response3.text
        assert 200 == response3.json().get('code')

    # 增加课程失败（用户未登录）
    def test_add_course_fail(self):
        course_data = {
            "name": "数据库原理",
            "subject": '7',
            "price": 900,
            "applicablePerson": "6",
            "info": "数据库原理"
        }
        # 登录成功
        response4 = self.add_course_api.add_coures(test_data=course_data, token='XXXXXXXXXX')
        assert 200 == response4.status_code
        assert '认证失败' in response4.text
        assert 401 == response4.json().get('code')