"""The Main Window Class"""
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from View.Ui_MainWindow import Ui_MainWindow
from Model.game_engine import GameEngine
from Model.iteration_thread import IterationThread


class MainWindow(QMainWindow):
    """Class that represents the Main Window"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self._init_model()
        self._init_ui()

    def _init_model(self):
        """sets up the model"""
        self.eng = GameEngine()
        self.iteration_thread = IterationThread(self.eng)
        self.iteration_thread.finished_signal.connect(self.draw_board)
        self.restarter = None

    def _init_ui(self):
        """Sets up the UI"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit_button.clicked.connect(self.quit_application)
        self.ui.start_button.clicked.connect(self.draw_board)
        self.ui.one_iteration_button.clicked.connect(self.start_one_iteration)
        self.ui.fast_forward_button.clicked.connect(self.continuous_iteration)
        self.ui.next_generation_button.clicked.connect(self.calculate_next_generation)
        self.show()

    def draw_board(self):
        """Draws the current state of the board"""
        self.ui.display_graphics.draw_scene(self.eng.board, self.eng.pool, self.eng.info_text())

    def start_one_iteration(self):
        """Iterates one step and draws the board"""
        self.iteration_thread.start()

    def continuous_iteration(self):
        """Based on the ffwd toggle button continuously restarts the iteration thread"""
        if self.ui.fast_forward_button.isChecked():
            self.iteration_thread.finished_signal.connect(self.restart_iteration_thread)
            self.iteration_thread.start()
        else:
            self.iteration_thread.finished_signal.disconnect(self.restart_iteration_thread)

    def restart_iteration_thread(self):
        """Restarts the iteration thread"""
        if self.eng.iteration_counter >= self.eng.iteration_max:
            self.eng.generate_new_generation()

        while self.iteration_thread.isRunning():
            time.sleep(0.1)
            # print("I have slept a bit, thread is still running? " + str(self.iteration_thread.isRunning()))

        if self.ui.fast_forward_button.isChecked():
            self.iteration_thread.start()

    def calculate_next_generation(self):
        """Calculates the next generation"""
        self.eng.generate_new_generation()

    @staticmethod
    def quit_application():
        """Quits the application"""
        QtCore.QCoreApplication.quit()
