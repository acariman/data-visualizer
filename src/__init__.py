#!/usr/bin/env python3

"""Top-level package for data visualizer"""

# Core
import logging

__author__ = """Alex Carimán"""
__email__ = "alex@cariman.cl"
__version__ = "0.1.0"


logging.basicConfig(
    filename='visualizer.log',
    level=logging.INFO,  # TODO: enable changing level from cli or settings
    format='%(asctime)s %(levelname)s\t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)
