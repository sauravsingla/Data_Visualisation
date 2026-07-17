"""Generate a small gallery from built-in, deterministic sample data."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from dataviz_reference import (
    apply_accessible_theme,
    correlation_heatmap,
    distribution_plot,
    ranked_bar_chart,
    time_series_chart,
)

OUTPUT = Path("artifacts")


def main() -> None:
    apply_accessible_theme()
    OUTPUT.mkdir(exist_ok=True)
    rng = np.random.default_rng(42)

    dates = pd.date_range("2025-01-01", periods=12, freq="MS")
    trends = pd.DataFrame(
        {
            "date": list(dates) * 2,
            "value": np.r_[rng.normal(100, 8, 12).cumsum(), rng.normal(80, 6, 12).cumsum()],
            "segment": ["Traditional"] * 12 + ["Modern"] * 12,
        }
    )
    time_series_chart(trends, date="date", value="value", group="segment", title="Monthly trend")
    plt.savefig(OUTPUT / "time_series.png")
    plt.close()

    categories = pd.DataFrame(
        {"category": [f"Category {i}" for i in range(1, 13)], "value": rng.uniform(10, 100, 12)}
    )
    ranked_bar_chart(categories, category="category", value="value", top_n=8)
    plt.savefig(OUTPUT / "ranked_bar.png")
    plt.close()

    samples = pd.DataFrame(
        {"score": np.r_[rng.normal(60, 10, 250), rng.normal(72, 8, 250)], "group": ["A"] * 250 + ["B"] * 250}
    )
    distribution_plot(samples, value="score", group="group")
    plt.savefig(OUTPUT / "distribution.png")
    plt.close()

    metrics = pd.DataFrame(rng.normal(size=(200, 5)), columns=list("ABCDE"))
    metrics["E"] = metrics["A"] * 0.7 + rng.normal(scale=0.3, size=200)
    correlation_heatmap(metrics)
    plt.savefig(OUTPUT / "correlation.png")
    plt.close()


if __name__ == "__main__":
    main()
