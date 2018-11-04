#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@dev: Simple PyQt5 window for GUI

To be updated..
"""

try:
    import PyQt5
except:
    print("\033[91m[-] Python module PyQt5 is missing.\033[0m Please install it (on Ubuntu: sudo apt install python-pyqt5)")
    exit(1)

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
