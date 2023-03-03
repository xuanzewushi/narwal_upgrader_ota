#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: __init__.py.py
@time: 2023/3/3 下午12:08
"""


import sys
import time

import yaml
from PyQt6.QtWidgets import *
# from conf import IO_yamls
# from conftest import edit_choice_yaml


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
        # grid.setSpacing(5)

        # 说明文案区
        self.configuration_one = QLabel('一、文案\n'
                                        '二、文案')
        # 新增机器人按钮
        self.add_robot = QPushButton('新增机器人')
        self.renovate = QPushButton('刷新')

        # 运行脚本按钮
        self.run_button = QPushButton('运行脚本')

        # 输入框文案
        self.save_tip = QLabel()
        self.devices_id = QLabel(' '*18 + 'stress_test_config.ini文件：')
        self.upgrade_version = QLabel(' '*6 + 'robot_adb_config.ini文件：')
        self.downgrade_version = QLabel('downgrade_version：')

        # 输入框
        self.log_text = QTextEdit()
        self.devices_id_ql = QLineEdit()
        self.upgrade_version_ql = QLineEdit()
        self.downgrade_version_ql = QLineEdit()
        self.config_text = QTextEdit()

        # 区域分割符
        self.label1 = QLabel('— — '*14 + '第1个脚本' + '— — '*14)
        self.label2 = QLabel(' ')
        # self.label3 = QLabel(' ')
        # self.mouse_right_click = QPushButton('鼠标右击')
        # self.sleep_time_button = QPushButton('写入时间')
        # self.clear_text = QPushButton('删除上一个配置')
        # self.clear_text_all = QPushButton('删除全部配置')
        # self.save_text = QPushButton('保存配置')

        self.setLayout(self.grid)
        self.main_win()
        self.show()

    def main_win(self):
        # 左边配置按钮
        # self.button_one.clicked.connect(self.configuration_one)
        # self.button_two.clicked.connect(self.configuration_two)
        # self.button_three.clicked.connect(self.configuration_three)

        # 配置框
        self.config_text.setPlaceholderText('请选择配置')
        self.config_text.setReadOnly(True)  # 只读
        self.log_text.setPlaceholderText('执行配置后显示log')
        self.log_text.setReadOnly(True)  # 只读

        # 输入框默认文案
        self.devices_id_ql.setPlaceholderText('机器人devices_id')
        self.upgrade_version_ql.setPlaceholderText('ota升级的固件版本')
        self.downgrade_version_ql.setPlaceholderText('需要验证的固件版本')

        # self.coordinate_x.resize(1, 2)
        # self.coordinate_y.resize(2, 3)
        # self.coordinate_button.clicked.connect(self.edit_coordinate)
        # self.mouse_left_click.clicked.connect(self.left_click)
        # self.mouse_right_click.clicked.connect(self.right_click)
        # self.sleep_time_edit.setPlaceholderText('单位:s')
        # self.sleep_time_button.clicked.connect(self.t_edit)
        # self.clear_text.clicked.connect(self.text_clear)
        # self.clear_text_all.clicked.connect(self.text_clear_all)
        # self.save_text.clicked.connect(self.save_configuration)

        # 说明文案区
        self.grid.addWidget(self.configuration_one, 1, 0, 1, 10)  # x, y, n, m。x是第几行，y是第几列，n是占多少行，m是多少列

        # 区域分割符
        self.grid.addWidget(self.label1, 2, 0, 1, 9)
        self.grid.addWidget(self.label2, 3, 0, 1, 9)
        # self.grid.addWidget(self.label3, 9, 0, 1, 9)

        # 输入框文案
        self.grid.addWidget(self.devices_id, 4, 6, 1, 1)
        self.grid.addWidget(self.upgrade_version, 5, 6, 1, 1)
        self.grid.addWidget(self.downgrade_version, 6, 6, 1, 1)

        # 输入框
        self.grid.addWidget(self.devices_id_ql, 4, 7, 1, 3)
        self.grid.addWidget(self.upgrade_version_ql, 5, 7, 1, 3)
        self.grid.addWidget(self.downgrade_version_ql, 6, 7, 1, 3)
        # grid.addWidget(self.button_choice, 2, 4, 1, 2)

        # 内容框
        # self.grid.addWidget(self.log_text, 10, 0, 1, 10)
        self.grid.addWidget(self.config_text, 4, 1, 6, 5)

        # 配置文件
        self.grid.addWidget(self.robot_adb_config, 4, 0)
        self.grid.addWidget(self.stress_test_config, 5, 0)

        # 运行脚本按钮
        self.grid.addWidget(self.run_button, 9, 0)

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








