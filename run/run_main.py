# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/22 16:36'
import json
from util.handle_excel import HandleExcel
from base.base_request import BaseRequest
from util.handle_result import HandleResult
from util.handle_cookie import HandleCookie
from util.handle_header import HandleHeader
from util.handle_condition import HandleCondition


class RunMain(object):

    def __init__(self):
        self.handle_excle = HandleExcel()
        self.rows = self.handle_excle.get_rows()
        self.base_request = BaseRequest()
        self.handle_result = HandleResult()
        self.handle_cookie = HandleCookie()
        self.handle_header = HandleHeader()
        self.handle_condition = HandleCondition()

    def run_case(self, data):

        for i in range(self.rows - 1):
            my_cookie = None
            get_cookie = None
            my_header = None
            # depend_data = None
            # my_depend_key = None
            is_run = data[2]
            case_id = data[0]
            i = self.handle_excle.get_row_number(case_id)
            if is_run == '是':
                is_depend = data[3]
                data = data[7]
                if is_depend:
                    # 获取依赖数据
                    data = json.loads(data)
                    depend_data = self.handle_condition.get_data(data=is_depend)
                    my_depend_key = data[4]
                    data[my_depend_key] = depend_data
                    data = json.dumps(data)
                url = data[5]
                method = data[6]
                is_cookie = data[8]
                is_header = data[9]
                expect_method = data[10]
                expect_code = data[11]
                if is_cookie == 'yes':
                    my_cookie = self.handle_cookie.get_cookie_value('web')
                if is_cookie == 'write':
                    get_cookie = {'is_cookie': 'web'}
                if is_header == 'yes':
                    my_header = self.handle_header.get_header()
                    # my_header = json.dumps(my_header_dict)
                res = self.base_request.run_request(method=method, url=url, data=data, cookie=my_cookie,
                                                    get_cookie=get_cookie, header=my_header)
                code = res['success']
                msg = res['success']

                if expect_method == 'msg_code':
                    msg_json = self.handle_result.get_msg(key_url=url, code=code)
                    if msg == msg_json:
                        self.handle_excle.excel_write_data(i, 13, 'pass')
                        self.handle_excle.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))

                        print('测试通过')
                    else:
                        self.handle_excle.excel_write_data(i, 13, 'fail')
                        self.handle_excle.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                        print('测试失败')

                elif expect_method == 'code':
                    if code == expect_code:
                        self.handle_excle.excel_write_data(i, 13, 'pass')
                        self.handle_excle.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                        print('测试通过')
                    else:
                        self.handle_excle.excel_write_data(i, 13, 'fail')
                        self.handle_excle.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))

                        print('测试失败')
                elif expect_method == 'result_json':
                    # if code == 1000:
                    if msg == True:
                        key = 'true'
                    else:
                        key = 'false'
                    expect_json = self.handle_result.get_result_json(key_url=url, key=key)

                    result = self.handle_result.handle_result_json(res, expect_json)

                    if result:
                        print('执行通过')
                        self.handle_excle.excel_write_data(i + 2, 13, 'pass')
                        self.handle_excle.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                    else:
                        self.handle_excle.excel_write_data(i + 2, 13, 'fail')
                        self.handle_excle.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                        print('执行失败')
            else:
                print('数据获取失败')


if __name__ == '__main__':
    RunMain()
