"""High-value chart patterns with validation and sensible defaults."""

from __future__ import annotations

from collections.abc import Sequence

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes


def _require_columns(data: pd.DataFrame, columns: Sequence[str]) -> None:
    missing = [column for column in columns if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("The input DataFrame must not be empty.")


def time_series_chart(
    data: pd.DataFrame,
    *,
    date: str,
    value: str,
    group: str | None = None,
    title: str | None = None,
    ax: Axes | None = None,
) -> Axes:
    """Plot one or more time series after sorting observations by date."""
    columns = [date, value] + ([group] if group else [])
    _require_columns(data, columns)
    frame = data.loc[:, columns].copy()
    frame[date] = pd.to_datetime(frame[date], errors="raise")
    frame = frame.sort_values(date)
    ax = ax or plt.subplots()[1]

    if group:
        for label, subset in frame.groupby(group, sort=True, observed=True):
            ax.plot(subset[date], subset[value], marker="o", markersize=3, label=str(label))
        ax.legend(title=group)
    else:
        ax.plot(frame[date], frame[value], marker="o", markersize=3)

    ax.set(title=title or value.replace("_", " ").title(), xlabel="", ylabel=value)
    ax.tick_params(axis="x", rotation=30)
    return ax


def ranked_bar_chart(
    data: pd.DataFrame,
    *,
    category: str,
    value: str,
    top_n: int | None = 10,
    title: str | None = None,
    ax: Axes | None = None,
) -> Axes:
    """Create a sorted horizontal bar chart with direct value labels."""
    _require_columns(data, [category, value])
    if top_n is not None and top_n < 1:
        raise ValueError("top_n must be at least 1 or None.")

    frame = data[[category, value]].dropna().sort_values(value, ascending=False)
    if top_n is not None:
        frame = frame.head(top_n)
    frame = frame.sort_values(value)
    ax = ax or plt.subplots()[1]
    bars = ax.barh(frame[category].astype(str), frame[value])
    ax.bar_label(bars, fmt="%.2f", padding=3)
    ax.set(title=title or f"{value.title()} by {category.title()}", xlabel=value, ylabel="")
    return ax


def distribution_plot(
    data: pd.DataFrame,
    *,
    value: str,
    group: str | None = None,
    title: str | None = None,
    ax: Axes | None = None,
) -> Axes:
    """Show distribution shape with histogram and density estimate."""
    columns = [value] + ([group] if group else [])
    _require_columns(data, columns)
    ax = ax or plt.subplots()[1]
    sns.histplot(data=data, x=value, hue=group, kde=True, element="step", ax=ax)
    ax.set_title(title or f"Distribution of {value.replace('_', ' ')}")
    return ax


def correlation_heatmap(
    data: pd.DataFrame,
    *,
    method: str = "pearson",
    title: str = "Correlation heatmap",
    ax: Axes | None = None,
) -> Axes:
    """Plot correlations for numeric columns with an annotated lower triangle."""
    if data.empty:
        raise ValueError("The input DataFrame must not be empty.")
    numeric = data.select_dtypes(include="number")
    if numeric.shape[1] < 2:
        raise ValueError("At least two numeric columns are required.")
    if method not in {"pearson", "spearman", "kendall"}:
        raise ValueError("method must be pearson, spearman, or kendall.")

    correlation = numeric.corr(method=method)
    mask = correlation.where(
        pd.DataFrame(
            [[row >= column for column in range(len(correlation))] for row in range(len(correlation))],
            index=correlation.index,
            columns=correlation.columns,
        )
    ).isna()
    ax = ax or plt.subplots(figsize=(9, 7))[1]
    sns.heatmap(
        correlation,
        mask=mask,
        annot=True,
        fmt=".2f",
        center=0,
        square=True,
        linewidths=0.5,
        cmap="vlag",
        ax=ax,
    )
    ax.set_title(title)
    return ax
