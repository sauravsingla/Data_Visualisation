# Python Data Visualization Guide

This guide maps common analytical questions to practical Python data visualization choices using Matplotlib, Seaborn, Plotly, Streamlit, and Datashader.

## Choosing the right chart

| Analytical task | Recommended chart | Typical Python tool |
|---|---|---|
| Show change over time | Line chart | Matplotlib or Plotly |
| Compare categories | Sorted horizontal bar chart | Matplotlib, Seaborn, or Plotly |
| Examine a distribution | Histogram, box plot, or density plot | Seaborn or Matplotlib |
| Study relationships | Scatter plot | Matplotlib or Plotly |
| Compare several numeric variables | Correlation heatmap | Seaborn |
| Compare countries or regions | Choropleth map | Plotly |
| Explore a dashboard interactively | Filtered charts and controls | Streamlit and Plotly |
| Render very large point datasets | Aggregated density image | Datashader |

## Time-series visualization

Use a line chart when the order of observations matters and the goal is to understand direction, seasonality, volatility, or change over time.

Good practice:

- sort observations chronologically;
- use a zero baseline only when it supports honest interpretation;
- avoid too many overlapping series;
- label units and time granularity;
- use interaction only when users need detailed inspection.

Repository examples:

- `time_series_chart`
- `interactive_time_series`
- `apps/streamlit_app.py`

## Ranked categorical comparison

Use sorted horizontal bars when users need to compare categories precisely. Horizontal labels are easier to read when category names are long.

Good practice:

- sort values intentionally;
- label values directly when practical;
- avoid unnecessary legends;
- limit the number of categories or group minor categories.

Repository example:

- `examples/gallery.py`

## Distribution analysis

Histograms and density plots help reveal skew, spread, clusters, and outliers. Box plots are useful for comparing distributions across groups.

Good practice:

- explain bin choices for histograms;
- avoid hiding sample size;
- compare groups using consistent scales;
- combine summary statistics with the chart when interpretation matters.

## Relationship and correlation analysis

Scatter plots show relationships between two numeric variables. Add grouping, size, or interaction only when each additional encoding answers a real question.

Correlation heatmaps provide a compact overview, but correlation should not be presented as causation.

Repository examples:

- `apps/streamlit_app.py`
- `examples/gallery.py`

## Interactive Plotly charts

Interactive charts are useful when users need tooltips, zooming, filtering, or selection. They should not replace a clear static chart when the question is simple.

Repository examples:

- `interactive_time_series`
- `examples/geospatial.py`
- `apps/streamlit_app.py`

## Streamlit dashboards

A Streamlit dashboard is appropriate when users need to explore several related views, change filters, or inspect subgroups without writing code.

A useful dashboard should:

- begin with the main analytical question;
- keep filters understandable;
- use consistent scales and terminology;
- avoid displaying every possible chart;
- make default views informative.

## Geospatial visualization

Use choropleth maps for region-level rates or normalized measures. Avoid mapping raw counts when regions have very different populations or exposure.

Repository example:

- `examples/geospatial.py`

## Large-data visualization with Datashader

Drawing every point can create overplotting and poor performance. Datashader aggregates large datasets into pixels, making density and structure visible even with one million or more observations.

Repository example:

- `examples/large_data.py`

## Accessibility checklist

- Use readable titles and labels.
- Do not rely on colour alone.
- Maintain sufficient contrast.
- Prefer direct labels where possible.
- Use honest axes and consistent units.
- Provide text explanations for important findings.
- Export charts at a suitable resolution.

## Reproducibility checklist

- Pin or constrain dependencies.
- Use deterministic sample data.
- Validate required columns and types.
- Return figure objects from reusable functions.
- Test chart-building logic.
- Run examples in CI.
- Record benchmark conditions.

## Related search topics

- Python data visualization examples
- Matplotlib chart examples
- Plotly interactive charts
- Streamlit dashboard tutorial
- Seaborn exploratory data analysis
- accessible data visualization
- geospatial visualization Python
- Datashader large dataset visualization
