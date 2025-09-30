import pathlib
import anywidget
import traitlets


class ThreeWidget(anywidget.AnyWidget):
    """An anywidget for rendering interactive 3D scatter plots with three.js.

    Parameters
    ----------
    data : list of dict
        Chart data as list of points: [{"x": float, "y": float, "z": float, "color": str, "size": float}, ...]
        - x, y, z: 3D coordinates (required)
        - color: Any CSS color string (e.g., "red", "#ff0000", "rgb(255,0,0)")
        - size: Optional per-point size (default: 0.1)
    width : int, default=600
        Width of the chart in pixels
    height : int, default=400
        Height of the chart in pixels
    show_grid : bool, default=False
        Whether to show the grid helper
    show_axes : bool, default=False
        Whether to show the axes helper
    dark_mode : bool, default=False
        Whether to use dark mode (dark background with lighter grid/axes)

    Notes
    -----
    - Uses lightweight point rendering for excellent performance (handles 100k+ points smoothly)
    - Cell restart properly cleans up resources via cancelAnimationFrame and dispose()

    Examples
    --------
    >>> # Create a 3D scatter plot
    >>> data = [
    ...     {"x": 1.0, "y": 2.0, "z": 3.0, "color": "red"},
    ...     {"x": -1.0, "y": 1.0, "z": -2.0, "color": "#00ff00"},
    ... ]
    >>> widget = ThreeWidget(data=data)

    >>> # Per-point sizes determined by data
    >>> data_with_sizes = [
    ...     {"x": 0, "y": 0, "z": 0, "color": "red", "size": 0.5},
    ...     {"x": 1, "y": 1, "z": 1, "color": "blue", "size": 0.2},
    ... ]
    >>> widget = ThreeWidget(data=data_with_sizes)

    >>> # With dark mode and no grid
    >>> widget = ThreeWidget(data=data, dark_mode=True, show_grid=False, width=800, height=600)
    """

    _esm = pathlib.Path(__file__).parent / "static" / "widget.bundle.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    # Data for the 3D chart
    data = traitlets.List([]).tag(sync=True)
    width = traitlets.Int(600).tag(sync=True)
    height = traitlets.Int(400).tag(sync=True)
    show_grid = traitlets.Bool(False).tag(sync=True)
    show_axes = traitlets.Bool(False).tag(sync=True)
    dark_mode = traitlets.Bool(False).tag(sync=True)


__all__ = ["ThreeWidget"]
