"""Smoke tests for the hvplot package.

Covers:
- the installed version matches the recipe version (via PKG_VERSION, set by conda-build)
- data-backend wrapper imports (pandas, xarray, dask, networkx)
- the pandas_plotting_backends entry point (pandas .plot() dispatch to hvplot)
"""

import os
from importlib.metadata import version

import holoviews as hv
import pandas as pd

import hvplot.dask  # noqa: F401
import hvplot.networkx  # noqa: F401
import hvplot.pandas  # noqa: F401
import hvplot.xarray  # noqa: F401


def test_version():
    expected = os.environ["PKG_VERSION"]
    assert version("hvplot") == expected


def test_pandas_plotting_backend_entry_point():
    """hvplot registers itself via the pandas_plotting_backends entry point
    (pyproject.toml [project.entry-points."pandas_plotting_backends"]).
    This confirms pandas' .plot() dispatch actually resolves to hvplot.
    """
    pd.options.plotting.backend = "hvplot"
    result = pd.DataFrame({"x": [1, 2, 3]}).plot()
    assert isinstance(result, hv.core.ViewableElement)


if __name__ == "__main__":
    test_version()
    test_pandas_plotting_backend_entry_point()
    print("All hvplot smoke tests passed.")
