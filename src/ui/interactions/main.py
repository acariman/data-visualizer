#!/usr/bin/env python3

# Core
import logging

# 1st party
from src.manipulation import Manipulator
from src.ui.design.main import MainDesign
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


class MainWindow(QMainWindow, MainDesign):
    def __init__(self):
        logging.info("Initializing main window")

        super().__init__()
        self.setup_ui(self)
        self.mpl = Manipulator(self.canvas)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        logging.debug("Drag event")

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        logging.debug("Drop event")

        for url in event.mimeData().urls():
            file = url.toLocalFile()
            self.add_layer(file)

    def add_layer(self, file):
        logging.debug(f"Adding layer")
        layer = self.mpl.add(file)

        item_widget = QWidget()
        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(0, 0, 0, 0)

        layer_name = QLabel(layer["nice-name"])
        checkbox = QCheckBox()
        checkbox.setChecked(layer["state"])
        checkbox.stateChanged.connect(lambda state, lyr=layer["name"]: self.toggle_layer(state, lyr))

        # Añadir los widgets al layout
        item_layout.addWidget(checkbox)
        item_layout.addWidget(layer_name)
        item_widget.setLayout(item_layout)

        # Añadir el widget contenedor al QListWidget
        list_item = QListWidgetItem(self.layers_list)
        self.layers_list.setItemWidget(list_item, item_widget)

        if layer["state"]:
            self.mpl.show(layer["name"])
        else:
            self.mpl.hide(layer["name"])

    def toggle_layer(self, state, layer):
        if state == Qt.CheckState.Checked.value:
            logging.debug(f"Showing layer {layer}")
            self.mpl.show(layer)
        else:
            logging.debug(f"Hiding layer {layer}")
            self.mpl.hide(layer)
