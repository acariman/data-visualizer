# Overview
Simple 3D data visualizer.


# Development environment
Run the following commands.
```
poetry config virtualenvs.in-project true  # optional
poetry self add poetry-bumpversion
poetry install --with dev
```

# Design
Generates python file from Designer using PyQt6 module.
```
poetry run pyuic6 src/ui/design.ui -o src/ui/_design.py
```
