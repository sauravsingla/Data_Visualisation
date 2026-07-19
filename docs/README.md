# Data Visualization Documentation

Use these guides to navigate the repository by analytical problem rather than by library.

## Guides

- [Python Data Visualization Guide](python-data-visualization-guide.md) — chart selection, Matplotlib, Plotly, Streamlit, geospatial visualization, Datashader, accessibility, and reproducibility.
- [Published articles and code map](../ARTICLES.md) — connects Saurav Singla's public writing and presentation material to runnable repository examples.

## Runnable examples

- [`examples/gallery.py`](../examples/gallery.py) — reproducible static chart gallery.
- [`examples/geospatial.py`](../examples/geospatial.py) — interactive country-level choropleth.
- [`examples/large_data.py`](../examples/large_data.py) — million-point rendering with Datashader.
- [`apps/streamlit_app.py`](../apps/streamlit_app.py) — interactive analytical dashboard.
- [`benchmarks/benchmark_rendering.py`](../benchmarks/benchmark_rendering.py) — chart construction benchmark.

## Reusable package

The reusable API is under [`src/dataviz_reference`](../src/dataviz_reference). It provides validated static and interactive visualization functions that accept pandas DataFrames and return figure objects.

## Common topics

- Python data visualization examples
- Matplotlib and Seaborn charts
- Plotly interactive visualization
- Streamlit dashboards
- exploratory data analysis
- accessible visualization
- geospatial choropleth maps
- large-data rendering with Datashader
