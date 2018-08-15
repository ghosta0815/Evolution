"""Threading"""
import time
from PyQt5 import QtCore

class IterationThread(QtCore.QThread):
    """Class that runs an iteration on a separate thread and calls back on finish"""
    finished_signal = QtCore.pyqtSignal(int)

    def __init__(self, engine):
        QtCore.QThread.__init__(self)
        self.engine = engine

    def run(self):
        """Performs one iteration of the engine and calls back on finish"""
        if self.engine.updating is False:
            self.engine.iterate()
            time.sleep(0.01)
            self.finished_signal.emit(1)
        else:
            self.finished_signal.emit(0)
