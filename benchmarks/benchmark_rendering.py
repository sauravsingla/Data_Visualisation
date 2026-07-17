"""Compare static and interactive chart construction time.

Run with: python benchmarks/benchmark_rendering.py
"""

from __future__ import annotations

from statistics import mean
from time import perf_counter

import numpy as np
import pandas as pd

from dataviz_reference import time_series_chart
from dataviz_reference.interactive import interactive_time_series


def measure(callable_, repeats: int = 5) -> float:
    timings = []
    for _ in range(repeats):
        start = perf_counter()
        callable_()
        timings.append(perf_counter() - start)
    return mean(timings)


def main() -> None:
    rng = np.random.default_rng(42)
    data = pd.DataFrame(
        {
            "date": pd.date_range("2020-01-01", periods=10_000, freq="h"),
            "value": rng.normal(size=10_000).cumsum(),
        }
    )

    results = pd.DataFrame(
        [
            {
                "library": "Matplotlib",
                "rows": len(data),
                "mean_seconds": measure(
                    lambda: time_series_chart(data, date="date", value="value")
                ),
            },
            {
                "library": "Plotly",
                "rows": len(data),
                "mean_seconds": measure(
                    lambda: interactive_time_series(data, date="date", value="value")
                ),
            },
        ]
    )
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
