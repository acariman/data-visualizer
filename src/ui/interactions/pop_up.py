#!/usr/bin/env python3

# Core
import logging

# 1st party
from src.ui.design.pop_up import PopUpDesign
from PyQt6.QtWidgets import *


class PopUp(QDialog, PopUpDesign):
    def __init__(self):
        logging.info("Initializing pop up")

        super().__init__()
        self.setup_ui(self)

        self.ok.clicked.connect(self.accept)
