#!/usr/bin/env python3

# 3rd party
import pytest

# 1st party
from src.manipulation import Manipulator


def test_initialization():
    m = Manipulator(render=False)
    m.add("tests/sample.csv")
