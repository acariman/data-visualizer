#!/usr/bin/env python3

"""Top-level package for data visualizer"""

__author__ = """Alex Carimán"""
__email__ = "alex@cariman.cl"
__version__ = "1.1.1"


# Logger
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# For files
file_handler = logging.FileHandler("visualizer.log")
file_handler.setLevel(logging.INFO)

# For cmd
cmd_handler = logging.StreamHandler()
cmd_handler.setLevel(logging.DEBUG)

# Formats
fmt = logging.Formatter(
    fmt="%(asctime)s %(levelname)s\t%(module)s\t%(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
file_handler.setFormatter(fmt)
cmd_handler.setFormatter(fmt)

# Adds handlers
logger.addHandler(file_handler)
logger.addHandler(cmd_handler)
