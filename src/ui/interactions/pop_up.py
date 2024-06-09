#!/usr/bin/env python3

# Core
import re
import logging

# 1st party
from src.ui.design.pop_up import CSVPopUpDesign
from PyQt6.QtWidgets import *


patterns = {
    "x_cb": re.compile(r"\b(\w*[_\s-]?x|x[_\s-]?\w*)\b", re.IGNORECASE),
    "y_cb": re.compile(r"\b(\w*[_\s-]?y|y[_\s-]?\w*)\b", re.IGNORECASE),
    "z_cb": re.compile(r"\b(\w*[_\s-]?z|z[_\s-]?\w*)\b", re.IGNORECASE),
}


class CSVPopUp(QDialog, CSVPopUpDesign):
    def __init__(self, file):
        logging.info("Initializing pop up")

        super().__init__()
        self.setup_ui(self)

        self.separator = self.sep_line.text()
        self.file = file
        self.layer_text.setText(str(file.stem))

        self.ok.clicked.connect(self.accept)
        self.sep_line.textChanged.connect(self.update)

        self.update()

    def update(self):
        logging.debug("Updating pop up")
        with open(self.file, "r") as file:
            line = file.readline().strip()

        cols = line.split(self.separator)

        suggestions = {}
        for col in cols:
            for axis, pattern in patterns.items():
                if pattern.search(col):
                    suggestions[axis] = col
        logging.debug(f"Suggesting following columns: {suggestions}")

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            name = widget.objectName()
            if isinstance(widget, QComboBox) and name not in ("color_cb",):
                widget.clear()
                widget.addItems(cols)

                if name in suggestions:
                    widget.setCurrentText(suggestions[name])
