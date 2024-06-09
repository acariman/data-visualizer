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
        self.should_render = render

    def add(self, file):
        file = Path(file)

        if file.exists():
            logging.info(f"Adding new layer ({file})")
        else:
            logging.error(f"File does not exists ({file})")
            return

        layer = file.stem

        if file.suffix == ".csv":
            logging.debug(f"CSV file detected")

            data = pd.read_csv(file)
            self.layers[layer] = {
                "actor": vedo.Points(data[["x", "y", "z"]]),
                "raw": data,
                "state": True,
                "nice-name": file.name,
                "name": layer,
            }
        else:
            logging.error(f"No valid layer ({file})")
            return

        return self.layers[layer]

    def show(self, layer):
        self.canvas.add(self.layers[layer]["actor"])

        if self.should_render:
            self.render()

    def hide(self, layer):
        self.canvas.remove(self.layers[layer]["actor"])

        if self.should_render:
            self.render()

    def render(self):
        logging.info("Rendering new state")
        self.canvas.show()
