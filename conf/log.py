#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: log.py
@time: 2023/5/20 下午6:08
"""
import os
from datetime import datetime


def logger(data):
    _logfile = './log/test.logging'
    with open(_logfile, 'w', encoding='utf-8') as w:
        w.write(str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + ' ' + data)

    if os.path.getsize(_logfile) > 1000:
        filename = './log/ota_upgrade_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.txt'
        os.rename(_logfile, filename)


