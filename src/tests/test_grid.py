import numpy as np
import pytest
from fdtd.grid import cell_num, create_grid


def test_cell_num():
    assert cell_num(1.0, 0.001) == 1000


def test_cell_num_invalid_length():
    with pytest.raises(ValueError):
        cell_num(0, 0.001)


def test_cell_num_invalid_spatial_step():
    with pytest.raises(ValueError):
        cell_num(1.0, 0)


def test_cell_num_non_divisible_length():
    with pytest.raises(ValueError):
        cell_num(1.0, 0.003)


def test_cell_num_domain_smaller_than_one_cell():
    with pytest.raises(ValueError):
        cell_num(0.001, 0.002)


def test_cell_num_infinite_length():
    with pytest.raises(ValueError):
        cell_num(np.inf, 0.001)


def test_cell_num_infinite_spatial_step():
    with pytest.raises(ValueError):
        cell_num(1.0, np.inf)


def test_create_grid_dimensions():
    N, z_e, z_h = create_grid(1.0, 0.001)

    assert N == 1000
    assert z_e.shape == (1001,)
    assert z_h.shape == (1000,)


def test_create_grid_electric_positions():
    N, z_e, z_h = create_grid(1.0, 0.001)

    assert z_e[0] == 0.0
    assert z_e[-1] == 1.0

    np.testing.assert_allclose(
        np.diff(z_e),
        0.001,
    )


def test_create_grid_magnetic_positions():
    N, z_e, z_h = create_grid(1.0, 0.001)

    assert z_h[0] == pytest.approx(0.0005)
    assert z_h[-1] == pytest.approx(0.9995)

    np.testing.assert_allclose(
        z_h,
        z_e[:-1] + 0.0005,
    )
