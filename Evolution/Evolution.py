"""This script starts an evolutionary algorithm with a GUI"""

import sys
from PyQt5 import QtWidgets
from View.main_window import MainWindow


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(APP.exec_())
