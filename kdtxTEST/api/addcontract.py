import requests

import config


class add_ContractAPI:
    def __init__(self):
        self.addcontract_url = config.base_url+"/api/contract"

    def add_contract(self, test_data, token):
        return requests.post(url=self.addcontract_url, json=test_data, headers={"Authorization": token})
