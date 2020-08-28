# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2018/6/22 16:55'
import os, sys
sys.path.append(os.pardir)
import configparser


class HandleIni(object):
    def get_ini_value(self, node, key, file_path=None):
        if file_path == None:
            self.file_path = os.path.abspath('..') + '/config/server.ini'
        else:
            self.file_path = file_path
        ini_file_path = self.file_path
        cf = configparser.ConfigParser()
        cf.read(ini_file_path, encoding='utf-8-sig')
        data = cf.get(node, key)
        return data
