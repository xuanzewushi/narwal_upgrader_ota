#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: main_window.py.py
@time: 2023/3/3 下午12:08
"""


import sys
import time

import yaml
from PyQt6.QtWidgets import *

"""
1.新增压测机器人数量
2.可以查看不同压测机器人的数据
3.可以选择不同机器人配置进行执行脚本
    3.1 单独子弹窗，每执行1个压测的机器人脚本就启动1个子弹窗
    3.2 已启动的机器人脚本不可继续启动，需等原来的脚本停掉
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 设置最大化窗口
        # self.showMaximized()
        self.setGeometry(800, 800, 800, 800)  # 窗口位置x，y，窗口尺寸x，y

        # 居中显示
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # 窗口title
        self.setWindowTitle('upgrade_ota升级脚本界面')

        # 引用grid布局
        self.grid = QGridLayout()

        # 说明文案区
        self.configuration_one = QLabel('一、当前可执行机器人\n'
                                        '二、文案')
        # -----------------分割符-----------------
        # 区域分割符
        self.label1 = QLabel('— — ' * 30)

        # 刷新按钮
        self.renovate = QPushButton('刷新')

        # 文案
        self.robot_times = QLabel('当前可执行机器人：')
        self.run_robot_times = QLabel('当前正在执行的机器人数量：')

        # 运行脚本按钮
        self.run_button = QPushButton('运行脚本')

        # 输入框
        # self.robot_times_edit = QLineEdit()

        # -----------------分割符-----------------
        # 区域分割符
        self.label2 = QLabel('— — '*13 + '当前选中第1个机器人' + '— — '*13)

        # 文案
        self.robot_data = QLabel('所拥有的机器人：')
        self.stress_test_config = QLabel('stress_test_config.ini文件：')
        self.robot_adb_config = QLabel('robot_adb_config.ini文件：')

        # 文件文本框
        self.stress_test_config_text = QTextEdit()
        self.robot_adb_config_text = QTextEdit()

        # 按钮
        self.change_file = QPushButton('切换机器人配置')

        # 输入框
        self.change_file_line = QLineEdit()

        self.setLayout(self.grid)
        self.main_win()
        self.show()

    def main_win(self):
        # 说明文案
        self.grid.addWidget(self.configuration_one, 1, 0, 1, 10)  # x, y, n, m。x是第几行，y是第几列，n是占多少行，m是多少列

        # -----------分割符------------
        # 区域分割符
        self.grid.addWidget(self.label1, 2, 0, 1, 9)

        # 文案
        self.grid.addWidget(self.robot_times, 3, 0)
        self.grid.addWidget(self.run_robot_times, 4, 0)

        # 按钮
        self.grid.addWidget(self.run_button, 5, 0)
        self.grid.addWidget(self.renovate, 5, 1)

        # -----------分割符------------
        # 区域分割符
        self.grid.addWidget(self.label2, 6, 0, 1, 9)

        # 所拥有的机器人
        self.grid.addWidget(self.robot_data, 7, 0)

        # 切换机器人配置文件按钮
        self.grid.addWidget(self.change_file, 8, 0)

        # 切换机器人输入框
        self.grid.addWidget(self.change_file_line, 8, 1, 1, 3)
        # 输入框默认文案
        self.change_file_line.setPlaceholderText('ota升级的固件版本')

        # 文件内容说明文案
        self.grid.addWidget(self.stress_test_config, 9, 0, 1, 1)
        self.grid.addWidget(self.robot_adb_config, 9, 4, 1, 1)

        # 文件内容框
        self.grid.addWidget(self.robot_adb_config_text, 9, 5, 5, 3)
        self.grid.addWidget(self.stress_test_config_text, 9, 1, 5, 3)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', "是否关闭程序?")
        if str(reply) == 'StandardButton.Yes':
            event.accept()
        else:
            event.ignore()








