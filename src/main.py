#!/usr/bin/env python3

# Core
import logging

# 1st party
from src.ui.interactions.main import MainWindow
from PyQt6.QtWidgets import QApplication


def run_ui():
    logging.debug("Running UI")

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    run_ui()
