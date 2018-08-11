"""The Main Window Class"""
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from View.Ui_MainWindow import Ui_MainWindow
from Model.game_engine import GameEngine


class MainWindow(QMainWindow):
    """Class that represents the Main Window"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self._init_model()
        self._init_ui()

    def _init_model(self):
        """sets up the model"""
        self.eng = GameEngine()

    def _init_ui(self):
        """Sets up the UI"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit_button.clicked.connect(self.quit_application)
        self.ui.start_button.clicked.connect(self.draw_board)
        self.ui.one_iteration_button.clicked.connect(self.iterate_and_draw)
        self.ui.fast_forward_button.clicked.connect(self.continuous_update)
        self.show()

    def draw_board(self):
        """Draws the current state of the board"""
        self.ui.display_graphics.draw_scene(self.eng.board, self.eng.pool)

    def iterate_and_draw(self):
        """Iterates one step and draws the board"""
        self.eng.iterate()
        self.draw_board()

    def continuous_update(self):
        """Continuously updates the board

        The Window freezes with this function call 
        --> move it to a different thread with signaling"""
        for i in range(self.eng.iteration_max - self.eng.iteration_counter):
            self.iterate_and_draw()
            self.repaint()
            # time.sleep(0.2)
            print("Iteration: " + str(i))

    def quit_application(self):
        """Quits the application"""
        QtCore.QCoreApplication.quit()
