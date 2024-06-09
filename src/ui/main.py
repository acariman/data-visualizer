#!/usr/bin/env python3

# 1st party
from src.manipulation import Manipulator
from src.ui.design import Design
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


class Window(QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mpl = Manipulator(self.canvas)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file = url.toLocalFile()
            self.mpl.add(file)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()

    window.show()
    app.exec()
