#!/usr/bin/env python3

"""
Generated with Designer from PyQt6-tools
"""

# 3rd party
from PyQt6 import QtCore, QtGui, QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Design(object):
    def __init__(self):
        self.central = None
        self.gridLayout = None
        self.canvas = None
        self.tabs = None
        self.tab_layers = None
        self.menu_bar = None
        self.status_bar = None

    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(911, 622)
        self.central = QtWidgets.QWidget(parent=main)
        self.central.setObjectName("central")
        self.gridLayout = QtWidgets.QGridLayout(self.central)
        self.gridLayout.setObjectName("gridLayout")
        self.canvas = QVTKRenderWindowInteractor(parent=self.central)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.tabs = QtWidgets.QTabWidget(parent=self.central)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab_layers = QtWidgets.QWidget()
        self.tab_layers.setObjectName("tab_layers")
        self.tabs.addTab(self.tab_layers, "")
        self.gridLayout.addWidget(self.tabs, 0, 1, 1, 1)
        main.setCentralWidget(self.central)
        self.menu_bar = QtWidgets.QMenuBar(parent=main)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 911, 22))
        self.menu_bar.setObjectName("menu_bar")
        main.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(parent=main)
        self.status_bar.setObjectName("status_bar")
        main.setStatusBar(self.status_bar)

        self.retranslateUi(main)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Data visualizer"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_layers), _translate("main", "Layers"))
