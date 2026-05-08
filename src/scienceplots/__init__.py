from pathlib import Path

import plotly.io as pio

from .templates_discovery import read_templates_in_folders


templates_path = Path(__file__).resolve().parent / "templates"
templates = read_templates_in_folders(templates_path)
for name, template in templates.items():
    pio.templates[name] = template
