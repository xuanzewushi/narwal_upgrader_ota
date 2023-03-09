#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: child_window.py
@time: 2023/3/9 下午3:57
"""

import os
import time

from PyQt6.QtWidgets import *


class ChildWindow(QDialog):
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
        self.setWindowTitle('脚本运行界面')
        # 定义grid布局
        self.grid = QGridLayout()

        # log文本框
        self.log_text = QTextEdit()
        self.log_text.setPlainText(self.log_text_now())
        self.log_text.setReadOnly(True)

        #
        self.setLayout(self.grid)
        self.child_win()

    def child_win(self):
        self.grid.addWidget(self.log_text, 1, 1, 1, 5)

    def log_text_now(self):
        # 需要使用多线程运行，否则会卡死
        # 使用sudo：echo %s|sudo -S %s' % (password, command)
        log = os.popen('echo asdf1234 |sudo -S ./upgrader_ota_file/upgrade_stress_test_one/upgrade_stress_test')
        return log.readlines()
