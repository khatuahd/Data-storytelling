from __future__ import annotations

from dataclasses import dataclass
import matplotlib as mpl


@dataclass(frozen=True)
class Theme:
    # Colors
    primary: str = "#2563EB"
    secondary: str = "#16A34A"
    accent: str = "#F59E0B"
    danger: str = "#DC2626"
    muted: str = "#64748B"
    grid: str = "#E2E8F0"
    bg: str = "#FFFFFF"
    text: str = "#0F172A"

    # Typography
    font_family: str = "DejaVu Sans"
    title_size: int = 14
    label_size: int = 11
    tick_size: int = 10

    # Geometry
    line_width: float = 2.2
    marker_size: int = 6


DEFAULT_THEME = Theme()


def apply_theme(theme: Theme = DEFAULT_THEME) -> None:
    """Apply a consistent Matplotlib style (rcParams)."""
    mpl.rcParams.update(
        {
            "figure.facecolor": theme.bg,
            "axes.facecolor": theme.bg,
            "savefig.facecolor": theme.bg,

            "font.family": theme.font_family,

            "axes.edgecolor": theme.grid,
            "axes.labelcolor": theme.text,
            "axes.titlecolor": theme.text,
            "axes.titlesize": theme.title_size,
            "axes.titleweight": "bold",
            "axes.labelsize": theme.label_size,

            "xtick.color": theme.text,
            "ytick.color": theme.text,
            "xtick.labelsize": theme.tick_size,
            "ytick.labelsize": theme.tick_size,

            "grid.color": theme.grid,
            "grid.linestyle": "-",
            "grid.linewidth": 0.8,
            "axes.grid": True,
            "axes.axisbelow": True,

            "lines.linewidth": theme.line_width,
        }
    )
