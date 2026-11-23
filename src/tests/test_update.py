import numpy as np
import pytest
from fdtd.update import update_electric_field, update_magnetic_field, apply_mur_boundaries


def test_update_magnetic_field():
    electric_field = np.array([0.0, 2.0, 4.0])
    magnetic_field = np.array([0.0, 0.0])

    time_step = 1.0
    spatial_step = 1.0
    permeability = 1.0

    result = update_magnetic_field(
        electric_field,
        magnetic_field,
        time_step,
        spatial_step,
        permeability,
    )

    expected = np.array([-2.0, -2.0])

    np.testing.assert_array_equal(result, expected)


def test_update_magnetic_field_invalid_dimensions():
    electric_field = np.array([0.0, 2.0, 4.0])
    magnetic_field = np.array([0.0, 0.0, 0.0])

    with pytest.raises(ValueError):
        update_magnetic_field(
            electric_field,
            magnetic_field,
            1.0,
            1.0,
            1.0,
        )


def test_update_electric_field():
    electric_field = np.array([0.0, 0.0, 0.0])
    magnetic_field = np.array([0.0, 2.0])

    result = update_electric_field(
        electric_field,
        magnetic_field,
        1.0,  # time_step
        1.0,  # spatial_step
        1.0,  # permittivity
        0.0,  # source_time
        0.0,  # source_center_time
        1.0,  # source_width
        0.0,  # source_amplitude
        2,  # num_cells
        1,  # source_position_index
    )

    expected = np.array([0.0, -2.0, 0.0])

    np.testing.assert_array_equal(result, expected)


def test_apply_mur_boundaries():
    electric_field = np.array([0.0, 2.0, 4.0])
    previous_electric_field = np.array([1.0, 3.0, 5.0])
    cfl_number = 1.0

    result = apply_mur_boundaries(
        electric_field,
        previous_electric_field,
        cfl_number,
    )

    expected = np.array([3.0, 2.0, 3.0])

    np.testing.assert_array_equal(result, expected)

def test_update_magnetic_field_invalid_permeability():
    electric_field = np.array([0.0, 2.0, 4.0])
    magnetic_field = np.array([0.0, 0.0])

    with pytest.raises(ValueError):
        update_magnetic_field(
            electric_field,
            magnetic_field,
            1.0,
            1.0,
            0.0,  # permeability invalide
        )

def test_apply_mur_boundaries_invalid_cfl():
    electric_field = np.array([0.0, 2.0, 4.0])
    previous_electric_field = np.array([1.0, 3.0, 5.0])

    with pytest.raises(ValueError):
        apply_mur_boundaries(
            electric_field,
            previous_electric_field,
            1.5,  # CFL supérieur à 1
        )