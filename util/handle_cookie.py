# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/23 17:51'
import os, sys
sys.path.append(os.pardir)
from util.handle_json import HandleJson

class HandleCookie(object):

    def __init__(self):
        file_path = os.path.abspath('..') + '/config/cookie.json'
        self.handle_json = HandleJson(file_path=file_path)

    def get_cookie_value(self,cookie_key):
        data = self.handle_json.read_json()
        cookie_data = data[cookie_key]
        return cookie_data

    def write_cookie(self,cookie_key,cookie_data):
        data = self.handle_json.read_json()
        data[cookie_key] = cookie_data
        self.handle_json.write_value(data)

