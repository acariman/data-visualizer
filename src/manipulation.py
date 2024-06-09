#!/usr/bin/env python3

# Core
from pathlib import Path

# 3rd party
import vedo
import pandas as pd


class Manipulator:
    def __init__(self, widget=None):
        self.layers = {}
        self.canvas = vedo.Plotter(qt_widget=widget)

    def add(self, file):
        file = Path(file)

        if file.suffix == ".csv":
            data = pd.read_csv(file)
            self.layers[file.stem] = {
                "actor": vedo.Points(data[["x", "y", "z"]]),
                "raw": data,
            }

        self.canvas += self.layers[file.stem]["actor"]

    def show(self):
        self.canvas.show()
