from __future__ import annotations

from typing import Sequence, Optional
import matplotlib.pyplot as plt

from .theme import Theme, DEFAULT_THEME, apply_theme


def styled_area(
    x: Sequence[float],
    y: Sequence[float],
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Optional[str] = None,
    alpha: float = 0.25,
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
    ax.plot(x, y, color=c)
    ax.fill_between(x, y, color=c, alpha=alpha)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    if show:
        plt.show()
    return fig, ax
