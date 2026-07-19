# Published Articles and Repository Guide

This repository is the practical companion to two public articles by **Saurav Singla** in the *Towards Data Science* archive on Medium.

## Applied external-dataset notebook

The notebook [`notebooks/iris_eda_visualisation_articles.ipynb`](notebooks/iris_eda_visualisation_articles.ipynb) combines the ideas from both articles using Fisher's public **UCI Iris dataset**, loaded through scikit-learn without a fragile network download.

For query-based navigation, use the [`searchable notebook and EDA index`](docs/NOTEBOOK_INDEX.md). It maps common searches such as *Iris EDA Python notebook*, *Plotly scatter example*, *correlation heatmap*, *small-multiple distribution plots*, and *external public dataset visualization* to the relevant notebook section or repository example.

It demonstrates:

- data-quality inspection before charting;
- chart selection based on the analytical question;
- sorted and directly labelled category comparisons;
- grouped distribution analysis using small multiples;
- relationship analysis with static and interactive scatter plots;
- an annotated correlation heatmap;
- honest scales, units, reduced visual noise, and narrative titles;
- movement from exploratory findings to a concise visual conclusion.

Run it after installing the complete dependency group:

```bash
pip install -e ".[all,dev]"
jupyter lab notebooks/iris_eda_visualisation_articles.ipynb
```

Generated PNG and HTML outputs are written to `artifacts/`.

## 1. What are the important principles of data visualization?

- Published: 19 October 2020
- Reading time: approximately 7 minutes
- Article: https://medium.com/data-science/what-are-the-important-principles-of-data-visualization-3d3ca6c8c303

### Main ideas

- Translate raw data into visual forms that expose patterns and trends.
- Select visual encodings that match the analytical question.
- Reduce visual noise and unnecessary decoration.
- Refine chart structure, labels, scales, and annotations.
- Use narrative visualisation to communicate an interpretable message.

### Where these ideas appear in the repository

| Principle | Repository implementation |
|---|---|
| Choose a chart based on the question | Reusable chart functions under `src/dataviz_reference/` and the Iris analytical-question sequence |
| Reduce noise | Accessible theme, simplified spines, restrained grids, and direct-labelling conventions |
| Use meaningful titles and honest scales | Static chart APIs, gallery examples, and the zero-based Iris category chart |
| Refine visual encoding | Ranking, distribution, correlation, time-series, and small-multiple examples |
| Build a narrative | Iris notebook conclusion, Streamlit dashboard, and interactive Plotly workflows |
| Avoid overplotting | Transparency in the Iris scatter and Datashader million-point aggregation example |

## 2. Exploratory Data Analysis is a significant part of Data Science

- Published: 5 August 2020
- Reading time: approximately 5 minutes
- Article: https://medium.com/data-science/exploratory-data-analysis-is-a-significant-part-of-data-science-7f3b173c04d2

### Main ideas

- Build a relationship with the dataset before modelling.
- Examine distributions, missing values, outliers, and relationships.
- Use visual analysis to generate and test hypotheses.
- Treat EDA as an iterative process rather than a one-time step.
- Communicate findings in a form that supports later modelling and decisions.

### Where these ideas appear in the repository

| EDA task | Repository implementation |
|---|---|
| Inspect structure and quality | Iris notebook data types, missing values, duplicates, uniqueness, and descriptive statistics |
| Inspect distributions | Iris small-multiple density plots and gallery histogram examples |
| Compare categories | Sorted, directly labelled Iris species-count chart |
| Study relationships | Static and interactive Iris petal scatter plots plus Streamlit multivariate scatter |
| Examine correlations | Annotated Iris correlation heatmap and gallery correlation example |
| Understand trends | Static and interactive time-series charts |
| Explore segments | Species grouping in the Iris notebook and Streamlit filtering |
| Validate inputs | Column and data-type validation in reusable APIs |
| Scale exploration | Geospatial and million-point examples |

## Recommended learning path

1. Read the data-visualisation principles article.
2. Open the [searchable notebook and EDA index](docs/NOTEBOOK_INDEX.md).
3. Run `notebooks/iris_eda_visualisation_articles.ipynb`.
4. Read the EDA article and revisit the notebook's data-quality and hypothesis sections.
5. Run `python examples/gallery.py`.
6. Open `Data_Visualisation_Charts.ipynb` for the original chart collection.
7. Run `streamlit run apps/streamlit_app.py`.
8. Try the geospatial and million-point examples.
9. Adapt the reusable APIs to a governed dataset of your own.

## Search topics covered

- Python exploratory data analysis notebook;
- UCI Iris dataset visualization;
- Matplotlib and Seaborn Iris examples;
- Plotly interactive scatter plot;
- annotated correlation heatmap;
- grouped distribution and density plots;
- small-multiple visualizations;
- accessible data visualization principles;
- visual storytelling with EDA;
- external public dataset analysis.

## Dataset provenance

The applied notebook uses Fisher's Iris dataset, originally published through the UCI Machine Learning Repository and distributed in scikit-learn. The notebook records its provenance and does not require a live external download.

## Suggested citation

When referring to the written material, cite the relevant Medium article and include its URL and publication date. When reusing the software or notebook, link to this GitHub repository and identify the release or commit used so that results remain reproducible.
