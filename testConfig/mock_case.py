# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/19 17:21'

import unittest,mock,openpyxl
from util.handle_json import HandleJson

def homePage(name):
    result = name
    return result


class TestCase(unittest.TestCase):

    def setUp(self):
        self.data = HandleJson().get_data('/register')

    def tearDown(self):
        pass


    def test01(self):
        data = self.data['status']
        homePage = mock.Mock(return_value=data)
        res = homePage()
        self.assertEqual(200,res,'测试失败')


if __name__ == '__main__':
    unittest.main()