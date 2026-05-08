import json
from pathlib import Path

import plotly.graph_objects as go


def read_templates_in_folders(root_path):
    """Read all Plotly template JSON files in a folder tree."""
    templates = {}
    for template_path in Path(root_path).rglob("*.json"):
        with template_path.open(encoding="utf-8") as f:
            template_dict = json.load(f)
        template_name = template_path.stem
        templates[template_name] = go.layout.Template(template_dict)
    return templates
