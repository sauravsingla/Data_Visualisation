# Python Data Visualization and EDA Documentation

Use these guides to navigate the repository by analytical problem, dataset, chart type, or Python visualization library.

## Start here

- [Searchable notebook and example index](NOTEBOOK_INDEX.md) — maps common searches such as Iris EDA Python notebook, correlation heatmap example, Plotly scatter plot, Seaborn distributions, Streamlit dashboard, choropleth map, and Datashader visualization to runnable examples.
- [Applied UCI Iris EDA notebook](../notebooks/iris_eda_visualisation_articles.ipynb) — complete external-dataset demonstration covering data quality, descriptive statistics, distributions, relationships, correlations, accessible chart design, and visual storytelling.
- [Python Data Visualization Guide](python-data-visualization-guide.md) — chart selection, Matplotlib, Plotly, Streamlit, geospatial visualization, Datashader, accessibility, and reproducibility.
- [Published articles and code map](../ARTICLES.md) — connects Saurav Singla's public writing and presentation material to runnable repository examples.

## Find an example by analytical question

| Search or analytical question | Recommended resource |
|---|---|
| Iris dataset EDA in Python | [Applied UCI Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) |
| Exploratory data analysis Jupyter notebook | [Applied UCI Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) |
| Matplotlib and Seaborn visualization examples | [Static chart gallery](../examples/gallery.py) and [Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) |
| Plotly interactive scatter plot | [Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) |
| Annotated correlation heatmap | [Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) and [gallery](../examples/gallery.py) |
| Distribution plots and small multiples | [Iris notebook](../notebooks/iris_eda_visualisation_articles.ipynb) |
| Streamlit data visualization dashboard | [Streamlit application](../apps/streamlit_app.py) |
| Python choropleth map | [Geospatial example](../examples/geospatial.py) |
| Million-point visualization | [Datashader example](../examples/large_data.py) |
| Visualization rendering benchmark | [Rendering benchmark](../benchmarks/benchmark_rendering.py) |

## Runnable examples

- [`notebooks/iris_eda_visualisation_articles.ipynb`](../notebooks/iris_eda_visualisation_articles.ipynb) — public UCI Iris dataset EDA and article demonstration.
- [`examples/gallery.py`](../examples/gallery.py) — reproducible static chart gallery.
- [`examples/geospatial.py`](../examples/geospatial.py) — interactive country-level choropleth.
- [`examples/large_data.py`](../examples/large_data.py) — million-point rendering with Datashader.
- [`apps/streamlit_app.py`](../apps/streamlit_app.py) — interactive analytical dashboard.
- [`benchmarks/benchmark_rendering.py`](../benchmarks/benchmark_rendering.py) — chart construction benchmark.

## Reusable package

The reusable API is under [`src/dataviz_reference`](../src/dataviz_reference). It provides validated static and interactive visualization functions that accept pandas DataFrames and return figure objects.

## Search topics

- Python data visualization examples
- Iris dataset exploratory data analysis
- UCI Iris visualization notebook
- Matplotlib and Seaborn chart examples
- Plotly interactive scatter plot
- correlation heatmap in Python
- distribution plots and small multiples
- Streamlit dashboard example
- accessible data visualization
- geospatial choropleth maps
- large-data rendering with Datashader
- visual storytelling and EDA