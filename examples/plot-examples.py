"""Generate Plotly example figures for SciencePlots templates."""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import scienceplots  # noqa: F401


ROOT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT_DIR / "figures" / "plotly"
X_VALUES = np.linspace(0.75, 1.25, 201)


def model(x_values: np.ndarray, p_value: float) -> np.ndarray:
    """Toy model used in the original project examples."""
    return x_values ** (2 * p_value + 1) / (1 + x_values ** (2 * p_value))


def create_line_figure(template: str, p_values: list[float]) -> go.Figure:
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
        xaxis_title="Voltage (mV)",
        yaxis_title=r"Current ($\mu$A)",
        legend_title="Order",
    )
    return figure


def save_html(figure: go.Figure, filename: str) -> None:
    """Save an interactive HTML file for gallery use."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    figure.write_html(OUTPUT_DIR / filename, include_plotlyjs="cdn")


def generate_core_examples() -> None:
    """Generate representative science template combinations."""
    examples = {
        "fig01a.html": ("science", [10, 15, 20, 30, 50, 100]),
        "fig02a.html": ("science+ieee", [10, 20, 40, 100]),
        "fig02c.html": ("science+nature", [10, 15, 20, 30, 50, 100]),
        "fig04.html": ("science+high-vis", [10, 15, 20, 30, 50, 100]),
        "fig06.html": ("science+bright", [5, 10, 15, 20, 30, 50, 100]),
        "fig10.html": ("science+notebook", [10, 15, 20, 30, 50, 100]),
        "fig16.html": ("science+russian-font", [5, 7, 10, 15, 20, 30, 50]),
        "fig17.html": ("science+turkish-font", [5, 7, 10, 15, 20, 30, 50]),
    }
    for filename, (template, p_values) in examples.items():
        save_html(create_line_figure(template, p_values), filename)


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
        save_html(figure, f"fig_dr_{count}.html")


if __name__ == "__main__":
    generate_core_examples()
    generate_discrete_rainbow_examples()
