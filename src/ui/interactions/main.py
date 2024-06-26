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
        self.mpl.canvas.add_callback("MouseMove", self.get_info)

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
        pop_up = CSVPopUp(file)
        if pop_up.exec() == QDialog.DialogCode.Accepted:
            params = {
                "separator": pop_up.sep_line.text(),
                "x": pop_up.x_cb.currentText(),
                "y": pop_up.y_cb.currentText(),
                "z": pop_up.z_cb.currentText(),
                "color": pop_up.color_cb.currentText(),
            }

        else:
            logging.warning(f"Pop up was closed")
            return

        layer = self.mpl.add_csv(file=file, params=params)

        if not layer:
            return

        self.add_layer(layer)

    def add_layer(self, layer):
        logging.debug(f"Adding layer")

        label = QLabel(layer["nice-name"], parent=self.layers_tab)
        checkbox = QCheckBox(parent=self.layers_tab)
        checkbox.setChecked(layer["state"])
        checkbox.stateChanged.connect(
            lambda state, lyr=layer["name"]: self.toggle_layer(state, lyr)
        )

        cnt = self.layers_layout.count()
        self.layers_layout.setWidget(cnt, QFormLayout.ItemRole.LabelRole, checkbox)
        self.layers_layout.setWidget(cnt, QFormLayout.ItemRole.FieldRole, label)

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

    def get_info(self, evt):
        info = self.mpl.get_info(evt)
        if info is None:
            self.layer_value.setText(" - ")
            self.x_value.setText(" - ")
            self.y_value.setText(" - ")
            self.z_value.setText(" - ")
        else:
            self.layer_value.setText(info["layer"])
            self.x_value.setText("{:,.1f}".format(info["x"]))
            self.y_value.setText("{:,.1f}".format(info["y"]))
            self.z_value.setText("{:,.1f}".format(info["z"]))
