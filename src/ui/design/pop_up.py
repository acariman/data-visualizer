#!/usr/bin/env python3

"""
Generated with Designer from PyQt6-tools
"""

# 3rd party
from PyQt6 import QtCore, QtWidgets


class CSVPopUpDesign(object):
    def __init__(self):
        self.layout = None
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
        pop_up.resize(270, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pop_up.sizePolicy().hasHeightForWidth())
        pop_up.setSizePolicy(sizePolicy)
        pop_up.setMinimumSize(QtCore.QSize(270, 190))
        pop_up.setMaximumSize(QtCore.QSize(270, 190))
        self.layout = QtWidgets.QFormLayout(pop_up)
        self.layout.setObjectName("layout")
        self.sep_label = QtWidgets.QLabel(parent=pop_up)
        self.sep_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sep_label.setObjectName("sep_label")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sep_label)
        self.sep_line = QtWidgets.QLineEdit(parent=pop_up)
        self.sep_line.setObjectName("sep_line")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sep_line)
        self.desc_label = QtWidgets.QLabel(parent=pop_up)
        self.desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.desc_label.setObjectName("desc_label")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.desc_label)
        self.desc_cb = QtWidgets.QComboBox(parent=pop_up)
        self.desc_cb.setObjectName("desc_cb")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.desc_cb)
        self.x_label = QtWidgets.QLabel(parent=pop_up)
        self.x_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.x_label.setObjectName("x_label")
        self.layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.x_label)
        self.x_cb = QtWidgets.QComboBox(parent=pop_up)
        self.x_cb.setObjectName("x_cb")
        self.layout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.x_cb)
        self.y_label = QtWidgets.QLabel(parent=pop_up)
        self.y_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.y_label.setObjectName("y_label")
        self.layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.y_label)
        self.y_cb = QtWidgets.QComboBox(parent=pop_up)
        self.y_cb.setObjectName("y_cb")
        self.layout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.y_cb)
        self.z_label = QtWidgets.QLabel(parent=pop_up)
        self.z_label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.z_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.z_label.setObjectName("z_label")
        self.layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.z_label)
        self.z_cb = QtWidgets.QComboBox(parent=pop_up)
        self.z_cb.setObjectName("z_cb")
        self.layout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.z_cb)
        self.ok = QtWidgets.QPushButton(parent=pop_up)
        self.ok.setObjectName("ok")
        self.layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.ok)

        self.retranslateUi(pop_up)
        QtCore.QMetaObject.connectSlotsByName(pop_up)

    def retranslateUi(self, pop_up):
        _translate = QtCore.QCoreApplication.translate
        pop_up.setWindowTitle(_translate("pop_up", "Dialog"))
        self.sep_label.setText(_translate("pop_up", "Separator"))
        self.sep_line.setText(_translate("pop_up", ","))
        self.desc_label.setText(_translate("pop_up", "Descriptor"))
        self.x_label.setText(_translate("pop_up", "x"))
        self.y_label.setText(_translate("pop_up", "y"))
        self.z_label.setText(_translate("pop_up", "z"))
        self.ok.setText(_translate("pop_up", "OK"))
