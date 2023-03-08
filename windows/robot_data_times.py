#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: robot_data_times.py
@time: 2023/3/6 上午10:03
"""

import os


def get_robot_times():
    robot_file_times = os.listdir('./upgrader_ota_file/')
    return str(len(robot_file_times))


# if __name__ == '__main__':
#     get_robot_times()

