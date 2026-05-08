import json
from pathlib import Path

import plotly.graph_objects as go


def read_templates_in_folders(root_path):
    """
    Read Plotly template JSON files from a folder tree.

    Parameters
    ----------
    root_path : str | pathlib.Path
        Root folder containing template JSON files.

    Returns
    -------
    dict[str, go.layout.Template]
        Mapping from template filename stem to Plotly template object.
    """
    templates = {}
    for template_path in Path(root_path).rglob("*.json"):
        try:
            with template_path.open(encoding="utf-8") as f:
                template_dict = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid template JSON in '{template_path}'.") from exc
        template_name = template_path.stem
        templates[template_name] = go.layout.Template(template_dict)
    return templates
