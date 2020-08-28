# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/20 18:35'
import os, sys
sys.path.append(os.pardir)

import json
from util.handle_ini import HandleIni
from util.handle_json import HandleJson
from util.handle_cookie import HandleCookie
import urllib3
import requests,requests.utils
'''
解决Python3 控制台输出InsecureRequestWarning的问题
'''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BaseRequest(object):
    def __init__(self):
        self.handle_cookie = HandleCookie()
    def send_get(self, url,cookie=None,get_cookie=None,header=None,**kwargs):

        res = requests.get(url=url,cookies=cookie,headers=header,verify=False)

        if get_cookie != None:
            cookie_jar = res.cookies
            # 获取的是cookieJar文件对象，需要转化为字典
            cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)

            self.handle_cookie.write_cookie(cookie_key=get_cookie['is_cookie'], cookie_data=cookie_dict)
        try:
            return res.json()
        except:
            return res

    def send_post(self, url, data, cookie=None,get_cookie=None,header=None,files =None,**kwargs):

        res = requests.post(url=url, data=data,cookies=cookie,headers=header,files=files,verify=False)

        if get_cookie != None:
            cookie_jar = res.cookies
            cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)
            print(cookie_dict)
            self.handle_cookie.write_cookie(cookie_key=get_cookie['is_cookie'],cookie_data=cookie_dict)
        try:
            return res.json()
        except:
            return res

    def run_request(self, method, url, data,cookie=None,get_cookie=None,header=None,files=None,**kwargs):
        # mock模拟数据
        # handle_json = HandleJson()
        # a=handle_json.get_data(url)
        # return a
        handle_ini = HandleIni()
        base_url = handle_ini.get_ini_value(node='server', key='host')

        if 'http' not in url:
            url = base_url + url
        if method == 'get':

            return self.send_get(url=url,cookie=cookie,get_cookie=get_cookie,header=header)
        if method == 'post':
            return self.send_post(url=url, data=data,cookie=cookie,get_cookie=get_cookie,header=header,files=files)
        else:
            print('请求方式不支持')
            return None
