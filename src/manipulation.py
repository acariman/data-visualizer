#!/usr/bin/env python3

# Core
import logging

# 3rd party
import vedo
import pandas as pd


class Manipulator:
    def __init__(self, widget=None, render=True):
        logging.info("Initializing Manipulator")

        self.layers = {}
        self.canvas = vedo.Plotter(qt_widget=widget)
        self.should_render = render

    def add_csv(self, file, params=None):
        logging.debug(f"Adding CSV file")
        layer = file.stem

        if layer in self.layers:
            logging.warning(f"Layer already added ({layer})")
            return

        data = pd.read_csv(file)

        if all(
            [
                params["x"] in data,
                params["y"] in data,
                params["z"] in data,
            ]
        ):
            logging.debug(f"Adding layer based on params ({params})")
            self.layers[layer] = {
                "actor": vedo.Points(
                    data[
                        [
                            params["x"],
                            params["y"],
                            params["z"],
                        ]
                    ],
                    c=params["color"],
                ),
                "raw": data,
                "state": True,
                "nice-name": file.name,
                "name": layer,
                "params": params,
            }
        else:
            logging.error(f"Invalid column selected ({params})")
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
        self.canvas.show(resetcam=len(self.layers) <= 1)
