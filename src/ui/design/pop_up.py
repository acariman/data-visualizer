#!/usr/bin/env python3

"""
Generated with Designer from PyQt6-tools
"""

# 3rd party
from PyQt6 import QtCore, QtWidgets


class CSVPopUpDesign(object):
    def __init__(self):
        self.layout = None

        self.layer_label = None
        self.layer_text = None
        self.sep_label = None
        self.sep_line = None
        self.color_label = None
        self.color_cb = None

        self.x_label = None
        self.x_cb = None
        self.y_label = None
        self.y_cb = None
        self.z_label = None
        self.z_cb = None

        self.ok = None

    def setup_ui(self, pop_up):
        pop_up.setObjectName("pop_up")
        pop_up.resize(270, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pop_up.sizePolicy().hasHeightForWidth())
        pop_up.setSizePolicy(sizePolicy)
        pop_up.setMinimumSize(QtCore.QSize(270, 210))
        pop_up.setMaximumSize(QtCore.QSize(270, 210))
        self.layout = QtWidgets.QFormLayout(pop_up)
        self.layout.setObjectName("layout")
        self.layer_label = QtWidgets.QLabel(parent=pop_up)
        self.layer_label.setObjectName("layer_label")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.layer_label)
        self.layer_text = QtWidgets.QLabel(parent=pop_up)
        self.layer_text.setObjectName("layer_text")
        self.layout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.layer_text)
        self.sep_label = QtWidgets.QLabel(parent=pop_up)
        self.sep_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sep_label.setObjectName("sep_label")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sep_label)
        self.sep_line = QtWidgets.QLineEdit(parent=pop_up)
        self.sep_line.setObjectName("sep_line")
        self.layout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sep_line)
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
        self.color_label = QtWidgets.QLabel(parent=pop_up)
        self.color_label.setObjectName("color_label")
        self.layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.color_label)
        self.color_cb = QtWidgets.QComboBox(parent=pop_up)
        self.color_cb.setObjectName("color_cb")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.color_cb.addItem("")
        self.layout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.color_cb)
        self.ok = QtWidgets.QPushButton(parent=pop_up)
        self.ok.setObjectName("ok")
        self.layout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.ok)

        self.retranslateUi(pop_up)
        QtCore.QMetaObject.connectSlotsByName(pop_up)

    def retranslateUi(self, pop_up):
        _translate = QtCore.QCoreApplication.translate
        pop_up.setWindowTitle(_translate("pop_up", "Dialog"))
        self.layer_label.setText(_translate("pop_up", "Layer"))
        self.layer_text.setText(_translate("pop_up", "file-nice-name"))
        self.sep_label.setText(_translate("pop_up", "Separator"))
        self.sep_line.setText(_translate("pop_up", ","))
        self.x_label.setText(_translate("pop_up", "x"))
        self.y_label.setText(_translate("pop_up", "y"))
        self.z_label.setText(_translate("pop_up", "z"))
        self.color_label.setText(_translate("pop_up", "Color"))
        self.color_cb.setItemText(0, _translate("pop_up", "black"))
        self.color_cb.setItemText(1, _translate("pop_up", "red"))
        self.color_cb.setItemText(2, _translate("pop_up", "green"))
        self.color_cb.setItemText(3, _translate("pop_up", "blue"))
        self.color_cb.setItemText(4, _translate("pop_up", "yellow"))
        self.ok.setText(_translate("pop_up", "OK"))
