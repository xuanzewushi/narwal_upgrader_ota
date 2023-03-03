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
# from conf import IO_yamls
# from conftest import edit_choice_yaml

"""
1.新增压测机器人数量
2.可以查看不同压测机器人的数据
3.可以选择不同机器人配置进行执行脚本
    3.1 单独子弹窗，每执行1个压测的机器人脚本就启动1个子弹窗
    3.2 已启动的机器人脚本不可继续启动，需等原来的脚本停掉
4.脚本的结果文档可以拷贝到自己指定的工作目录/显示工作目录
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
        self.configuration_one = QLabel('一、文案\n'
                                        '二、文案')
        # -----------------分割符-----------------
        # 区域分割符
        self.label1 = QLabel('— — ' * 20)

        # 刷新按钮
        self.renovate = QPushButton('刷新')

        # 文案
        self.robot_times = QLabel('当前可执行机器人：')
        self.run_robot_times = QLabel('当前正在执行的机器人数量：')

        # 运行脚本按钮
        self.run_button = QPushButton('运行脚本')

        # 输入框
        self.robot_times_edit = QLineEdit()

        # -----------------分割符-----------------
        # 区域分割符
        self.label2 = QLabel('— — '*6 + '当前选中第1个机器人' + '— — '*6)

        # 文案
        self.save_tip = QLabel()
        self.stress_test_config = QLabel('stress_test_config.ini文件：')
        self.robot_adb_config = QLabel('robot_adb_config.ini文件：')

        # 文件文本框
        self.stress_test_config_text = QTextEdit()
        self.robot_adb_config_text = QTextEdit()

        self.setLayout(self.grid)
        self.main_win()
        self.show()

    def main_win(self):
        # 输入框默认文案
        self.robot_times_edit.setPlaceholderText('ota升级的固件版本')

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
        self.grid.addWidget(self.renovate, 3, 2)

        # -----------分割符------------
        # 区域分割符
        self.grid.addWidget(self.label2, 6, 0, 1, 9)
        # 文件内容说明文案
        self.grid.addWidget(self.stress_test_config, 7, 0, 1, 1)
        self.grid.addWidget(self.robot_adb_config, 7, 4, 1, 1)

        # 文件内容框
        self.grid.addWidget(self.robot_adb_config_text, 7, 5, 5, 3)
        self.grid.addWidget(self.stress_test_config_text, 7, 1, 5, 3)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', "是否关闭程序?")
        if str(reply) == 'StandardButton.Yes':
            event.accept()
        else:
            event.ignore()

    # def w_yaml(self):
    #     if self.button_choice.text() != '请先选择配置文件':
    #         if self.configuration_text.toPlainText() != '':
    #             pass
    #             # edit_choice_yaml(self.configuration_text, self.button_choice, self.save_tip)
    #         else:
    #             self.information('写入配置')
    #     else:
    #         self.information('选择配置文件')
    #
    # def massage(self, tid, dt1=None, dt2=None):
    #     p_text = self.button_choice.text()
    #     if p_text != '请先选择配置文件':
    #         if tid == 1:
    #             self.configuration_text.append(dt1)
    #         elif tid == 2:
    #             if dt1 != '' and dt2 != '':
    #                 self.configuration_text.append(dt1 + ',' + dt2)
    #             else:
    #                 self.information('填写坐标')
    #         elif tid == 3:
    #             if str(dt1) != '':
    #                 self.configuration_text.append(dt1)
    #             else:
    #                 self.information('填写时间')
    #         else:
    #             print('无法识别的id')
    #     else:
    #         self.information('选择配置文件')
    #
    # def information(self, mass):
    #     information = QMessageBox.information(self, '警告！', '请先' + mass)
    #
    # # 调用读取文件方法区
    # def configuration_one(self):
    #     self.button_choice.setText('配置一')
    #     # self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置一')))
    #
    # def configuration_two(self):
    #     self.button_choice.setText('配置二')
    #     # self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置二')))
    #
    # def configuration_three(self):
    #     self.button_choice.setText('配置三')
    #     # self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置三')))
    #
    # # 调用信息弹窗区
    # def edit_coordinate(self):
    #     self.massage(2, self.coordinate_x.text(), self.coordinate_y.text())
    #
    # def left_click(self):
    #     self.massage(1, self.mouse_left_click.text())
    #
    # def right_click(self):
    #     self.massage(1, self.mouse_right_click.text())
    #
    # def t_edit(self):
    #     self.massage(3, self.sleep_time_edit.text())
    #
    # def text_clear(self):
    #     if self.button_choice.text() != '请先选择配置文件':
    #         text = self.configuration_text.toPlainText()
    #         data = text.split('\n')
    #         data.pop(-1)
    #         self.configuration_text.setText('\n'.join(data))
    #     else:
    #         self.information('选择配置文件')
    #
    # def text_clear_all(self):
    #     if self.button_choice.text() != '请先选择配置文件':
    #         self.configuration_text.clear()
    #     else:
    #         self.information('选择配置文件')
    #
    # def save_configuration(self):
    #     self.w_yaml()








