# Data Visualisation Reference

A practical reference repository for building clear, accessible, and reusable data visualisations in Python. It covers both traditional charting foundations and modern analytical patterns that can be used in notebooks, reports, dashboards, and production workflows.

## What this repository solves

- Time-series trends and multi-segment comparisons
- Ranked categorical comparisons
- Distribution analysis across groups
- Correlation analysis for numeric features
- Consistent, colour-blind-friendly visual styling
- Reusable chart functions with input validation
- Reproducible examples and automated tests

## Repository structure

```text
.
├── Data_Visualisation_Charts.ipynb   # Original notebook and traditional examples
├── examples/gallery.py               # Reproducible modern chart gallery
├── src/dataviz_reference/            # Reusable visualisation package
├── tests/                             # Unit tests
├── .github/workflows/ci.yml          # Lint, tests, coverage, gallery execution
└── pyproject.toml                     # Packaging and development configuration
```

## Quick start

```bash
git clone https://github.com/sauravsingla/Data_Visualisation.git
cd Data_Visualisation
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
python examples/gallery.py
```

Generated charts are written to `artifacts/`.

## Example

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

time_series_chart(
    data,
    date="date",
    value="transactions",
    title="Monthly transactions",
)
```

## Traditional and modern coverage

| Area | Traditional foundation | Modern implementation |
|---|---|---|
| Line charts | Direct Matplotlib plotting | Validated, sorted, reusable time-series helper |
| Bar charts | Basic vertical bars | Ranked horizontal bars with direct labels |
| Distributions | Histograms | Histogram plus density and group comparison |
| Relationships | Scatter plots | Correlation matrices and analytical summaries |
| Styling | Per-chart formatting | Shared accessible theme and export defaults |
| Reliability | Manual notebook execution | Automated linting, tests, coverage, and CI |

## Design principles

1. Start with the analytical question, not the chart type.
2. Prefer direct labels, meaningful titles, and honest scales.
3. Avoid unnecessary 3D effects, decoration, and chart junk.
4. Use accessible colours and readable typography.
5. Validate data before plotting.
6. Keep examples deterministic and reproducible.
7. Separate reusable plotting logic from exploratory notebooks.

## Quality checks

```bash
ruff check .
pytest --cov=dataviz_reference --cov-report=term-missing
python examples/gallery.py
```

The GitHub Actions workflow runs these checks on Python 3.10, 3.11, and 3.12.

## Roadmap

- Interactive Plotly reference patterns
- Dashboard examples using Streamlit
- Geospatial visualisation examples
- Large-data rendering with Datashader
- Benchmark comparison across charting libraries
- Visual regression testing

## Contributing

Contributions are welcome. Keep examples focused on a real analytical question, include deterministic sample data, add tests for reusable code, and document the intended interpretation of each chart.

## License

MIT
