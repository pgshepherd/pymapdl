"""Small or misc tests that don't fit in other test modules"""
import numpy as np
import pyvista as pv

import pytest
from pyvista.plotting import system_supports_plotting

from ansys.mapdl import core as pymapdl

def test_report():
    report = pymapdl.Report(gpu=system_supports_plotting())
    assert 'PyMAPDL Software and Environment Report' in str(report)
