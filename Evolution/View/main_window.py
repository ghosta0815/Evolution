from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from View.Ui_MainWindow import Ui_MainWindow
import random


class MainWindow(QMainWindow):
    """Class that represents the Main Window"""
    def __init__(self):
        super(MainWindow, self).__init__()

        self._init_ui()

    def _init_ui(self):
        """Sets up the UI"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        

        self.ui.quit_button.clicked.connect(self.quit_application)
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

    def quit_application(self):
        """Quits the application"""
        QtCore.QCoreApplication.quit()
