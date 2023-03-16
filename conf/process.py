#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: process.py
@time: 2023/3/15 下午3:16
"""

from multiprocessing import Process, pool
import os


# def test(name):
#     print(name + str(os.getpid()))


# def run_process(name):
#     p = Process(target=name)
#     p.start()
#     p.join()
upgrade_stress_test_one = "gnome-terminal -e 'bash -c \"echo asdf1234 |sudo -S ../upgrade_ota_file/upgrade_stress_test_one/upgrade_stress_test; exec bash\"'"

path = "gnome-terminal -e 'bash -c \"echo asdf1234 |sudo -S ../upgrade_ota_file/upgrade_stress_test_one/upgrade_stress_test; exec bash\"'"
# 执行脚本
os.system(upgrade_stress_test_one)

# if __name__ == '__main__':
#     print(os.getpid())
#     run_process()
