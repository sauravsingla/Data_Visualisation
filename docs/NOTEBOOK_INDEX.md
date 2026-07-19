# Searchable Notebook and EDA Index

Use this page to find the repository's Jupyter notebooks, external-dataset demonstrations, chart examples, and exploratory data analysis workflows by analytical question or search term.

## Featured external-dataset notebook

### UCI Iris exploratory data analysis and visualization

Notebook: [`notebooks/iris_eda_visualisation_articles.ipynb`](../notebooks/iris_eda_visualisation_articles.ipynb)

This reproducible Python notebook uses Fisher's UCI Iris dataset through scikit-learn and demonstrates the concepts from the repository's two published articles on data-visualization principles and exploratory data analysis.

It is relevant to searches such as:

- Iris dataset EDA in Python;
- UCI Iris visualization notebook;
- exploratory data analysis Jupyter notebook;
- Matplotlib Iris dataset examples;
- Seaborn distribution plots by species;
- Plotly interactive scatter plot example;
- Python correlation heatmap example;
- data visualization principles with code;
- external public dataset visualization;
- question-led EDA workflow.

## Find the right example by analytical question

| Search or analytical question | Recommended notebook section or repository example |
|---|---|
| How do I inspect missing values, duplicates and data types? | Iris notebook: data-quality inspection |
| How do I create a sorted horizontal bar chart with labels? | Iris notebook: species-count comparison |
| How do I compare distributions across groups? | Iris notebook: Seaborn small-multiple density plots |
| How do I visualize relationships between numeric variables? | Iris notebook: static petal scatter plot |
| How do I create an interactive Plotly scatter plot? | Iris notebook: interactive species comparison |
| How do I create an annotated correlation heatmap? | Iris notebook: Pearson-correlation heatmap |
| How do I turn EDA into a visual narrative? | Iris notebook: narrative conclusion and species profile |
| How do I create reusable Matplotlib and Plotly charts? | [`src/dataviz_reference/`](../src/dataviz_reference/) |
| How do I build a Streamlit analytics dashboard? | [`apps/streamlit_app.py`](../apps/streamlit_app.py) |
| How do I visualize one million points? | [`examples/large_data.py`](../examples/large_data.py) |
| How do I create a choropleth map in Python? | [`examples/geospatial.py`](../examples/geospatial.py) |
| How do I generate a static visualization gallery? | [`examples/gallery.py`](../examples/gallery.py) |

## Methods demonstrated in the Iris notebook

- pandas DataFrame inspection and descriptive statistics;
- missing-value and duplicate checks;
- category counts and balanced-class validation;
- Matplotlib horizontal bar charts;
- Seaborn grouped density plots and small multiples;
- static scatter plots with colour and shape encoding;
- Plotly interactive scatter plots with hover information;
- Pearson correlation matrices;
- annotated correlation heatmaps;
- accessible labels, units, titles and restrained chart decoration;
- reproducible PNG and HTML artifact generation.

## Run the notebook

```bash
pip install -e ".[notebook]"
jupyter lab notebooks/iris_eda_visualisation_articles.ipynb
```

For a complete development installation:

```bash
pip install -e ".[all,dev]"
```

The notebook writes generated PNG charts and the interactive Plotly HTML visualization to `artifacts/`.

## Related reading

- [`ARTICLES.md`](../ARTICLES.md) maps the two published articles to concrete notebook sections and repository implementations.
- [`python-data-visualization-guide.md`](python-data-visualization-guide.md) provides broader guidance on selecting and designing charts.
- [`README.md`](../README.md) is the main repository entry point.
