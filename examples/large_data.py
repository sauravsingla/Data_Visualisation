"""Render one million points efficiently with Datashader."""

from pathlib import Path

import datashader as ds
import datashader.transfer_functions as tf
import numpy as np
import pandas as pd

OUTPUT = Path("artifacts")
OUTPUT.mkdir(exist_ok=True)

rng = np.random.default_rng(42)
rows = 1_000_000
data = pd.DataFrame(
    {
        "x": rng.normal(size=rows),
        "y": rng.normal(size=rows) * 0.6 + rng.normal(size=rows) * 0.4,
    }
)

canvas = ds.Canvas(plot_width=900, plot_height=550)
aggregate = canvas.points(data, "x", "y")
image = tf.shade(aggregate, how="eq_hist")
image.to_pil().save(OUTPUT / "million_points.png")
