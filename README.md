# Python Data Visualization Reference: Matplotlib, Plotly, Streamlit and Datashader

[![CI](https://github.com/sauravsingla/Data_Visualisation/actions/workflows/ci.yml/badge.svg)](https://github.com/sauravsingla/Data_Visualisation/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CITATION.cff](https://img.shields.io/badge/citation-CFF-blue.svg)](CITATION.cff)

A production-minded Python data visualization repository with reusable Matplotlib and Plotly APIs, Streamlit dashboards, geospatial choropleths, accessible themes, exploratory data analysis examples, million-point Datashader rendering, benchmarks, tests, and CI.

Use this project when searching for practical **Python data visualization examples**, **Matplotlib chart patterns**, **Plotly interactive visualizations**, **Streamlit dashboard examples**, **EDA visualizations**, **geospatial charts**, or **large-data visualization in Python**.

## Generated chart gallery

![Generated Python data visualization gallery showing a time series, ranked bar chart, grouped distribution and correlation heatmap](docs/assets/gallery-preview.svg)

The preview is generated from the same deterministic sample design used by [`examples/gallery.py`](examples/gallery.py). Run the gallery locally to regenerate the individual high-resolution outputs in `artifacts/`.

## Applied notebook using a public external dataset

[`notebooks/iris_eda_visualisation_articles.ipynb`](notebooks/iris_eda_visualisation_articles.ipynb) converts the repository's two published articles into a complete executable demonstration using Fisher's public **UCI Iris dataset**.

The notebook loads the dataset through scikit-learn without a fragile live download and demonstrates:

- data-quality inspection, missing values, duplicates, and descriptive statistics;
- chart selection based on the analytical question;
- sorted and directly labelled category comparisons;
- grouped feature distributions using small multiples;
- static and interactive relationship analysis;
- an annotated correlation heatmap;
- honest scales, units, reduced chart noise, and narrative titles;
- movement from EDA findings to a concise visual conclusion.

Run it with:

```bash
pip install -e ".[all,dev]"
jupyter lab notebooks/iris_eda_visualisation_articles.ipynb
```

The notebook writes reproducible PNG and interactive HTML outputs to `artifacts/`. See [`ARTICLES.md`](ARTICLES.md) for the detailed article-to-notebook mapping and dataset provenance.

## Explore by analytical problem

| Analytical question | Recommended approach | Repository example |
|---|---|---|
| How is a metric changing over time? | Matplotlib or Plotly time series | `time_series_chart`, `interactive_time_series` |
| Which categories rank highest? | Sorted horizontal bar chart | `examples/gallery.py` and the Iris notebook |
| How are variables related? | Scatter plot with optional grouping | Iris notebook and `apps/streamlit_app.py` |
| What does the distribution look like? | Histogram, density comparison, or small multiples | Iris notebook and `examples/gallery.py` |
| Which variables move together? | Annotated correlation heatmap | Iris notebook and `examples/gallery.py` |
| Which charts best explain one real dataset? | Question-led EDA narrative | `notebooks/iris_eda_visualisation_articles.ipynb` |
| How do countries compare? | Interactive choropleth map | `examples/geospatial.py` |
| How can one million points be rendered clearly? | Datashader aggregation | `examples/large_data.py` |
| How can analysis be shared with users? | Streamlit dashboard or standalone HTML | `apps/streamlit_app.py` |
| How can chart performance be measured? | Reproducible rendering benchmark | `benchmarks/benchmark_rendering.py` |

## What this repository includes

- Reusable static chart APIs built with Matplotlib and Seaborn
- Interactive Plotly charts with filtering, hover, zoom, and responsive layouts
- An applied UCI Iris dataset notebook connecting published visualization and EDA principles to code
- Streamlit analytical dashboard patterns
- Country-level geospatial choropleth visualization
- Million-point visualization with Datashader
- Exploratory data analysis and statistical graphics examples
- Accessible themes, direct labels, honest scales, and readable chart defaults
- Reproducible chart galleries and rendering benchmarks
- Input validation, automated tests, branch coverage, linting, and GitHub Actions CI

## Quick start

```bash
git clone https://github.com/sauravsingla/Data_Visualisation.git
cd Data_Visualisation
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[all,dev]"
ruff check .
pytest --cov=dataviz_reference
python examples/gallery.py
```

Generated outputs are written to `artifacts/`.

## Static analytical API

```python
import pandas as pd
from dataviz_reference import apply_accessible_theme, time_series_chart

apply_accessible_theme()
data = pd.DataFrame(
    {
        "date": ["2026-01-01", "2026-02-01", "2026-03-01"],
        "transactions": [120, 148, 171],
    }
)
axis = time_series_chart(
    data,
    date="date",
    value="transactions",
    title="Monthly transactions",
)
axis.figure.savefig("artifacts/monthly_transactions.png", bbox_inches="tight")
```

## Interactive Plotly API

```python
from dataviz_reference import interactive_time_series

figure = interactive_time_series(
    data,
    date="date",
    value="transactions",
    title="Monthly transactions",
)
figure.write_html("artifacts/monthly_transactions.html")
```

## Run the Streamlit dashboard

```bash
streamlit run apps/streamlit_app.py
```

The dashboard demonstrates filtering, segmented time series, multivariate scatter plots, tooltips, zooming, and responsive layout.

## Run specialised examples

```bash
python examples/geospatial.py
python examples/large_data.py
python benchmarks/benchmark_rendering.py
```

The geospatial example produces a standalone HTML choropleth. The large-data example aggregates one million points into a readable density image. The benchmark compares average chart-construction time on the same 10,000-row dataset.

## Traditional and modern coverage

| Problem | Traditional foundation | Modern solution |
|---|---|---|
| Trends | Matplotlib lines | Validated Plotly time series with unified hover |
| Ranking | Vertical bars | Sorted horizontal bars with direct labels |
| Distribution | Histograms | Grouped density comparison and small multiples |
| Relationships | Scatter plots | Multivariate interactive scatter |
| Correlation | Manual matrices | Annotated correlation heatmap |
| Applied EDA | Isolated charts | Question-led Iris dataset notebook with a narrative conclusion |
| Geography | Static maps | Browser-based choropleth |
| Large data | Overplotted points | Datashader aggregation for one million rows |
| Delivery | Notebook output | Streamlit dashboard and standalone HTML |
| Reliability | Manual checking | Ruff, pytest, branch coverage, and CI |
| Performance | Assumptions | Reproducible rendering benchmark |

## Design principles

1. Start with the analytical question, not the chart type.
2. Prefer direct labels, meaningful titles, honest scales, and accessible colours.
3. Validate columns and data types before rendering.
4. Return figure objects so callers control display and export.
5. Keep examples deterministic and reproducible.
6. Use interactive charts only when interaction improves understanding.
7. Aggregate large datasets instead of drawing every mark blindly.
8. Separate reusable plotting logic from notebooks and applications.

## Repository structure

```text
.
├── Data_Visualisation_Charts.ipynb   # Original traditional-chart notebook
├── notebooks/
│   └── iris_eda_visualisation_articles.ipynb # Applied UCI Iris EDA article demo
├── ARTICLES.md                       # Published articles and code mapping
├── CITATION.cff                      # Machine-readable citation metadata
├── apps/streamlit_app.py             # Interactive analytical dashboard
├── benchmarks/benchmark_rendering.py # Matplotlib and Plotly benchmark
├── docs/                             # Searchable guides and generated preview assets
├── examples/gallery.py               # Static reproducible gallery
├── examples/geospatial.py            # Interactive choropleth example
├── examples/large_data.py            # Million-point Datashader example
├── src/dataviz_reference/            # Reusable static and interactive API
├── tests/                             # Unit and validation tests
├── .github/workflows/ci.yml          # Lint, tests, coverage, gallery execution
├── CONTRIBUTING.md                   # Contribution quality standards
└── pyproject.toml                    # Packaging and dependency groups
```

## Publications and presentations

This repository complements public articles and presentation material by **Saurav Singla**.

### Published articles

1. [What are the important principles of data visualization?](https://medium.com/data-science/what-are-the-important-principles-of-data-visualization-3d3ca6c8c303) — visual encoding, refinement, clarity, and narrative visualisation.
2. [Exploratory Data Analysis is a significant part of Data Science](https://medium.com/data-science/exploratory-data-analysis-is-a-significant-part-of-data-science-7f3b173c04d2) — practical EDA, understanding distributions, relationships, patterns, and data quality before modelling.

The applied [UCI Iris notebook](notebooks/iris_eda_visualisation_articles.ipynb) demonstrates both articles together on one real public dataset.

### Presentation

- [Data visualization — Road Accidents in United Kingdom](https://share.google/stvTDaRe4NFjtxVFs) — an applied data-visualisation study using UK road-accident data to identify trends and relationships across accident, road, vehicle, driver, time, and severity attributes.

See [ARTICLES.md](ARTICLES.md) for the detailed article-to-code map.

## Quality checks

```bash
ruff check .
pytest --cov=dataviz_reference --cov-report=term-missing
python examples/gallery.py
python examples/geospatial.py
python benchmarks/benchmark_rendering.py
```

Coverage is configured with branch measurement and an 85% minimum. GitHub Actions validates supported Python versions and executes the reproducible gallery.

## Open-source data policy

Examples use deterministic synthetic data by default, avoiding unstable downloads and licensing surprises. The applied article notebook uses Fisher's public Iris dataset, distributed through scikit-learn and originally published through the UCI Machine Learning Repository. The APIs also accept ordinary pandas DataFrames, so users can apply them to open datasets from World Bank Open Data, Our World in Data, data.gov.in, Kaggle, UCI Machine Learning Repository, or governed internal data sources. Always retain the original dataset licence and citation.

## Search terms and use cases

This project is relevant to:

- Python data visualization examples
- Matplotlib and Seaborn chart examples
- Plotly interactive chart examples
- Streamlit dashboard examples
- exploratory data analysis visualizations
- UCI Iris dataset EDA notebook
- external dataset visualization in Python
- statistical graphics in Python
- geospatial data visualization and choropleth maps
- large dataset visualization with Datashader
- accessible data visualization
- reusable chart APIs for analytics and data science

## Citation

Use GitHub's **Cite this repository** control, powered by [`CITATION.cff`](CITATION.cff), to generate a software citation. For conceptual discussion, also cite the relevant Medium article listed above. Include the repository release or commit hash in reproducible research.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New reusable charts should include validation, tests, accessible presentation, deterministic examples, and a documented analytical purpose.

## License

MIT