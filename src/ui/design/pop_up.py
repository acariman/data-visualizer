#!/usr/bin/env python3

"""
Generated with Designer from PyQt6-tools
"""

# 3rd party
from PyQt6 import QtCore, QtWidgets


class PopUpDesign(object):
    def __init__(self):
        self.sep_label = None
        self.sep_line = None
        self.x_label = None
        self.y_label = None
        self.z_label = None
        self.x_cb = None
        self.y_cb = None
        self.z_cb = None
        self.desc_cb = None
        self.desc_label = None
        self.ok = None

    def setup_ui(self, pop_up):
        pop_up.setObjectName("pop_up")
        pop_up.resize(270, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pop_up.sizePolicy().hasHeightForWidth())
        pop_up.setSizePolicy(sizePolicy)
        pop_up.setMinimumSize(QtCore.QSize(270, 220))
        pop_up.setMaximumSize(QtCore.QSize(270, 220))
        self.desc_cb = QtWidgets.QComboBox(parent=pop_up)
        self.desc_cb.setGeometry(QtCore.QRect(90, 50, 161, 22))
        self.desc_cb.setObjectName("desc_cb")
        self.sep_line = QtWidgets.QLineEdit(parent=pop_up)
        self.sep_line.setGeometry(QtCore.QRect(90, 20, 161, 22))
        self.sep_line.setObjectName("sep_line")
        self.z_cb = QtWidgets.QComboBox(parent=pop_up)
        self.z_cb.setGeometry(QtCore.QRect(90, 140, 161, 22))
        self.z_cb.setObjectName("z_cb")
        self.desc_label = QtWidgets.QLabel(parent=pop_up)
        self.desc_label.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.desc_label.setObjectName("desc_label")
        self.x_cb = QtWidgets.QComboBox(parent=pop_up)
        self.x_cb.setGeometry(QtCore.QRect(90, 80, 161, 22))
        self.x_cb.setObjectName("x_cb")
        self.y_label = QtWidgets.QLabel(parent=pop_up)
        self.y_label.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.y_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.y_label.setObjectName("y_label")
        self.y_cb = QtWidgets.QComboBox(parent=pop_up)
        self.y_cb.setGeometry(QtCore.QRect(90, 110, 161, 22))
        self.y_cb.setObjectName("y_cb")
        self.z_label = QtWidgets.QLabel(parent=pop_up)
        self.z_label.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.z_label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.z_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.z_label.setObjectName("z_label")
        self.sep_label = QtWidgets.QLabel(parent=pop_up)
        self.sep_label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.sep_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sep_label.setObjectName("sep_label")
        self.x_label = QtWidgets.QLabel(parent=pop_up)
        self.x_label.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.x_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.x_label.setObjectName("x_label")
        self.ok = QtWidgets.QPushButton(parent=pop_up)
        self.ok.setGeometry(QtCore.QRect(30, 180, 201, 24))
        self.ok.setObjectName("ok")

        self.retranslateUi(pop_up)
        QtCore.QMetaObject.connectSlotsByName(pop_up)

    def retranslateUi(self, pop_up):
        _translate = QtCore.QCoreApplication.translate
        pop_up.setWindowTitle(_translate("pop_up", "Dialog"))
        self.sep_line.setText(_translate("pop_up", ","))
        self.desc_label.setText(_translate("pop_up", "Description"))
        self.y_label.setText(_translate("pop_up", "y"))
        self.z_label.setText(_translate("pop_up", "z"))
        self.sep_label.setText(_translate("pop_up", "Separator"))
        self.x_label.setText(_translate("pop_up", "x"))
        self.ok.setText(_translate("pop_up", "OK"))
