from __future__ import annotations

from typing import Sequence, Optional
import matplotlib.pyplot as plt

from .theme import Theme, DEFAULT_THEME, apply_theme


def styled_line(
    x: Sequence[float],
    y: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    marker: str = "o",
    theme: Theme = DEFAULT_THEME,
    ax=None,
    show: bool = True,
):
    apply_theme(theme)
    if ax is None:
        fig, ax = plt.subplots(figsize=(7.2, 4.2))
    else:
        fig = ax.figure

    c = color or theme.primary
    ax.plot(x, y, color=c, marker=marker, markersize=theme.marker_size)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax
