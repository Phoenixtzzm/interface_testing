# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/25 19:40'

import os, sys, random, re,time

sys.path.append(os.pardir)
import os, ddt, json, unittest, datetime
from util.handle_excel import HandleExcel
from base.base_request import BaseRequest
from util.handle_result import HandleResult
from util.handle_cookie import HandleCookie
from util.handle_header import HandleHeader
from util.handle_condition import HandleCondition
from util.handle_ini import HandleIni
from util.handle_email import send_email
from run.run_main import RunMain
from BeautifulReport import BeautifulReport
from requests_toolbelt import MultipartEncoder
import pymssql
from apscheduler.schedulers.blocking import BlockingScheduler

# 实例化excel操作类，调用获取表格数据方法，拿到表格sheet1所有数据
case_data = HandleExcel().get_excel_data()


# 调用数据驱动库
@ddt.ddt
class RunCaseDdt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化表格、配置文件、json文件处理类，调用对应方法
        cls.handle_excel = HandleExcel()
        cls.rows = cls.handle_excel.get_rows()
        cls.base_request = BaseRequest()
        cls.handle_result = HandleResult()
        cls.handle_cookie = HandleCookie()
        cls.handle_header = HandleHeader()
        cls.handle_condition = HandleCondition()
        cls.handle_ini = HandleIni()
        cls.database_url = cls.handle_ini.get_ini_value(node='server', key='database_url')
        cls.role = cls.handle_ini.get_ini_value(node='server', key='role')
        cls.password = cls.handle_ini.get_ini_value(node='server', key='password')
        cls.database_name = cls.handle_ini.get_ini_value(node='server', key='database_name')

    @classmethod
    def tearDownClass(cls):
        connect = pymssql.connect(cls.database_url,cls.role,cls.password,cls.database_name)
        connect.autocommit(True)
        if connect:
            print('连接成功')
        try:
            sql1 = 'ALTER DATABASE csscloud SET OFFLINE WITH ROLLBACK IMMEDIATE'
            sql2 = "RESTORE DATABASE csscloud FROM DISK = N'D:/Program Files/Microsoft SQL Server/MSSQL11.MSSQLSERVER/MSSQL/Backup/api_test.bak' WITH FILE = 2,RECOVERY,STATS = 5;"
            sql3 = 'ALTER DATABASE csscloud SET online'
            cursor = connect.cursor()
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            connect.autocommit(False)
            cursor.close()
            connect.close()
        except Exception as e:
            raise e
        print('测试结束')

    def setUp(self):
        print('------')

    def tearDown(self):
        print('------')

    # 解包excel数据，传入test_case01中
    @ddt.data(*case_data)
    def test_case01(self, case_data):
        my_cookie = None
        get_cookie = None
        my_header = None
        depend_data = None
        # my_depend_key = None
        formData_dict = None
        files = None
        is_run = case_data[2]
        case_id = case_data[0]
        form_handle = case_data[16]
        url_splicing = case_data[11]
        # 获取case所在行号
        i = self.handle_excel.get_row_number(case_id)
        if is_run == '是':
            is_depend = case_data[3]
            data = case_data[8]
            my_depend_key = case_data[4]
            url = case_data[5]
            random_count = case_data[17]
            auth_url_ = None
            run_count = case_data[19]
            if run_count == None:
                run_count = 0
                run_count = run_count + 1
            else:
                run_count = int(run_count) + 1
            if is_depend:
                # 获取依赖数据
                if data != None:
                    data = json.loads(data)

                # 根据依赖key解析获得依赖数据
                depend_data = self.handle_condition.get_data(data=is_depend)
                if my_depend_key != '<token>' and my_depend_key != '<token><error>' and my_depend_key != '<token><timeout>':
                    # 请求参数处理
                    # 判断‘>>’是否在依赖key中
                    if my_depend_key != None and '>>' in my_depend_key:
                        # 根据指定规则切分字符串,获得一个列表
                        data_key = my_depend_key.split('>>')[0]
                        my_depend_key = my_depend_key.split('>>')[1]
                        # 请求参数字典赋值操作
                        data[data_key][my_depend_key] = depend_data
                        # 序列化data,请求参数需要是json格式的字符串,当前为字典格式
                        data = json.dumps(data)

                    elif my_depend_key != None and '<' in my_depend_key:
                        str_value = my_depend_key.split('<')[0]
                        str_key = my_depend_key.split('<')[1]
                        data_key = my_depend_key.split('<')[2]
                        request_args = my_depend_key.split('<')[3]
                        target_dict = None
                        try:
                            nesting = my_depend_key.split('<')[4]
                            # 遍历depend_data,拿到所有单个字典
                            for item_dict in depend_data:
                                # 拿到值和单个字典值对应的字典
                                if item_dict[str_key] == str_value:
                                    target_dict = item_dict
                            # 获取目标字典对应键的值,赋值给请求参数data
                            data[nesting][request_args] = target_dict[data_key]
                            data = json.dumps(data)
                        except:
                            # 没有嵌套nesting的流程
                            for item_dict in depend_data:
                                if item_dict[str_key] == str_value:
                                    target_dict = item_dict
                            data[request_args] = target_dict[data_key]
                            data = json.dumps(data)

                    elif my_depend_key != None and '%' in my_depend_key:
                        data_key = my_depend_key.split('%')[0]
                        my_depend_key1 = my_depend_key.split('%')[1]
                        my_depend_key2 = my_depend_key.split('%')[2]
                        data[data_key][my_depend_key1] = depend_data
                        data[my_depend_key2] = depend_data + '.select'
                        data = json.dumps(data)

                    elif my_depend_key != None and '?' in my_depend_key:
                        # 获取文件路径
                        file_path = case_data[21]
                        # 获取文件流
                        files = {'files': ('321.xlsx', open(file_path, 'rb'), 'application/vnd.ms-excel')}
                        my_depend_key_2 = my_depend_key.split('?')[1]
                        auth_url_ = '?' + my_depend_key_2 + '=' + depend_data
                        if data:
                            data = json.dumps(data)

                    elif my_depend_key != None and 'p↑' in my_depend_key:

                        files = {'files': ('123.png', open('C:\\Users\\pcsales\\Desktop\\123.png', 'rb'), 'image/png')}
                        data_key = my_depend_key.split('↑')[1]
                        data_key_value = my_depend_key.split('↑')[2]
                        my_depend_key_1 = my_depend_key.split('↑')[3]
                        target_dict = None
                        for pic_i in depend_data:
                            if pic_i[data_key] == data_key_value:
                                target_dict = pic_i
                        data[my_depend_key_1] = target_dict['id']
                        data = json.dumps(data)

                    elif my_depend_key != None and 'f↑' in my_depend_key:
                        files = {'files': (
                        '321.xlsx', open('C:\\Users\\pcsales\\Desktop\\321.xlsx', 'rb'), 'application/vnd.ms-excel')}
                        data_key = my_depend_key.split('↑')[1]
                        data_key_value = my_depend_key.split('↑')[2]
                        my_depend_key_1 = my_depend_key.split('↑')[3]
                        target_dict = None
                        for pic_i in depend_data:
                            if pic_i[data_key] == data_key_value:
                                target_dict = pic_i
                        data[my_depend_key_1] = target_dict['id']
                        data = json.dumps(data)
                    elif my_depend_key !=None and 'Approval' in my_depend_key:
                        currentLinkId = depend_data['currentLinkId']
                        taskApplyId = depend_data['taskApplyId']
                        nextLinkName = depend_data['agree']['approvalLinkName']
                        nextLinkId = depend_data['agree']['approvalLinkId']
                        data = {

                            'jsonStr': {
                                'variablelist': [],
                                'nextLinkType': '3',
                                'nextLinkId': nextLinkId ,
                                'nextLinkName': nextLinkName,
                                'mainTaskLinkId': '',
                                'result': '同意',
                                'taskApplyId': taskApplyId,
                                'currentLinkId': currentLinkId
                            }
                        }
                        data =  json.dumps(data)
                        print(data)
                    else:
                        data[my_depend_key] = depend_data
                        data = json.dumps(data)

            # 项目编号唯一处理,每次随机生成一个编号
            if random_count:
                main_key = random_count.split('>')[0]
                secondary_key = random_count.split('>')[1]
                data = json.loads(data)
                random_str = str(random.randrange(100000000, 999999999))
                data[main_key][secondary_key] = random_str
                self.handle_excel.excel_write_data(i, 21, random_str)
                data = json.dumps(data)

            auth_url = url
            method = case_data[7]
            is_cookie = case_data[9]
            is_header = case_data[10]
            expect_method = case_data[12]
            expect_code = case_data[13]
            # 请求url带上token
            if url_splicing:
                if url_splicing == 'read':
                    url_path = self.handle_excel.get_cell_value(row=3, col=7)
                    auth_url = url + url_path
                if url_splicing != 'read' and url_splicing != 'write':
                    auth_row = url_splicing.split('>')[1]
                    url_path = self.handle_excel.get_cell_value(row=int(auth_row), col=7)
                    auth_url = url + url_path
            if my_depend_key != None and '?' in my_depend_key:
                auth_url = auth_url + auth_url_
            if is_cookie == 'yes':
                my_cookie = self.handle_cookie.get_cookie_value('web')
            if is_cookie == 'write':
                get_cookie = {'is_cookie': 'web'}
            # 根据不同字符串,获取指定header内容
            if is_header == 'yes':
                my_header = self.handle_header.get_header('true')
            if is_header == 'yes>upload':
                my_header = self.handle_header.get_header('false')
                if my_depend_key == '<token>':
                    header_auth = depend_data
                    my_header = self.handle_header.get_token_header(data=header_auth)
                elif my_depend_key == '<token><error>':
                    header_auth = 'qwerty'
                    my_header = self.handle_header.get_token_header(data=header_auth)
                elif my_depend_key == '<token><timeout>':
                    header_auth = 'MTc3RDE0NEY1QTlDN0EwM0IwM0M4NDA0OTNFRjhDQTEzNTQzMTM4RDk0RDg5Q0QzNTMyNDg4OUEwNjE1OTFBRjA4NzMzM0MwMjg3NUQ5NEE5QUU4Q0Q3MzJBRUMyRkZFNTNFNEEzNzYxRDE1OTNFNThDMEEwOEFGREE0MDE0NTE='
                    my_header = self.handle_header.get_token_header(data=header_auth)
                # my_header = json.dumps(my_header_dict)

            # 请求参数格式处理,转为FormData数据格式
            if form_handle == 'yes':
                if data != None:
                    data_dict = json.loads(data)
                    formData_dict = {}
                    dict_items = data_dict.items()
                    for key, value in dict_items:
                        va = json.dumps(value)
                        formData_dict[key] = va.strip('"')
                else:
                    formData_dict = data
            # 获取请求返回的结果,用于断言和响应结果写入
            res = self.base_request.run_request(method=method, url=auth_url, data=formData_dict, cookie=my_cookie,
                                                get_cookie=get_cookie, header=my_header, files=files)
            print(res)
            # 写入url要拼接的token部分
            if url_splicing == 'write':
                token = res['token']
                userId = res['data']['loginUserModel']['userId']
                auth_id = '/' + token + '/' + userId
                self.handle_excel.excel_write_data(row=i, col=7, value=auth_id)
            # res.get(),拿到则返回对应值，找不到返回None
            code = res.get('msgCode')
            msg = res.get('message')
            message = res.get('message')
            # 根据'响应码-2'和响应消息是否一致,进行断言
            if expect_method == 'msg_code':
                # 判断'响应码-1'是否为1,是则继续流程,否则写入测试结果与响应结果,抛出异常
                try:
                    self.assertEqual(str(code), expect_code)
                    msg_json = self.handle_result.get_msg(key_url=url, code=str(code))
                    try:
                        self.assertEqual(msg, msg_json)
                        # if msg == msg_json:
                        self.handle_excel.excel_write_data(i, 15, 'pass')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                    except Exception as e:
                        self.handle_excel.excel_write_data(i, 15, 'fail')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                        raise e
                except Exception as e:
                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e

            elif expect_method == 'code':
                # if code == expect_code:
                try:
                    self.assertEqual(str(code), expect_code)
                    self.handle_excel.excel_write_data(i, 15, 'pass')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                except Exception as e:
                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e
            # 根据响应结果的数据格式,判断接口是否正常
            elif expect_method == 'result_json':
                # if code == 1000:
                if msg == '操作成功！':
                    key = 'true'
                else:
                    key = 'false'
                expect_json = self.handle_result.get_result_json(key_url=url, key=key)
                result = self.handle_result.handle_result_json(res, expect_json)
                try:
                    self.assertTrue(result)
                    self.handle_excel.excel_write_data(i, 15, 'pass')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                except Exception as e:
                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e

            elif expect_method == 'message':
                try:
                    self.assertEqual(str(code), expect_code)
                    expect_message = self.handle_result.get_result_json(key_url=url, key=message,
                                                                        file_path='C:/Users/pcsales/Desktop/ApiAuto/config/message.json')
                    if expect_message:
                        result = True
                    else:
                        result = False
                    try:
                        self.assertTrue(result)
                        self.handle_excel.excel_write_data(i, 15, 'pass')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                    except Exception as e:

                        self.handle_excel.excel_write_data(i, 15, 'fail')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                        raise e
                except Exception as e:

                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e

            # 执行sql语句,返回查询结果和接口响应结果进行对比,不一致则抛出异常
            elif expect_method == 'query':
                query_db = case_data[18]
                try:
                    self.assertEqual(str(code), expect_code)
                    connect = pymssql.connect(self.database_url, self.role, self.password, self.database_name)
                    if connect:
                        print("连接成功!")
                    try:
                        time.sleep(3)
                        cursor = connect.cursor()
                        cursor.execute(query_db)
                        query_result = cursor.fetchone()
                        if query_result:
                            result = True
                        else:
                            result = False
                        try:
                            self.assertTrue(result)
                            self.handle_excel.excel_write_data(i, 15, 'pass')
                            self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                            self.handle_excel.excel_write_data(i, 20, run_count)
                        except Exception as e:
                            self.handle_excel.excel_write_data(i, 15, 'fail')
                            self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                            self.handle_excel.excel_write_data(i, 20, run_count)
                            raise e
                        cursor.close()
                        connect.close()
                    except Exception as e:
                        self.handle_excel.excel_write_data(i, 20, run_count)
                        raise e
                except Exception as e:
                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e

            # 正则匹配,匹配目标内容是否在响应内容中,不在则抛出异常
            elif expect_method == 're':
                try:
                    self.assertEqual(str(code), expect_code)
                    try:
                        re_str = case_data[18]
                        target_str = '\'' + json.dumps(res, ensure_ascii=False) + '\''
                        re_result = re.findall(re_str, target_str)
                        if re_result:
                            result = True
                        else:
                            result = False
                        self.assertTrue(result)
                        self.handle_excel.excel_write_data(i, 15, 'pass')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                    except Exception as e:
                        self.handle_excel.excel_write_data(i, 15, 'fail')
                        self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        self.handle_excel.excel_write_data(i, 20, run_count)
                        raise e
                except Exception as e:
                    self.handle_excel.excel_write_data(i, 15, 'fail')
                    self.handle_excel.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    self.handle_excel.excel_write_data(i, 20, run_count)
                    raise e


if __name__ == '__main__':
    # unittest.main()
    # 获取当前文件的（上级）工作目录
    case_path = os.getcwd()
    # 将所有‘run_case开头的py文件加入测试套件中’
    suite = unittest.defaultTestLoader.discover(case_path, 'run_case*.py')
    # 实例化BeautifulReport类，执行测试
    test_suite = BeautifulReport(suite)
    # 测试报告文件生成地址
    test_suite.report(filename='api_test', description='星辰-默认分组接口测试报告',
                      report_dir='C:/Users/pcsales/Desktop/ApiAuto/report',
                      theme='theme_cyan')

    # 发送邮件方法，测试结束将测试报告以附件的形式发到指定邮箱
    send_email()
