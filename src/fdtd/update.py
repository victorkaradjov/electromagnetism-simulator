import numpy as np

from .source import gaussian_source


def _validate_fields(electric_field, magnetic_field):
    if not isinstance(electric_field, np.ndarray):
        raise TypeError("electric_field must be a NumPy array")

    if not isinstance(magnetic_field, np.ndarray):
        raise TypeError("magnetic_field must be a NumPy array")

    if electric_field.ndim != 1 or magnetic_field.ndim != 1:
        raise ValueError("Fields must be one-dimensional arrays")

    if electric_field.size != magnetic_field.size + 1:
        raise ValueError("Incompatible field dimensions")

    if not np.issubdtype(electric_field.dtype, np.number):
        raise TypeError("electric_field must contain numeric values")

    if not np.issubdtype(magnetic_field.dtype, np.number):
        raise TypeError("magnetic_field must contain numeric values")


def _validate_parameters(time_step, spatial_step, material_parameter):
    parameters = {
        "time_step": time_step,
        "spatial_step": spatial_step,
        "material_parameter": material_parameter,
    }

    for name, value in parameters.items():
        if not np.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be positive and finite, got {value}")


def _validate_mur_fields(electric_field, previous_electric_field):
    if not isinstance(electric_field, np.ndarray):
        raise TypeError("electric_field must be a NumPy array")

    if not isinstance(previous_electric_field, np.ndarray):
        raise TypeError("previous_electric_field must be a NumPy array")

    if electric_field.ndim != 1 or previous_electric_field.ndim != 1:
        raise ValueError("Fields must be one-dimensional arrays")

    if electric_field.size != previous_electric_field.size:
        raise ValueError("Electric fields must have the same size")

    if electric_field.size < 2:
        raise ValueError("Electric fields must contain at least two elements")

    if not np.issubdtype(electric_field.dtype, np.number):
        raise TypeError("electric_field must contain numeric values")

    if not np.issubdtype(previous_electric_field.dtype, np.number):
        raise TypeError("previous_electric_field must contain numeric values")


def _validate_cfl(cfl_number):
    if not np.isfinite(cfl_number) or not 0 < cfl_number <= 1:
        raise ValueError(f"cfl_number must be between 0 and 1, got {cfl_number}")


def update_magnetic_field(
    electric_field, magnetic_field, time_step, spatial_step, permeability
):
    _validate_parameters(time_step, spatial_step, permeability)
    _validate_fields(electric_field, magnetic_field)

    update_coefficient = time_step / (permeability * spatial_step)

    magnetic_field += update_coefficient * (electric_field[:-1] - electric_field[1:])

    return magnetic_field


def update_electric_field(
    electric_field,
    magnetic_field,
    time_step,
    spatial_step,
    permittivity,
    source_time,
    source_center_time,
    source_width,
    source_amplitude,
    num_cells,
    source_position_index,
):
    _validate_parameters(time_step, spatial_step, permittivity)
    _validate_fields(electric_field, magnetic_field)

    if not isinstance(num_cells, (int, np.integer)) or isinstance(num_cells, bool):
        raise TypeError("num_cells must be an integer")

    if num_cells != magnetic_field.size:
        raise ValueError("num_cells must match the magnetic field size")

    update_coefficient = time_step / (permittivity * spatial_step)

    source = gaussian_source(
        source_time,
        source_center_time,
        source_width,
        source_amplitude,
        num_cells,
        source_position_index,
    )

    electric_field[1:-1] += (
        update_coefficient * (magnetic_field[:-1] - magnetic_field[1:])
        - (spatial_step * update_coefficient) * source[1:-1]
    )

    return electric_field


def apply_mur_boundaries(electric_field, previous_electric_field, cfl_number):
    _validate_mur_fields(electric_field, previous_electric_field)
    _validate_cfl(cfl_number)

    coefficient = (cfl_number - 1) / (cfl_number + 1)

    # Left boundary
    electric_field[0] = previous_electric_field[1] + coefficient * (
        electric_field[1] - previous_electric_field[0]
    )

    # Right boundary
    electric_field[-1] = previous_electric_field[-2] + coefficient * (
        electric_field[-2] - previous_electric_field[-1]
    )

    return electric_field
