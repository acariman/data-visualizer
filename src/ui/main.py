#!/usr/bin/env python3

# Core
import logging

# 1st party
from src.manipulation import Manipulator
from src.ui.design import Design
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


class Window(QMainWindow, Design):
    def __init__(self):
        logging.info("Initializing UI")

        super().__init__()
        self.setupUi(self)
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
            self.mpl.add(file)


def run():
    logging.debug("Running UI")

    app = QApplication([])
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    run()
