# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/22 18:12'
import os, sys,json
sys.path.append(os.pardir)
from util.handle_json import HandleJson
from deepdiff import DeepDiff


class HandleResult(object):
    def __init__(self):
        self.handle_json = HandleJson()

    def get_msg(self, key_url, code, file_path=None):
        if file_path == None:
            self.file_path = os.path.abspath('..') + '/config/code_message.json'
        else:
            self.file_path = file_path
        data = self.handle_json.get_data(file_path=self.file_path, key=key_url)
        if data != None:
            for i in data:
                msg = i.get(code)
                if msg != None:
                    return msg
        return None

    def get_result_json(self, key_url, key, file_path=None):
        if file_path == None:
            self.file_path = os.path.abspath('..') + '/config/expect_result.json'
        else:
            self.file_path = file_path
        data = self.handle_json.get_data(file_path=self.file_path, key=key_url)
        if data != None:
            for i in data:
                json_data = i.get(key)
                if json_data != None:
                    return json_data
        return None

    # 校验格式,只比较key
    def handle_result_json(self, dict1, dict2):

        if isinstance(dict1,dict) and isinstance(dict2,dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            if cmp_dict.get('dictionary_item_removed') or cmp_dict.get('dictionary_item_added') or cmp_dict.get(
                    'type_changes'):
                return False
            else:
                return True
        return False



