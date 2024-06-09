#!/usr/bin/env python3

# 1st party
from src.ui.design import Design
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()

    window.show()
    app.exec()
