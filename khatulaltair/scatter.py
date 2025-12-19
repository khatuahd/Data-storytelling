from __future__ import annotations

from typing import Sequence, Optional
import matplotlib.pyplot as plt

from .theme import Theme, DEFAULT_THEME, apply_theme


def styled_scatter(
    x: Sequence[float],
    y: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    size: int = 60,
    alpha: float = 0.85,
    theme: Theme = DEFAULT_THEME,
    ax=None,
    show: bool = True,
):
    apply_theme(theme)
    if ax is None:
        fig, ax = plt.subplots(figsize=(7.2, 4.2))
    else:
        fig = ax.figure

    c = color or theme.secondary
    ax.scatter(x, y, s=size, alpha=alpha, color=c, edgecolor=theme.bg, linewidth=0.8)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax
