import marimo

__generated_with = "0.16.3"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""# MoThree - 3D Chart Widget with Three.js""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""This library gives a simple wrapper around three.js to make 3d charts. It's also pretty performant! """)
    return


@app.cell
def _(ThreeWidget, mo, random):
    scatter_data = [
        {
            "x": random.uniform(-3, 3),
            "y": random.uniform(-3, 3),
            "z": random.uniform(-3, 3),
            "color": random.choice(["red", "green", "blue", "yellow", "magenta"]),
        }
        for _ in range(5_000)
    ]

    scatter_widget = mo.ui.anywidget(ThreeWidget(data=scatter_data, dark_mode=True))
    scatter_widget
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## 3D Grid Visualization\nCreate a grid of points in 3D space.""")
    return


@app.cell
def _(ThreeWidget, random):
    # Generate grid data with positioned points
    grid_data = []
    for _i in range(5):
        for _j in range(5):
            grid_data.append(
                {
                    "x": _i - 2,
                    "y": random.uniform(0.5, 3),
                    "z": _j - 2,
                    "color": "steelblue" if (_i + _j) % 2 == 0 else "coral",
                }
            )

    grid_widget = ThreeWidget(data=grid_data, width=800, height=500, show_grid=True)
    grid_widget
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Mathematical Function Visualization\nVisualize a mathematical function in 3D.""")
    return


@app.cell
def _(ThreeWidget, math):
    # Create a wave pattern
    wave_data = []
    for i in range(-100, 110, 1):
        for j in range(-100, 110, 1):
            x = i * 0.1
            z = j * 0.1
            y = math.sin(math.sqrt(x**2 + z**2)) * 2

            # Color based on height
            if y > 0:
                color = "red"
            else:
                color = "blue"

            wave_data.append({"x": x, "y": y, "z": z, "color": color})

    wave_widget = ThreeWidget(data=wave_data, width=700, height=600)
    wave_widget
    return


@app.cell
def _():
    from mothree import ThreeWidget
    import random
    import math
    return ThreeWidget, math, random


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
