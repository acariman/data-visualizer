#!/usr/bin/env python3

# Core
import logging
from pathlib import Path

# 1st party
from src.manipulation import Manipulator
from src.ui.design.main import MainDesign
from src.ui.interactions.pop_up import CSVPopUp
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
            file = Path(url.toLocalFile())

            if file.exists():
                logging.info(f"Adding new layer ({file})")
            else:
                logging.error(f"File does not exists ({file})")
                return

            if file.suffix == ".csv":
                self.add_layer_csv(file)
            else:
                logging.error(f"No valid layer ({file})")

    def add_layer_csv(self, file):
        params = None
        pop_up = CSVPopUp(file)
        if pop_up.exec() == QDialog.DialogCode.Accepted:
            params = {
                "separator": pop_up.sep_line.text(),
                "descriptor": pop_up.x_cb.currentText(),
                "x": pop_up.x_cb.currentText(),
                "y": pop_up.x_cb.currentText(),
                "z": pop_up.x_cb.currentText(),
            }

        layer = self.mpl.add_csv(file=file, params=params)

        if not layer:
            return

        self.add_layer(layer)

    def add_layer(self, layer):
        logging.debug(f"Adding layer")

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
