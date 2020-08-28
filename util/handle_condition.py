# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/24 16:35'
import os, sys
sys.path.append(os.pardir)
import json
from util.handle_excel import HandleExcel
from jsonpath_rw import parse

class HandleCondition(object):
    def __init__(self):
        self.handle_excel = HandleExcel()

    def split_data(self,data):
        case_id = data.split('>')[0]
        rule_data = data.split('>')[1]
        return case_id,rule_data

    def depend_data(self,depend_key):
        # 获取依赖数据集
        # case_id = self.split_data(depend_key)[0]
        row_num = self.handle_excel.get_row_number(depend_key)
        depend_data = self.handle_excel.get_cell_value(row=row_num,col=16)
        return json.loads(depend_data)

    # data.banner.id
    def get_depend_data(self,depend_data,parse_key):
        # 按解析规则生成解析器
        json_exe = parse(parse_key)
        target_data = json_exe.find(depend_data)
        # 更高效的写法
        return [math.value for math in target_data][0]
        # print(madle)
        # for math in madle:
        #     return math.value

    def get_data(self,data):
        # 获取依赖数据
        split_data_list = self.split_data(data)
        key = split_data_list[0]
        rule_data = split_data_list[1]
        res_data = self.depend_data(key)
        dep_data = self.get_depend_data(depend_data=res_data,parse_key=rule_data)
        return dep_data


if __name__ == '__main__':
    a= HandleCondition()
    data = a.depend_data('test01')

    print(a.get_depend_data(depend_data=data,parse_key='data'))