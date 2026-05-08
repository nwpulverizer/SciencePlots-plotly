
> [!WARNING]  
> Work in progress. Not yet fully implemented. This is currently just the base repo of science plots
>
> This repository is a Plotly-focused fork of the original SciencePlots project.

Science Plots
=============

<p align="left">
    <table>
        <tr>
            <td style="text-align: center;">PyPI version</td>
            <td style="text-align: center;">
                <a href="https://badge.fury.io/py/SciencePlots">
                    <img src="https://badge.fury.io/py/SciencePlots.svg" alt="PyPI version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">conda-forge version</td>
            <td style="text-align: center;">
                <a href="https://anaconda.org/conda-forge/scienceplots">
                    <img src="https://anaconda.org/conda-forge/scienceplots/badges/version.svg" alt="conda-forge version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">DOI</td>
            <td style="text-align: center;">
                <a href="https://zenodo.org/badge/latestdoi/144605189">
                    <img src="https://zenodo.org/badge/144605189.svg" alt="DOI" height="18"/>
                </a>
            </td>
        </tr>
    </table>
</p>

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

SciencePlots in Academic Papers
-------------------------------

The following papers use ``SciencePlots``:

- C.-S. Li, S.-P. Ma, and T.-H. Lin, ["FMSA: A Universal Microservice Architecture Based on FHIR Medical Informatics Standard,"](https://ieeexplore.ieee.org/document/11326732) 2025 Second International Conference on Artificial Intelligence for Medicine, Health and Care (AIxMHC), pp. 42–49, Oct. 2025.

- Keçeci, Mehmet. "Scalable Complexity: Mathematical Analysis and Potential for Physical Applications of the Keçeci Circle Fractal", 13 May 2025. https://doi.org/10.5281/zenodo.15396198. (Reference has been made to the module "SciencePlots".)

- J. D. Garrett, C.-Y. E. Tong, L. Zeng, T.-J. Chen and M.-J. Wang, ["A 345 GHz Sideband-Separating Receiver Prototype with Ultra-Wide Instantaneous Bandwidth,"](https://ieeexplore.ieee.org/document/10089556) *IEEE Trans. THz Sci. Technol.*, vol. 13, no. 3, pp. 237-245, Mar. 2023.

- J. Garrett, B.-K. Tan, C. Chaumont, F. Boussaha, and G. Yassin, ["A 230-GHz Endfire SIS Mixer With Near Quantum-Limited Performance,"](https://ieeexplore.ieee.org/document/9833810) *IEEE Microw. Wirel. Compon. Lett.*, Jul. 2022. ([open access](https://ora.ox.ac.uk/objects/uuid:59a100bf-c997-499a-be20-01fc66fffe2b))

- J. Garrett, and E. Tong, ["Measuring Cryogenic Waveguide Loss in the Terahertz Regime,"](https://ieeexplore.ieee.org/document/9727077) *IEEE Trans. THz Sci. Technol.*, vol. 12, no. 3, pp. 293-299, May 2022.

- Y. Liu, X. Liu, and Y. Sun, ["QGrain: An open-source and easy-to-use software for the comprehensive analysis of grain size distributions"](https://doi.org/10.1016/j.sedgeo.2021.105980), *Sedimentary Geology*, vol. 423, 105980, Aug. 2021.

- M. Gasanov, *et al.*, ["A New Multi-objective Approach to Optimize Irrigation Using a Crop Simulation Model and Weather History"](https://link.springer.com/chapter/10.1007/978-3-030-77970-2_7) in *Computational Science–ICCS 2021*, Krakow, Poland, Jun. 2021, pp. 75-88. ([open access](https://www.researchgate.net/profile/Sergey-Matveev-5/publication/352285985_A_New_Multi-objective_Approach_to_Optimize_Irrigation_Using_a_Crop_Simulation_Model_and_Weather_History/links/60e74b88b8c0d5588ce2da07/A-New-Multi-objective-Approach-to-Optimize-Irrigation-Using-a-Crop-Simulation-Model-and-Weather-History.pdf))

- J. Garrett, and E. Tong, ["A Dispersion-Compensated Algorithm for the Analysis of Electromagnetic Waveguides,"](https://ieeexplore.ieee.org/document/9447194) *IEEE Signal Process. Lett.*, vol. 28, pp. 1175-1179, Jun. 2021.

- G. Jegannathan, *et al.*, ["Current-Assisted SPAD with Improved p-n Junction and Enhanced NIR Performance"](https://www.mdpi.com/1424-8220/20/24/7105), *Sensors*, Dec 2020. ([open access](https://www.mdpi.com/1424-8220/20/24/7105))

- H. Tian, *et al.*, ["ivis Dimensionality Reduction Framework for Biomacromolecular Simulations"](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00485), *J. Chem. Inf. Model.*, Aug 2020. ([open access](https://arxiv.org/pdf/2004.10718.pdf))

- P. Stoltz, *et al.*, ["A new simple algorithm for space charge limited emission,"](https://aip.scitation.org/doi/10.1063/5.0020781) *Phys. Plasmas*, vol. 27, no. 9, pp. 093103, Sep. 2020. ([open access](https://aip.scitation.org/doi/10.1063/5.0020781))

- J. Garrett, *et al.*, ["A Nonlinear Transmission Line Model for Simulating Distributed SIS Frequency Multipliers,"](https://ieeexplore.ieee.org/abstract/document/9050728)  *IEEE Trans. THz Sci. Technol.*, vol. 10, no. 3, pp. 246-255, May 2020. ([open access](https://ora.ox.ac.uk/objects/uuid:5ca31c2c-a984-462c-b21a-3fe16eee0d9b/download_file?safe_filename=XXXX_final_JohnGarrett.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["Simulating the Behavior of a 230 GHz SIS Mixer Using Multi-Tone Spectral Domain Analysis,"](https://ieeexplore.ieee.org/document/8822760/) *IEEE Trans. THz Sci. Technol.*, vol. 9, no. 9, pp. 540-548, Nov. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:0fd4537d-258c-454a-bbfb-09b1bcd88d49/download_file?file_format=pdf&safe_filename=XXXX_final.pdf&type_of_work=Journal+article))

- J. Garrett, *et al.*, ["A Compact and Easy to Fabricate E-plane Waveguide Bend,"](https://ieeexplore.ieee.org/document/8760521) *IEEE Microw. Wireless Compon. Lett.*, vol. 29, no. 8, pp. 529-531, Aug. 2019. ([open access](https://ora.ox.ac.uk/objects/uuid:496855f9-be2a-47cd-b498-1753d8033f50/download_file?file_format=pdf&safe_filename=Waveguide_Bend__IEEE_MWCL_.pdf&type_of_work=Journal+article))

- J. Garrett, ["A 230 GHz Focal Plane Array Using a Wide IF Bandwidth SIS Receiver,"](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis) DPhil thesis, University of Oxford, Oxford, UK, 2018. ([open access](https://ora.ox.ac.uk/objects/uuid:d47fbf3b-1cf3-4e58-be97-767b9893066e/download_file?file_format=pdf&safe_filename=GarrettJ_DPhilThesis.pdf&type_of_work=Thesis))

If you use ``SciencePlots`` in your paper/thesis, feel free to add it to the list!

Citing SciencePlots
-------------------

You don't have to cite SciencePlots if you use it but it's nice if you do:

    @article{SciencePlots,
      author       = {John D. Garrett},
      title        = {{garrettj403/SciencePlots}},
      month        = sep,
      year         = 2021,
      publisher    = {Zenodo},
      version      = {1.0.9},
      doi          = {10.5281/zenodo.4106649},
      url          = {http://doi.org/10.5281/zenodo.4106649}
    }
