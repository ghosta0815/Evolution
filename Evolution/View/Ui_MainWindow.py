# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Manuel\Source\Repos\Evolution\Evolution\View\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 795)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.one_iteration_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_iteration_button.setObjectName("one_iteration_button")
        self.verticalLayout.addWidget(self.one_iteration_button)
        self.fast_forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.fast_forward_button.setObjectName("fast_forward_button")
        self.verticalLayout.addWidget(self.fast_forward_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setObjectName("quit_button")
        self.verticalLayout.addWidget(self.quit_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.display_graphics = GraphicsViewCanvas(self.centralwidget)
        self.display_graphics.setObjectName("display_graphics")
        self.gridLayout.addWidget(self.display_graphics, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.one_iteration_button.setText(_translate("MainWindow", "Next Iteration"))
        self.fast_forward_button.setText(_translate("MainWindow", "Fast Forward"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))

from View.graphics_view_canvas import GraphicsViewCanvas
