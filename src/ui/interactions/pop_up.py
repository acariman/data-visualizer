#!/usr/bin/env python3

# Core
import logging

# 1st party
from src.ui.design.pop_up import CSVPopUpDesign
from PyQt6.QtWidgets import *


class CSVPopUp(QDialog, CSVPopUpDesign):
    def __init__(self, file):
        logging.info("Initializing pop up")

        super().__init__()
        self.setup_ui(self)

        self.separator = self.sep_line.text()
        self.file = file
        self.layer_text.setText(str(file.name))

        self.ok.clicked.connect(self.accept)
        self.sep_line.textChanged.connect(self.update)

        self.update()

    def update(self):
        logging.debug("Updating pop up")
        with open(self.file, 'r') as file:
            line = file.readline().strip()

        cols = line.split(self.separator)

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QComboBox) and widget.objectName() not in ("color_cb",):
                widget.clear()
                widget.addItems(cols)
