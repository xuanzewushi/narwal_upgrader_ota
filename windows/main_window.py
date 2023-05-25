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
from conf.config import *
from conf.oprate_ini_file import OprateIni

"""
1.新增压测机器人数量
2.可以查看不同压测机器人的数据
3.可以选择不同机器人配置进行执行脚本
    3.1 单独子弹窗，每执行1个压测的机器人脚本就启动1个子弹窗
    3.2 已启动的机器人脚本不可继续启动，需等原来的脚本停掉
"""


class MainWindow(QMainWindow):
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

        # widget
        widget = QWidget()

        # 引用grid布局
        self.grid = QGridLayout()

        # 说明文案区
        self.configuration_one = QLabel('注意事项：\n'
                                        '一、每个脚本只能单独运行一次，如果存在已运行的脚本，则不可再次运行\n'
                                        '二、切换脚本文件配置不可为空，需填写所拥有的脚本文件名称\n'
                                        '三、文件输入框内容可以编辑\n'
                                        '    1、upgrade_version为ota升级的版本，downgrade_version为本地回退版本\n'
                                        '    2、download_timeout_timer为下载超时时间，start_upgrade_timeout_timer为开始超时时间，'
                                        'upgrade_timeout_timer为升级超时时间\n'
                                        '    3、adb_device_id：为电脑连接机器人使用adb devices指令获取的adb device id\n'
                                        '四、测试多台机器人时，机器人的adb device id必须修改成不同的')
        # -----------------分割符-----------------
        # 区域分割符
        self.label1 = QLabel('— — ' * 30)

        # 刷新按钮
        # self.renovate = QPushButton('刷新')
        # self.renovate.clicked.connect(self.renovate_click)

        # 文案
        self.robot_times = QLabel('当前拥有脚本文件数量：' + get_robot_times())
        # self.run_robot_times = QLabel('当前正在执行的机器人数量：')

        # 运行脚本按钮
        self.run_button = QPushButton('运行脚本')
        self.run_button.clicked.connect(self.upgrade)

        # 输入框
        # self.robot_times_edit = QLineEdit()

        # -----------------分割符-----------------
        # 区域分割符
        self.label2 = QLabel('— — '*13 + '当前选中第1个脚本文件' + '— — '*13)
        self.label2.repaint()

        # 文案
        self.robot_data = QLabel('所拥有的脚本文件：' + get_robots())
        self.stress_test_config = QLabel('stress_test_config.ini文件：')
        self.robot_adb_config = QLabel('robot_adb_config.ini文件：')

        # 文件文本框
        _path = get_robot()[0]
        self.stress_test_config_text = QTextEdit()
        self.stress_test_config_text.setPlainText(self.get_data(_path, 'stress_test_config.ini'))
        self.robot_adb_config_text = QTextEdit()
        self.robot_adb_config_text.setPlainText(self.get_data(_path, 'robot_adb_config.ini'))

        # 按钮
        self.change_file = QPushButton('切换脚本文件')
        self.change_file.clicked.connect(self.change_robot)
        self.write_stress_test_config_text = QPushButton('保存编辑')
        self.write_stress_test_config_text.clicked.connect(self.write_stress_test_config)
        self.write_robot_adb_config_text = QPushButton('保存编辑')
        self.write_robot_adb_config_text.clicked.connect(self.write_robot_adb_config)

        # 切换机器人输入框
        self.change_file_line = QLineEdit()
        self.change_file_line.setText(str(get_robot()[0]))

        self.setLayout(self.grid)

        # 状态栏
        # self.statusBar()

        # 定义widget布局为grid
        widget.setLayout(self.grid)
        self.setCentralWidget(widget)
        self.statusBar()
        self.main_win()
        self.show()

    def main_win(self):
        # 说明文案
        self.grid.addWidget(self.configuration_one, 1, 0, 1, 8)  # x, y, n, m。x是第几行，y是第几列，n是占多少行，m是多少列

        # -----------分割符------------
        # 区域分割符
        self.grid.addWidget(self.label1, 2, 0, 1, 9)

        # 文案
        self.grid.addWidget(self.robot_times, 3, 0)
        # self.grid.addWidget(self.run_robot_times, 4, 0)

        # 按钮
        self.grid.addWidget(self.run_button, 5, 0)
        # self.grid.addWidget(self.renovate, 5, 1)

        # -----------分割符------------
        # 区域分割符
        self.grid.addWidget(self.label2, 6, 0, 1, 9)

        # 所拥有的机器人
        self.grid.addWidget(self.robot_data, 7, 0, 1, 10)

        # 按钮
        self.grid.addWidget(self.change_file, 8, 0)
        self.grid.addWidget(self.write_stress_test_config_text, 13, 0)
        self.grid.addWidget(self.write_robot_adb_config_text, 13, 4)

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

    def get_data(self, path, name):
        return OprateIni(path, name).read_ini_data()

    def write_stress_test_config(self):
        _path = self.change_file_line.text()
        name = 'stress_test_config.ini'
        data = self.stress_test_config_text.toPlainText()
        OprateIni(_path, name, data).write_ini_data()
        self.status_charge('写入成功！')

    def write_robot_adb_config(self):
        _path = self.change_file_line.text()
        name = 'robot_adb_config.ini'
        data = self.robot_adb_config_text.toPlainText()
        OprateIni(_path, name, data).write_ini_data()
        self.status_charge('写入成功！')

    def renovate_click(self):
        _path = get_robot()[0]
        stress_name = 'stress_test_config.ini'
        robot_name = 'robot_adb_config.ini'
        self.stress_test_config_text.setPlainText(self.get_data(_path, stress_name))
        self.robot_adb_config_text.setPlainText(self.get_data(_path, robot_name))

    def change_robot(self):
        _path = self.change_file_line.text()
        stress_name = 'stress_test_config.ini'
        robot_name = 'robot_adb_config.ini'
        # robot_list = ['one', 'two', 'three', 'four', 'five']
        for i in range(len(get_robot())):
            self.label2.setText('— — '*10 + '当前已打开[' + get_robot()[i] + ']的脚本文件' + '— — '*10)
        self.stress_test_config_text.setPlainText(self.get_data(_path, stress_name))
        self.robot_adb_config_text.setPlainText(self.get_data(_path, robot_name))
        self.status_charge('切换配置成功！')

    def status_charge(self, msg):
        self.statusBar().showMessage(msg)

    def upgrade(self):
        _path = self.change_file_line.text()
        upgrade_stress_test_one = "gnome-terminal -e 'bash -c \"echo qwer1234 |sudo -S ./upgrade_ota_file/" + str(_path) + "/upgrade_stress_test; exec bash\"'"
        # 执行脚本
        os.system(upgrade_stress_test_one)
        self.status_charge('成功运行脚本' + str(_path))






