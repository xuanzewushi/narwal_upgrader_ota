#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: conf.py
@time: 2023/3/3 下午4:35
"""


class OprateIni(object):
    def __init__(self, path, name, data=''):
        self._path = './upgrader_ota_file/' + path + '/config/' + name
        self._data = data

    def read_ini_data(self):
        with open(self._path, 'r', encoding='utf-8') as r:
            return r.read()

    def write_ini_data(self):
        with open(self._path, 'w', encoding='utf-8') as w:
            w.write(self._data)
            return '写入成功!'

