"""Generate an interactive country-level choropleth."""

from pathlib import Path

import pandas as pd

from dataviz_reference.interactive import interactive_choropleth

OUTPUT = Path("artifacts")
OUTPUT.mkdir(exist_ok=True)

data = pd.DataFrame(
    {
        "country": ["India", "United States", "Brazil", "Germany", "Japan", "Australia"],
        "adoption_index": [92, 84, 71, 77, 81, 74],
    }
)

figure = interactive_choropleth(
    data,
    location="country",
    value="adoption_index",
    title="Illustrative digital adoption index",
)
figure.write_html(OUTPUT / "geospatial_adoption.html", include_plotlyjs="cdn")
