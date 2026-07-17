"""Run with: streamlit run apps/streamlit_app.py"""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from dataviz_reference.interactive import interactive_scatter, interactive_time_series

st.set_page_config(page_title="Data Visualisation Reference", layout="wide")
st.title("Data Visualisation Reference Dashboard")
st.caption("Interactive patterns for trends, segmentation, and multivariate analysis.")

rng = np.random.default_rng(42)
dates = pd.date_range("2025-01-01", periods=24, freq="MS")
segments = ["Consumer", "Business", "Platform"]
trend = pd.DataFrame(
    [
        {
            "date": date,
            "segment": segment,
            "transactions": max(0, 1000 + i * 55 + offset + rng.normal(0, 55)),
        }
        for i, date in enumerate(dates)
        for segment, offset in zip(segments, [0, 250, 500], strict=True)
    ]
)

selected_segments = st.multiselect("Segments", segments, default=segments)
filtered = trend[trend["segment"].isin(selected_segments)]

left, right = st.columns(2)
with left:
    st.plotly_chart(
        interactive_time_series(
            filtered,
            date="date",
            value="transactions",
            group="segment",
            title="Monthly transaction trend",
        ),
        use_container_width=True,
    )

scatter = pd.DataFrame(
    {
        "latency_ms": rng.gamma(4, 20, 500),
        "throughput": rng.normal(1500, 300, 500),
        "error_rate": rng.uniform(0.1, 3.0, 500),
        "environment": rng.choice(["Production", "Staging"], 500, p=[0.8, 0.2]),
    }
)
with right:
    st.plotly_chart(
        interactive_scatter(
            scatter,
            x="latency_ms",
            y="throughput",
            color="environment",
            size="error_rate",
            title="System performance explorer",
        ),
        use_container_width=True,
    )

st.subheader("Filtered data")
st.dataframe(filtered, use_container_width=True, hide_index=True)
