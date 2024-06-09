#!/usr/bin/env python3

"""
Generated with Designer from PyQt6-tools
"""

# 3rd party
from PyQt6 import QtCore, QtGui, QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class MainDesign(object):
    def __init__(self):
        self.central = None
        self.central_layout = None

        self.info_group = None
        self.info_layout = None

        self.canvas = None
        self.tabs = None

        self.label_tab = None
        self.layers_tab = None
        self.layers_layout = None
        self.layers_list = None

        self.x_label = None
        self.x_value = None
        self.y_label = None
        self.y_value = None
        self.z_label = None
        self.z_value = None
        self.layer_label = None
        self.layer_value = None

        self.menu_bar = None
        self.status_bar = None

    def setup_ui(self, main):
        main.setObjectName("main")
        main.resize(1280, 720)
        main.setMinimumSize(QtCore.QSize(1280, 720))
        self.central = QtWidgets.QWidget(parent=main)
        self.central.setObjectName("central")
        self.central_layout = QtWidgets.QGridLayout(self.central)
        self.central_layout.setObjectName("central_layout")
        self.info_group = QtWidgets.QGroupBox(parent=self.central)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_group.sizePolicy().hasHeightForWidth())
        self.info_group.setSizePolicy(sizePolicy)
        self.info_group.setObjectName("info_group")
        self.info_layout = QtWidgets.QFormLayout(self.info_group)
        self.info_layout.setLabelAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.info_layout.setObjectName("info_layout")
        self.x_label = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.x_label.setFont(font)
        self.x_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.x_label.setObjectName("x_label")
        self.info_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.x_label
        )
        self.x_value = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setBold(True)
        self.x_value.setFont(font)
        self.x_value.setObjectName("x_value")
        self.info_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.x_value
        )
        self.y_label = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.y_label.setFont(font)
        self.y_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.y_label.setObjectName("y_label")
        self.info_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.y_label
        )
        self.z_label = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.z_label.setFont(font)
        self.z_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.z_label.setObjectName("z_label")
        self.info_layout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.z_label
        )
        self.y_value = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setBold(True)
        self.y_value.setFont(font)
        self.y_value.setObjectName("y_value")
        self.info_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.y_value
        )
        self.z_value = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setBold(True)
        self.z_value.setFont(font)
        self.z_value.setObjectName("z_value")
        self.info_layout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.z_value
        )
        self.layer_label = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.layer_label.setFont(font)
        self.layer_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.layer_label.setObjectName("layer_label")
        self.info_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.layer_label
        )
        self.layer_value = QtWidgets.QLabel(parent=self.info_group)
        font = QtGui.QFont()
        font.setBold(True)
        self.layer_value.setFont(font)
        self.layer_value.setObjectName("layer_value")
        self.info_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.layer_value
        )
        self.central_layout.addWidget(self.info_group, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            15,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Maximum,
        )
        self.central_layout.addItem(spacerItem, 2, 1, 1, 1)
        self.canvas = QVTKRenderWindowInteractor(parent=self.central)
        self.canvas.setObjectName("canvas")
        self.central_layout.addWidget(self.canvas, 0, 0, 4, 1)
        self.label_tab = QtWidgets.QLabel(parent=self.central)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tab.sizePolicy().hasHeightForWidth())
        self.label_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_tab.setFont(font)
        self.label_tab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_tab.setObjectName("label_tab")
        self.central_layout.addWidget(self.label_tab, 1, 1, 1, 1)
        self.tabs = QtWidgets.QTabWidget(parent=self.central)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setMinimumSize(QtCore.QSize(200, 0))
        self.tabs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tabs.setObjectName("tabs")
        self.layers_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layers_tab.sizePolicy().hasHeightForWidth())
        self.layers_tab.setSizePolicy(sizePolicy)
        self.layers_tab.setObjectName("layers_tab")
        self.layers_layout = QtWidgets.QFormLayout(self.layers_tab)
        self.layers_layout.setLabelAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.layers_layout.setObjectName("layers_layout")
        self.tabs.addTab(self.layers_tab, "")
        self.central_layout.addWidget(self.tabs, 0, 1, 1, 1)
        main.setCentralWidget(self.central)
        self.menu_bar = QtWidgets.QMenuBar(parent=main)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
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
        self.info_group.setTitle(_translate("main", "Information"))
        self.x_label.setText(_translate("main", "x"))
        self.x_value.setText(_translate("main", " - "))
        self.y_label.setText(_translate("main", "y"))
        self.z_label.setText(_translate("main", "z"))
        self.y_value.setText(_translate("main", " - "))
        self.z_value.setText(_translate("main", " - "))
        self.layer_label.setText(_translate("main", "Layer"))
        self.layer_value.setText(_translate("main", " - "))
        self.label_tab.setText(_translate("main", "Drag & drop to add a layer"))
        self.tabs.setTabText(
            self.tabs.indexOf(self.layers_tab), _translate("main", "Layers")
        )
