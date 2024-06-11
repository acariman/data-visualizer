#!/usr/bin/env python3

# Core
import logging

# 3rd party
import vedo
import pandas as pd


class Manipulator:
    def __init__(self, widget=None, render=True, parallel_proj=True):
        logging.info("Initializing Manipulator")

        self.layers = {}
        self.canvas = vedo.Plotter(qt_widget=widget)
        self.cam = self.canvas.camera
        self.cam.SetParallelProjection(parallel_proj)

        self.should_render = render

    def add_csv(self, file, params=None):
        logging.debug(f"Adding CSV file")
        layer = file.name

        if layer in self.layers:
            logging.warning(f"Layer already added ({layer})")
            return

        data = pd.read_csv(file, sep=params["separator"])

        if all(
            [
                params["x"] in data,
                params["y"] in data,
                params["z"] in data,
                len(data.columns) > 1,
            ]
        ):
            logging.debug(f"Adding layer based on params ({params})")
            data[["x", "y", "z"]] = data[[params["x"], params["y"], params["z"]]]
            self.layers[layer] = {
                "actor": vedo.Points(data[["x", "y", "z"]], c=params["color"]),
                "raw": data,
                "state": True,
                "nice-name": file.stem,
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

    def get_info(self, evt):
        obj = evt.object
        if not obj:
            return

        for layer in self.layers.values():
            if layer["actor"] is obj:
                picked = evt.picked3d
                point = obj.closest_point(picked, return_point_id=True)

                data = layer["raw"].iloc[point].to_dict()
                data["layer"] = layer["nice-name"]

                return data

        return
