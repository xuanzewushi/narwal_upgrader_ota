# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs
import os
import sys
from PyQt6.QtWidgets import *
from windows.main_window import MainWindow


def main():
    # 创建应用
    window_application = QApplication(sys.argv)
    # 设置登录窗口
    main_win = MainWindow()
    # child_win = ChildWindow()
    main_win.show()

    # 设置应用退出
    sys.exit(window_application.exec())


if __name__ == "__main__":
    main()


