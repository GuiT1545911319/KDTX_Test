# 接口封装，依据接口文档封装接口信息
import requests


# 创建接口类
class loginAPI:
    # 初始化
    def __init__(self):
        # url基本信息
        self.url_verify = "https://kdtx-test.itheima.net/api/captchaImage"
        self.url_login = "https://kdtx-test.itheima.net/api/login"

    # 验证码
    def get_code(self):
        return requests.get(url=self.url_verify)

    # 登录
    def login(self, test_data):
        return requests.post(url=self.url_login, json=test_data)
