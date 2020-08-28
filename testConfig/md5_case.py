# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/19 15:27'

import hashlib
import requests
import json
target_str = '12345'
md5 = hashlib.md5()
md5.update(target_str.encode('utf-8'))
md5_str= md5.hexdigest()
print(md5_str)

data = {
        "username": "",
        "password": ""}


res = requests.post(url='http://127.0.0.1:8801/login',json=data)
print(type(res))
res.encoding = 'utf-8'
a=res.text
print(a)