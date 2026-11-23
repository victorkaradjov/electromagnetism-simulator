import numpy as np
import pytest
from fdtd.source import gaussian_source


def test_gaussian_source_peak():
    source = gaussian_source(
        t=1.0,
        t0=1.0,
        tau=0.5,
        j0=2.0,
        N=4,
        source_index=2,
    )

    assert source[2] == 2.0
    assert np.count_nonzero(source) == 1


def test_gaussian_source_decreases_away_from_center():
    center = gaussian_source(1.0, 1.0, 0.5, 2.0, 4, 2)
    away = gaussian_source(1.5, 1.0, 0.5, 2.0, 4, 2)

    assert away[2] < center[2]


def test_gaussian_source_position():
    source = gaussian_source(1.0, 1.0, 0.5, 2.0, 4, 3)

    assert source.shape == (5,)
    assert source[3] == 2.0
    assert np.count_nonzero(source) == 1

def test_gaussian_source_invalid_N():
    with pytest.raises(ValueError):
        gaussian_source(1.0, 1.0, 0.5, 2.0, 0, 0)


def test_gaussian_source_invalid_tau():
    with pytest.raises(ValueError):
        gaussian_source(1.0, 1.0, 0.0, 2.0, 4, 2)


def test_gaussian_source_invalid_index():
    with pytest.raises(ValueError):
        gaussian_source(1.0, 1.0, 0.5, 2.0, 4, 5)


def test_gaussian_source_non_integer_index():
    with pytest.raises(ValueError):
        gaussian_source(1.0, 1.0, 0.5, 2.0, 4, 2.5)
