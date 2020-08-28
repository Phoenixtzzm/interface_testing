# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/23 21:21'

import os, sys
sys.path.append(os.pardir)
import hashlib,json
from util.handle_json import HandleJson

class HandleHeader(object):
    def __init__(self):
        file_path = os.path.abspath('..') + '/config/header.json'
        self.handle_json = HandleJson(file_path=file_path)

    # 无token的header
    def get_header(self,type):
        header_data = self.handle_json.read_json()
        header_data = header_data['header'][0][type]
        return header_data

    #md5加密的header
    def header_md5(self,type):
        data = self.get_header(type)
        target = data['token']
        md5 = hashlib.md5()
        md5_str = md5.update(target.encoding('utf-8'))
        data['token'] = md5_str
        return data

    # 带token的header
    def get_token_header(self,data):
        header_data = self.handle_json.read_json()
        header_data['AuthToken'] = data
        return header_data
