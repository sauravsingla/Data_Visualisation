"""Accessible and publication-friendly visual defaults."""

from __future__ import annotations

import matplotlib as mpl


def apply_accessible_theme() -> None:
    """Apply consistent defaults for readable charts.

    The configuration avoids chart junk, keeps text legible, and uses a
    colour-blind-friendly cycle suitable for reports and presentations.
    """
    mpl.rcParams.update(
        {
            "figure.figsize": (10, 6),
            "figure.dpi": 120,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.axisbelow": True,
            "grid.alpha": 0.25,
            "axes.titleweight": "bold",
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "legend.frameon": False,
            "font.size": 10,
            "savefig.bbox": "tight",
            "savefig.dpi": 200,
            "axes.prop_cycle": mpl.cycler(
                color=["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9"]
            ),
        }
    )
