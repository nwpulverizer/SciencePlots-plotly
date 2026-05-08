"""Configuration of SciencePlots tests."""

import os
from pathlib import Path

import pytest
import scienceplots

TEMPLATES_PATH = Path(scienceplots.__path__[0], "templates")


def get_templates_in_dir(directory):
    """Return set of template filenames (without trailing '.json')."""
    return {fn.stem for fn in Path(directory).glob("*.json")}


@pytest.fixture(scope="session")
def templates_in_scienceplots_per_folder():
    """Output: dictionary of templates per folder in SciencePlots."""
    templates_per_folder = {}
    for folder, _, _ in os.walk(TEMPLATES_PATH):
        folder = Path(folder)
        templates_per_folder[folder.name] = get_templates_in_dir(folder)
    return templates_per_folder
