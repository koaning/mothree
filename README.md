# MoThree

A lightweight 3D visualization widget for Jupyter notebooks and Marimo, powered by Three.js.

## Installation

```bash
uv pip install mothree
```

## Usage

```python
from mothree import ThreeWidget

# Create some 3D data
data = [
    {"x": random.random(), "y": 2.0, "z": random.random(), "color": "red"}
    for i in range(2_000)
]

# Create the widget
widget = ThreeWidget(data=data, dark_mode=True, show_grid=True)
widget
```
