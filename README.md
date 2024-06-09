# Overview
Simple 3D visualization of points by dragging files into the UI.


# Installation
Run the following commands.
```
poetry config virtualenvs.in-project true  # optional
poetry install
```


# To do
- Enable more file types.
- Add pop-up for CSV files with different separators and columns.
- Show information when hovering a point.
- Generates a executable.


# Development environment
Run the following commands.
```
poetry self add poetry-bumpversion
poetry install --with dev
```

# Design environment
Generates python file from Designer using PyQt6 module.
```
poetry run pyuic6 src/ui/design.ui -o src/ui/_design.py
```
