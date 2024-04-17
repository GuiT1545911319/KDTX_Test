import requests


class upload_contractAPI:

    def __init__(self):
        self.upload_url = "https://kdtx-test.itheima.net/api/common/upload"

    def upload(self, test_data, token):
        return requests.post(url=self.upload_url,files={"file": test_data}, headers={"Authorization": token})
