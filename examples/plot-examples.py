"""Generate Plotly example figures for SciencePlots templates.

Outputs both interactive HTML files and static PNG images.
PNG images are used in the README; HTML files provide interactive gallery versions.
"""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import scienceplots  # noqa: F401


ROOT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT_DIR / "figures" / "plotly"
X_VALUES = np.linspace(0.75, 1.25, 201)
PNG_WIDTH = 900
PNG_HEIGHT = 600
PNG_SCALE = 2


def model(x_values: np.ndarray, p_value: float) -> np.ndarray:
    """Toy model used in the original project examples."""
    return x_values ** (2 * p_value + 1) / (1 + x_values ** (2 * p_value))


def create_line_figure(
    template: str,
    p_values: list[float],
    xlabel: str = "Voltage (mV)",
    ylabel: str = r"Current ($\mu$A)",
) -> go.Figure:
    """Build one multi-line figure using a template expression."""
    figure = go.Figure()
    for p_value in p_values:
        figure.add_trace(
            go.Scatter(
                x=X_VALUES,
                y=model(X_VALUES, p_value),
                mode="lines",
                name=f"Order {p_value:g}",
            )
        )
    figure.update_layout(
        template=template,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        legend_title="Order",
    )
    return figure


def save_outputs(figure: go.Figure, stem: str) -> None:
    """Save both an interactive HTML file and a static PNG for a figure."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    figure.write_html(OUTPUT_DIR / f"{stem}.html", include_plotlyjs="cdn")
    figure.write_image(
        OUTPUT_DIR / f"{stem}.png",
        width=PNG_WIDTH,
        height=PNG_HEIGHT,
        scale=PNG_SCALE,
    )


def generate_core_examples() -> None:
    """Generate representative science template combinations."""
    examples = {
        "fig01a": ("science", [10, 15, 20, 30, 50, 100], {}, "science"),
        "fig02a": ("science+ieee", [10, 20, 40, 100], {}, "science+ieee"),
        "fig02c": ("science+nature", [10, 15, 20, 30, 50, 100], {}, "science+nature"),
        "fig04": ("science+high-vis", [10, 15, 20, 30, 50, 100], {}, "science+high-vis"),
        "fig06": ("science+bright", [5, 10, 15, 20, 30, 50, 100], {}, "science+bright"),
        "fig10": ("science+notebook", [10, 15, 20, 30, 50, 100], {}, "science+notebook"),
        "fig14a": (
            "science",
            [5, 7, 10, 15, 20, 30, 38, 50, 100],
            {"xlabel": "電壓 (mV)", "ylabel": "電流 (μA)"},
            "science (Traditional Chinese)",
        ),
        "fig16": ("science+russian-font", [5, 7, 10, 15, 20, 30, 50], {}, "science+russian-font"),
        "fig17": ("science+turkish-font", [5, 7, 10, 15, 20, 30, 50], {}, "science+turkish-font"),
    }
    for stem, (template, p_values, extra, _title) in examples.items():
        fig = create_line_figure(template, p_values, **extra)
        save_outputs(fig, stem)


def generate_discrete_rainbow_examples() -> None:
    """Generate one file per discrete-rainbow template."""
    p_values = np.logspace(0, 2, 23)
    for count in range(1, 24):
        template = f"science+discrete-rainbow-{count}"
        figure = go.Figure()
        for p_value in p_values[:count]:
            figure.add_trace(
                go.Scatter(
                    x=X_VALUES,
                    y=model(X_VALUES, p_value),
                    mode="lines",
                    showlegend=False,
                )
            )
        figure.update_layout(
            template=template,
            xaxis_title="Voltage (mV)",
            yaxis_title=r"Current ($\mu$A)",
            title=f"discrete-rainbow-{count}",
        )
        save_outputs(figure, f"fig_dr_{count}")


if __name__ == "__main__":
    generate_core_examples()
    generate_discrete_rainbow_examples()
