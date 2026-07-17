"""Interactive visualisation helpers built with Plotly."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def interactive_time_series(
    data: pd.DataFrame,
    *,
    date: str,
    value: str,
    group: str | None = None,
    title: str = "Time-series trend",
) -> go.Figure:
    """Build an interactive, zoomable time-series chart."""
    required = [date, value] + ([group] if group else [])
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    frame = data[required].copy()
    frame[date] = pd.to_datetime(frame[date], errors="raise")
    frame = frame.sort_values(date)
    figure = px.line(
        frame,
        x=date,
        y=value,
        color=group,
        markers=True,
        title=title,
        template="plotly_white",
    )
    figure.update_layout(hovermode="x unified", legend_title_text=group or "")
    return figure


def interactive_scatter(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    color: str | None = None,
    size: str | None = None,
    hover_name: str | None = None,
    title: str = "Relationship explorer",
) -> go.Figure:
    """Build an interactive scatter plot for multivariate exploration."""
    required = [column for column in [x, y, color, size, hover_name] if column]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if not pd.api.types.is_numeric_dtype(data[x]) or not pd.api.types.is_numeric_dtype(data[y]):
        raise TypeError("x and y must be numeric columns")

    return px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        hover_name=hover_name,
        title=title,
        template="plotly_white",
        opacity=0.75,
    )


def interactive_choropleth(
    data: pd.DataFrame,
    *,
    location: str,
    value: str,
    title: str = "Geospatial comparison",
    location_mode: str = "country names",
) -> go.Figure:
    """Build a country-level choropleth without requiring local shape files."""
    missing = [column for column in [location, value] if column not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if not pd.api.types.is_numeric_dtype(data[value]):
        raise TypeError("value must be numeric")

    return px.choropleth(
        data,
        locations=location,
        locationmode=location_mode,
        color=value,
        hover_name=location,
        title=title,
        template="plotly_white",
        color_continuous_scale="Viridis",
    )
