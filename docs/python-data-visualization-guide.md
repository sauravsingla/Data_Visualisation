# Python Data Visualization and EDA Guide

This guide maps common analytical questions to practical Python data visualization choices using Matplotlib, Seaborn, Plotly, Streamlit, and Datashader. For a complete public-dataset walkthrough, use the [UCI Iris exploratory data analysis notebook](../notebooks/iris_eda_visualisation_articles.ipynb).

## Choosing the right chart

| Analytical task | Recommended chart | Typical Python tool | Repository example |
|---|---|---|---|
| Show change over time | Line chart | Matplotlib or Plotly | `time_series_chart`, `interactive_time_series` |
| Compare categories | Sorted horizontal bar chart | Matplotlib, Seaborn, or Plotly | Iris species-count chart and `examples/gallery.py` |
| Examine a distribution | Histogram, box plot, density plot, or small multiples | Seaborn or Matplotlib | Iris feature-distribution section |
| Study relationships | Scatter plot | Matplotlib or Plotly | Static and interactive Iris petal scatter plots |
| Compare several numeric variables | Correlation heatmap | Seaborn | Annotated Iris correlation heatmap |
| Compare countries or regions | Choropleth map | Plotly | `examples/geospatial.py` |
| Explore a dashboard interactively | Filtered charts and controls | Streamlit and Plotly | `apps/streamlit_app.py` |
| Render very large point datasets | Aggregated density image | Datashader | `examples/large_data.py` |

## Applied UCI Iris EDA notebook

The notebook [`notebooks/iris_eda_visualisation_articles.ipynb`](../notebooks/iris_eda_visualisation_articles.ipynb) is the repository's end-to-end example for searches such as:

- Iris dataset EDA in Python;
- UCI Iris visualization Jupyter notebook;
- exploratory data analysis with Matplotlib and Seaborn;
- Plotly interactive scatter plot example;
- annotated correlation heatmap in Python;
- distribution plots and small multiples;
- visual storytelling with a public dataset.

It validates data quality, compares species, studies distributions and relationships, creates static and interactive charts, and ends with a concise evidence-based narrative. See the [searchable notebook index](NOTEBOOK_INDEX.md) for a query-to-example map.

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

Repository examples:

- Iris species-count section in `notebooks/iris_eda_visualisation_articles.ipynb`
- `examples/gallery.py`

## Distribution analysis

Histograms and density plots help reveal skew, spread, clusters, and outliers. Box plots are useful for comparing distributions across groups. Small multiples are useful when several variables need the same visual grammar without overcrowding one chart.

Good practice:

- explain bin choices for histograms;
- avoid hiding sample size;
- compare groups using consistent scales;
- combine summary statistics with the chart when interpretation matters.

Repository examples:

- Iris grouped density and small-multiple section
- `examples/gallery.py`

## Relationship and correlation analysis

Scatter plots show relationships between two numeric variables. Add grouping, size, shape, or interaction only when each additional encoding answers a real question.

Correlation heatmaps provide a compact overview, but correlation should not be presented as causation.

Repository examples:

- static and interactive Iris petal scatter plots;
- annotated Iris Pearson correlation heatmap;
- `apps/streamlit_app.py`;
- `examples/gallery.py`.

## Interactive Plotly charts

Interactive charts are useful when users need tooltips, zooming, filtering, or selection. They should not replace a clear static chart when the question is simple.

Repository examples:

- interactive Iris scatter plot;
- `interactive_time_series`;
- `examples/geospatial.py`;
- `apps/streamlit_app.py`.

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
- Use deterministic or versioned public data.
- Validate required columns, types, missing values, and category labels.
- Return figure objects from reusable functions.
- Test chart-building logic.
- Execute notebooks and examples in CI.
- Record dataset provenance and benchmark conditions.

## Related search topics

- Python data visualization examples
- Python exploratory data analysis notebook
- Iris dataset EDA Python
- UCI Iris Jupyter notebook
- Matplotlib Iris dataset visualization
- Seaborn distribution plots
- Plotly interactive scatter plot
- annotated correlation heatmap Python
- small multiples visualization
- Streamlit dashboard tutorial
- accessible data visualization
- visual storytelling with data
- geospatial visualization Python
- Datashader large dataset visualization
