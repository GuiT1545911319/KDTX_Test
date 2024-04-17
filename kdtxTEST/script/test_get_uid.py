import requests

response = requests.get(url="https://kdtx-test.itheima.net/api/captchaImage")
print(response.status_code)
dict = response.json()
print(dict['uuid'])