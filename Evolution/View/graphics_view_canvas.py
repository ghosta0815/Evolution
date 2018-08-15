"""Python Class that represents a canvas to be drawn on"""
from PyQt5 import QtWidgets

class GraphicsViewCanvas(QtWidgets.QGraphicsView):
    """Canvas class that allows to be drawn on"""

    def __init__(self, container):
        super().__init__(container)
        self.dot_size = 4

    def draw_scene(self, board, dot_list, info_text):
        """Draws the complete scene"""
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.clear()
        self.draw_boundaries(board)
        self.draw_dots(dot_list)
        self.draw_target(board.target)
        self.draw_text(info_text, -board.width/2, board.height/2)
        self.setScene(self.scene)

    def draw_target(self, target):
        """Draws the target"""
        target_ellipse = QtWidgets.QGraphicsEllipseItem(target.pos_x - 3, -target.pos_y - 3, 6, 6)
        self.scene.addItem(target_ellipse)

    def draw_boundaries(self, board):
        """Draws the boundary frame of the field"""
        width = board.width
        height = board.height
        self.scene.addItem(QtWidgets.QGraphicsRectItem(
            -width/2-self.dot_size/2, -height/2-self.dot_size/2,
            width+self.dot_size/2, height+self.dot_size/2))
        for obstacle in board.obstacles:
            self.scene.addItem(QtWidgets.QGraphicsRectItem(
                obstacle.left, -obstacle.top, obstacle.right-obstacle.left, -obstacle.bot+obstacle.top
            ))

    def draw_dots(self, dot_list):
        """Draws the dots at the given positions"""
        for dot in dot_list:
            self.scene.addItem(
                QtWidgets.QGraphicsEllipseItem(
                    dot.pos_x-self.dot_size/2,
                    -dot.pos_y-self.dot_size/2,
                    self.dot_size,
                    self.dot_size))

    def draw_text(self, info_text, pos_x, pos_y):
        """Draws some text on the canvas"""
        text_item = QtWidgets.QGraphicsSimpleTextItem(info_text)
        text_item.setPos(pos_x, -pos_y)
        self.scene.addItem(text_item)
