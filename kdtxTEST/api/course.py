import requests

import config


class courseAPI:

    def __init__(self):
        self.url_course = config.base_url+"/api/clues/course"
        self.url_select = config.base_url+"/api/clues/course/list"

    def add_coures(self, test_data, token):
        return requests.post(url=self.url_course, json=test_data, headers={"Authorization": token})

    def select_course(self, token, test_data):
        return requests.get(url=self.url_select+f"/{test_data}", headers={"Authorization": token})

    def change_course(self, test_data, token):
        return requests.put(url=self.url_course, json=test_data, headers={"Authorization": token})

    def delete_course(self, test_data, token):
        return requests.delete(url=self.url_course+f"/{test_data}", headers={"Authorization": token})