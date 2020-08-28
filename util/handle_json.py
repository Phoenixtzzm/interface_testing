# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/20 18:49'
import os, sys
sys.path.append(os.pardir)
import json


class HandleJson(object):
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = os.path.abspath('..') + '/config/userdata.json'
        else:
            self.file_path = file_path

    def read_json(self,file_path=None):
        if file_path == None:
            with open(self.file_path,encoding='utf-8') as f:
                data = json.load(f)
        else:
            with open(file_path,encoding='utf-8') as f:
                data = json.load(f)
        return data

    def get_data(self, key,file_path=None):
        if file_path == None:
            data = self.read_json()
        else:
            data = self.read_json(file_path)
        # res_data = data[key]
        res_data = data.get(key)
        return res_data

    def write_value(self,data):
        data_value = json.dumps(data)
        with open(self.file_path,"w") as f:
            f.write(data_value)

if __name__ == '__main__':
    pass