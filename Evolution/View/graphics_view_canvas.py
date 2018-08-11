"""Python Class that represents a canvas to be drawn on"""
from PyQt5 import QtWidgets

class GraphicsViewCanvas(QtWidgets.QGraphicsView):
    """Canvas class that allows to be drawn on"""

    def __init__(self, container):
        super().__init__(container)
        self.dot_size = 4

    def draw_scene(self, board, dot_list):
        """Draws the complete scene"""
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.clear()
        self.draw_boundaries(board.width, board.height)
        self.draw_dots(dot_list)
        self.setScene(self.scene)

    def draw_boundaries(self, width, height):
        """Draws the boundary frame of the field"""
        self.scene.addItem(QtWidgets.QGraphicsRectItem(-width/2, -height/2, width, height))

    def draw_dots(self, dot_list):
        """Draws the dots at the given positions"""
        for dot in dot_list:
            self.scene.addItem(
                QtWidgets.QGraphicsEllipseItem(
                    dot.pos_x, dot.pos_y, self.dot_size, self.dot_size))
