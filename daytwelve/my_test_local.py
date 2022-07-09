import requests
import unittest

session = requests.session()

url_local = 'http://localhost:8083/login/authen'
param_data = {'name': 'tiger', 'password': '123456'}
header = {"Content-Type": "application/json"}
r = session.post(url_local, param_data, header)
print(r.text)

url_local_list = 'http://localhost:8083/user/list'
list_r = session.get(url_local_list)
print(list_r.text)
