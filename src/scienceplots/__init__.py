from pathlib import Path

import plotly.io as pio

from .templates_discovery import read_templates_in_folders

TEMPLATES_DIR_NAME = "templates"

templates_path = Path(__file__).resolve().parent / TEMPLATES_DIR_NAME
templates = read_templates_in_folders(templates_path)
for name, template in templates.items():
    pio.templates[name] = template
