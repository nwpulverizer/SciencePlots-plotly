"""Test suite of SciencePlots."""

import plotly.graph_objects as go
import plotly.io as pio


def test_plotly_required_api_existence():
    """Check if all Plotly API pieces used by scienceplots are available."""
    assert hasattr(pio, "templates")
    assert hasattr(pio.templates, "default")


def test_templates_existence(templates_in_scienceplots_per_folder):
    """Check all templates are available in plotly.io.templates."""
    for folder, templates in templates_in_scienceplots_per_folder.items():
        assert len(templates) > 0, f"No templates found in {folder}."
        for template in templates:
            assert template in pio.templates, (
                f"'{template}' not in available templates. Template in folder {folder}."
            )


def test_usage_of_each_template(templates_in_scienceplots_per_folder):
    """Test templates are valid and can be applied to a figure."""
    for _, templates in templates_in_scienceplots_per_folder.items():
        for template in templates:
            fig = go.Figure(data=[go.Scatter(x=[0, 1], y=[0, 1], name="line")])
            fig.update_layout(template=template, title="Template test")
            serialized = fig.to_json()
            assert serialized
