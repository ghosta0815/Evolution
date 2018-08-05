import sys
from PyQt5 import QtWidgets
from View.MainWindow import *


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec_())