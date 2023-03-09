#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: conf.py
@time: 2023/3/3 下午4:35
"""

import os


def get_robot_times():
    robot_file_times = os.listdir('./upgrader_ota_file/')
    return str(len(robot_file_times))


def get_robots():
    robot_file_times = os.listdir('./upgrader_ota_file/')
    robots = ''
    for i in robot_file_times:
        robots = robots + i + ', '
    return robots


def get_robot():
    robot_file_times = os.listdir('./upgrader_ota_file/')
    robots = ''
    for i in robot_file_times:
        robots = robots + i + ', '
    return robots


#
# if __name__ == '__main__':
#     get_robots()
