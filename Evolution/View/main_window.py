from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from View.Ui_MainWindow import Ui_MainWindow

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

    def quit_application(self):
        """Quits the application"""
        QtCore.QCoreApplication.quit()