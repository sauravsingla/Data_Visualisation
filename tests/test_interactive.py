import pandas as pd
import pytest

from dataviz_reference.interactive import (
    interactive_choropleth,
    interactive_scatter,
    interactive_time_series,
)


def test_interactive_time_series_returns_figure() -> None:
    data = pd.DataFrame({"date": ["2026-02-01", "2026-01-01"], "value": [2, 1]})
    figure = interactive_time_series(data, date="date", value="value")
    assert len(figure.data) == 1
    assert list(figure.data[0].x) == list(pd.to_datetime(["2026-01-01", "2026-02-01"]))


def test_interactive_scatter_rejects_non_numeric_axes() -> None:
    data = pd.DataFrame({"x": ["a", "b"], "y": [1, 2]})
    with pytest.raises(TypeError, match="numeric"):
        interactive_scatter(data, x="x", y="y")


def test_choropleth_validates_required_columns() -> None:
    data = pd.DataFrame({"country": ["India"]})
    with pytest.raises(ValueError, match="Missing columns"):
        interactive_choropleth(data, location="country", value="score")
