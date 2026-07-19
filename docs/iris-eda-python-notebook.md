# Iris Dataset EDA in Python: Jupyter Notebook with Matplotlib, Seaborn and Plotly

This page is the searchable landing page for the repository's applied **UCI Iris dataset exploratory data analysis notebook**.

Open the runnable notebook: [`notebooks/iris_eda_visualisation_articles.ipynb`](../notebooks/iris_eda_visualisation_articles.ipynb)

## What the notebook demonstrates

The notebook provides a complete Iris dataset EDA workflow in Python using pandas, Matplotlib, Seaborn, Plotly and scikit-learn. It covers:

- loading Fisher's Iris dataset from scikit-learn;
- checking rows, columns, data types, missing values and duplicate records;
- producing descriptive statistics by species;
- comparing Iris species with a sorted horizontal bar chart;
- visualizing sepal and petal distributions with Seaborn density plots and small multiples;
- studying petal length and petal width with a grouped scatter plot;
- creating an annotated Pearson correlation heatmap;
- building an interactive Plotly scatter plot with hover details;
- converting exploratory findings into a concise visual story;
- exporting reproducible PNG and HTML artifacts.

## Common searches answered by this example

This repository example is relevant to searches such as:

- Iris dataset EDA Python notebook
- UCI Iris exploratory data analysis
- Jupyter notebook for Iris dataset visualization
- Matplotlib Iris dataset example
- Seaborn Iris distribution plot
- Plotly Iris interactive scatter plot
- Python correlation heatmap example
- petal length and petal width scatter plot
- small multiples visualization in Python
- external dataset visualization project
- beginner EDA project with Python
- visual storytelling with exploratory data analysis

## Charts included

### Species count comparison

A sorted horizontal bar chart shows that the Iris dataset contains balanced observations across the three species. The axis starts at zero because bar length directly encodes magnitude.

### Feature distribution analysis

Seaborn density plots compare sepal length, sepal width, petal length and petal width by species. Small multiples reduce visual clutter and make it easier to compare distribution shape.

### Relationship analysis

A scatter plot of petal length versus petal width shows clear separation among setosa, versicolor and virginica. Colour and marker shape both encode species so the chart does not rely on colour alone.

### Correlation heatmap

An annotated heatmap summarizes Pearson correlations among the four numeric Iris measurements. The notebook explicitly notes that correlation does not establish causation.

### Interactive Plotly visualization

The Plotly scatter plot adds hover details for sepal measurements while preserving the same analytical message as the static chart.

## Run the notebook

```bash
git clone https://github.com/sauravsingla/Data_Visualisation.git
cd Data_Visualisation
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[notebook]"
jupyter lab notebooks/iris_eda_visualisation_articles.ipynb
```

The notebook writes generated files to `artifacts/`.

## Related repository resources

- [Searchable notebook index](NOTEBOOK_INDEX.md)
- [Python data visualization guide](python-data-visualization-guide.md)
- [Published articles and repository map](../ARTICLES.md)
- [Main repository README](../README.md)
- [Static chart gallery](../examples/gallery.py)
- [Interactive Streamlit dashboard](../apps/streamlit_app.py)

## Dataset provenance

The example uses Fisher's Iris dataset, originally published through the UCI Machine Learning Repository and distributed through scikit-learn. Loading it through scikit-learn avoids a fragile live download and supports reproducible execution.

## Search keywords

Iris dataset, UCI Iris, exploratory data analysis, EDA, Python, Jupyter notebook, pandas, Matplotlib, Seaborn, Plotly, correlation heatmap, scatter plot, density plot, small multiples, interactive visualization, data visualization, data visualisation, visual storytelling, scikit-learn.
