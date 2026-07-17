# Data Visualisation Reference

A production-minded reference repository for clear, accessible, scalable, and reusable data visualisation in Python. It combines traditional statistical graphics with interactive dashboards, geospatial analysis, million-point rendering, benchmarking, testing, and CI.

## What this repository solves

- Time-series trends and multi-segment comparisons
- Ranked categorical comparisons
- Distribution and correlation analysis
- Interactive exploration with Plotly
- Shareable analytical dashboards with Streamlit
- Country-level geospatial visualisation
- Million-point rendering with Datashader
- Reproducible chart galleries and rendering benchmarks
- Accessible themes, validation, testing, coverage, and CI

## Repository structure

```text
.
├── Data_Visualisation_Charts.ipynb   # Original traditional-chart notebook
├── apps/streamlit_app.py             # Interactive analytical dashboard
├── benchmarks/benchmark_rendering.py # Matplotlib and Plotly benchmark
├── examples/gallery.py               # Static reproducible gallery
├── examples/geospatial.py            # Interactive choropleth example
├── examples/large_data.py            # Million-point Datashader example
├── src/dataviz_reference/            # Reusable static and interactive API
├── tests/                             # Unit and validation tests
├── .github/workflows/ci.yml          # Lint, tests, coverage, gallery execution
├── CONTRIBUTING.md                   # Contribution quality standards
└── pyproject.toml                    # Packaging and dependency groups
```

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
figure, axis = time_series_chart(
    data,
    date="date",
    value="transactions",
    title="Monthly transactions",
)
figure.savefig("artifacts/monthly_transactions.png", bbox_inches="tight")
```

## Interactive API

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

## Run the dashboard

```bash
streamlit run apps/streamlit_app.py
```

The dashboard demonstrates filtering, segmented time series, multivariate scatter plots, tooltips, zooming, and responsive layout.

## Specialised examples

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
| Distribution | Histograms | Grouped density comparison |
| Relationships | Scatter plots | Multivariate interactive scatter |
| Correlation | Manual matrices | Annotated correlation heatmap |
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

Examples use deterministic synthetic data by default, avoiding unstable downloads and licensing surprises. The APIs accept ordinary pandas DataFrames, so users can directly apply them to open datasets from World Bank Open Data, Our World in Data, data.gov.in, Kaggle, UCI Machine Learning Repository, or their own governed data sources. Always retain the original dataset licence and citation.

## Contributing

See `CONTRIBUTING.md`. New reusable charts should include validation, tests, accessible presentation, deterministic examples, and a documented analytical purpose.

## License

MIT
