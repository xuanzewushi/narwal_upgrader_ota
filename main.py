# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs


import sys
from PyQt6.QtWidgets import *
from windows.main_window import MainWindow
from child_window import ChildWindow


def main():
    # 创建应用
    window_application = QApplication(sys.argv)
    # 设置登录窗口
    main_win = MainWindow()
    child_win = ChildWindow()
    main_win.show()
    main_win.run_button.clicked.connect(child_win.open)
    # 设置应用退出
    sys.exit(window_application.exec())


if __name__ == "__main__":
    main()


