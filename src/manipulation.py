#!/usr/bin/env python3

# Core
import logging

# Core
from pathlib import Path

# 3rd party
import vedo
import pandas as pd


class Manipulator:
    def __init__(self, widget=None, render=True):
        logging.info("Initializing Manipulator")

        self.layers = {}
        self.canvas = vedo.Plotter(qt_widget=widget)
        self.render = render

    def add(self, file):
        file = Path(file)

        if file.exists():
            logging.info(f"Adding new layer ({file})")
        else:
            logging.error(f"File does not exists ({file})")
            return

        if file.suffix == ".csv":
            logging.debug(f"CSV file detected")

            data = pd.read_csv(file)
            self.layers[file.stem] = {
                "actor": vedo.Points(data[["x", "y", "z"]]),
                "raw": data,
            }
        else:
            logging.error(f"No valid layer ({file})")
            return

        self.canvas += self.layers[file.stem]["actor"]

        if self.render:
            self.show()

    def show(self):
        logging.info("Rendering new state")
        self.canvas.show()
