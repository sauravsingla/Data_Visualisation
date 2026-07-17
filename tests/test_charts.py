import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

from dataviz_reference import correlation_heatmap, ranked_bar_chart, time_series_chart


def test_time_series_chart_sorts_dates():
    data = pd.DataFrame({"date": ["2024-02-01", "2024-01-01"], "value": [2, 1]})
    ax = time_series_chart(data, date="date", value="value")
    x_values = list(ax.lines[0].get_xdata())
    assert x_values == sorted(x_values)


def test_ranked_bar_chart_limits_categories():
    data = pd.DataFrame({"category": ["a", "b", "c"], "value": [1, 3, 2]})
    ax = ranked_bar_chart(data, category="category", value="value", top_n=2)
    assert len(ax.patches) == 2


def test_missing_columns_raise_clear_error():
    with pytest.raises(ValueError, match="Missing required columns"):
        time_series_chart(pd.DataFrame({"x": [1]}), date="date", value="value")


def test_heatmap_requires_two_numeric_columns():
    with pytest.raises(ValueError, match="At least two numeric columns"):
        correlation_heatmap(pd.DataFrame({"category": ["a"], "value": [1]}))
