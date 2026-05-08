
> [!WARNING]  
> Work in progress. Not yet fully tested. 
>
> This repository is a Plotly-focused fork of the original SciencePlots project.

Science Plots
=============

> **Warning**
> Import `scienceplots` before using templates so they are registered in `plotly.io.templates`.

*Plotly templates for scientific figures*

This repo provides Plotly templates to format figures for scientific papers, presentations, and theses.

<p align="center">
<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig01a.png" width="500">
</p>

You can find generated examples in [`examples/figures`](./examples/figures) and use
[`examples/plot-examples.py`](./examples/plot-examples.py) to regenerate Plotly
gallery outputs.

Getting Started
---------------

The easiest way to install SciencePlots is by using `pip`:

```bash
# to install the latest release (from PyPI)
pip install SciencePlots

# to install the latest release (using Conda)
conda install -c conda-forge scienceplots

# to install the latest commit (from GitHub)
pip install git+https://github.com/nwpulverizer/SciencePlots-plotly

# to clone and install from a local copy
git clone https://github.com/nwpulverizer/SciencePlots-plotly.git
cd SciencePlots-plotly
pip install -e .
```

Import `scienceplots` once in your script so templates are registered in Plotly.

**Notes:**
- Plotly uses MathJax for math text (`$...$`), so a local LaTeX toolchain is not required.
- If you would like to use CJK fonts, install those fonts on your system for local export rendering.

Please see the [FAQ](#faq) for more information and troubleshooting.

Using the Templates
----------------

`"science"` is the primary template in this repo. Use it by registering templates via import and then applying it in Plotly:

```python
import plotly.graph_objects as go
import plotly.io as pio
import scienceplots

pio.templates.default = "science"
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 1, 3])])
fig.show()
```

You can also combine templates:

```python
fig.update_layout(template="science+ieee")
```

In this case, `ieee` overrides parameters from `science` for IEEE-style figures.

You can also apply templates per figure:

```python
fig.update_layout(template="science")
```

Examples
--------

The basic ``science`` template is shown below:

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig01a.png" width="500">

It can be cascaded with other templates to fine-tune appearance. For example, the ``science`` + ``notebook`` templates (intended for Jupyter notebooks):

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig10.png" width="500">

Please see [`examples/plot-examples.py`](./examples/plot-examples.py) for template
combinations used in the gallery examples.

Specific Templates for Academic Journals
-------------------------------------

The ``science`` + ``ieee`` templates for IEEE papers:

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig02a.png" width="500">

   - IEEE requires figures to be readable when printed in black and white. The ``ieee`` style also sets the figure width to fit within one column of an IEEE paper.

The ``science`` + ``nature`` templates for Nature articles:

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig02c.png" width="500">

   - Nature recommends sans-serif fonts.

Other languages
---------------

SciencePlots currently supports:
 * Traditional Chinese
 * Simplified Chinese
 * Japanese
 * Korean
 * Russian
 * Turkish

Example: Traditional Chinese (`science` + `no-latex` + `cjk-tc-font`):

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig14a.png" width="500">

See [Getting Started](#getting-started) for CJK font notes.

Other color cycles
------------------

SciencePlots comes with a variety of different color cycles. For the full set,
see the discrete rainbow section in [`examples/plot-examples.py`](./examples/plot-examples.py).
Two examples are shown below.

The ``bright`` color cycle (color blind safe):

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig06.png" width="500">

The ``high-vis`` color cycle:

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig04.png" width="500">

Paul Tol's discrete rainbow color sets are available as well, with the template identifier ``discrete-rainbow-<n>``, where ``<n>`` is the number of unique colors. ``<n>`` ranges from ``1`` to ``23`` (inclusive). For example, ``discrete-rainbow-15``:

<img src="https://github.com/nwpulverizer/SciencePlots-plotly/raw/master/examples/figures/plotly/fig_dr_15.png" width="500">

Help and Contributing
---------------------

Please feel free to contribute to the SciencePlots repo! For example, it would be good to add new styles for different journals and add new color cycles. Before starting a new style or making any changes, please create an issue through the [GitHub issue tracker](https://github.com/nwpulverizer/SciencePlots-plotly/issues). That way we can discuss if the changes are necessary and the best approach.

If you need any help with SciencePlots, please first check the [FAQ](#faq) and
search through the [previous GitHub issues](https://github.com/nwpulverizer/SciencePlots-plotly/issues).
If you can't find an answer, create a new issue through the
[GitHub issue tracker](https://github.com/nwpulverizer/SciencePlots-plotly/issues).

You can check [Plotly's template documentation](https://plotly.com/python/templates/) for more information on plotting settings.

FAQ
---

Use this section as the primary FAQ reference for this repository.


Cite
---
Cite the original author of the matplotlib repo please. I didn't really do any work here. 
https://github.com/garrettj403/SciencePlots
      doi          = {10.5281/zenodo.4106649},
      url          = {http://doi.org/10.5281/zenodo.4106649}
    }
