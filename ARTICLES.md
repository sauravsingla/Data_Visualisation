# Published Articles and Repository Guide

This repository is the practical companion to two public articles by **Saurav Singla** in the *Towards Data Science* archive on Medium.

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
| Choose a chart based on the question | Reusable chart functions under `src/dataviz_reference/` |
| Reduce noise | Accessible theme and direct-labelling conventions |
| Use meaningful titles and honest scales | Static chart APIs and gallery examples |
| Refine visual encoding | Ranking, distribution, correlation, and time-series examples |
| Build a narrative | Streamlit dashboard and interactive Plotly workflows |
| Avoid overplotting | Datashader million-point aggregation example |

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
| Inspect distributions | Histogram and grouped-density examples |
| Compare categories | Sorted horizontal ranking charts |
| Study relationships | Scatter and multivariate interactive scatter plots |
| Examine correlations | Annotated correlation heatmaps |
| Understand trends | Static and interactive time-series charts |
| Explore segments | Streamlit filtering and segmented views |
| Validate inputs | Column and data-type validation in reusable APIs |
| Scale exploration | Geospatial and million-point examples |

## Recommended learning path

1. Read the data-visualisation principles article.
2. Run `python examples/gallery.py`.
3. Read the EDA article.
4. Open `Data_Visualisation_Charts.ipynb`.
5. Run `streamlit run apps/streamlit_app.py`.
6. Try the geospatial and million-point examples.
7. Adapt the reusable APIs to a governed dataset of your own.

## Suggested citation

When referring to the written material, cite the relevant Medium article and include its URL and publication date. When reusing the software, link to this GitHub repository and identify the release or commit used so that results remain reproducible.
