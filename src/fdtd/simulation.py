import numpy as np

from .fields import initialize_fields
from .grid import create_grid
from .update import (
    apply_mur_boundaries,
    update_electric_field,
    update_magnetic_field,
)


def run_simulation(
    domain_length,
    spatial_step,
    permittivity,
    permeability,
    cfl_number,
    num_time_steps,
    source_center_time,
    source_width,
    source_amplitude,
    source_position_index,
):
    # Validate the number of time steps
    if (
        not isinstance(num_time_steps, (int, np.integer))
        or isinstance(num_time_steps, bool)
        or num_time_steps <= 0
    ):
        raise ValueError("num_time_steps must be a positive integer")

    # Validate physical parameters
    if (
        not np.isfinite(permittivity)
        or not np.isfinite(permeability)
        or permittivity <= 0
        or permeability <= 0
    ):
        raise ValueError("Permittivity and permeability must be positive and finite")

    # Validate source parameters
    if not np.isfinite(source_center_time) or not np.isfinite(source_amplitude):
        raise ValueError("Source center time and amplitude must be finite")

    # Calculate electromagnetic wave propagation speed
    wave_speed = 1 / np.sqrt(permeability * permittivity)

    # Calculate time step using the CFL condition
    time_step = cfl_number * spatial_step / wave_speed

    # Create spatial grids
    num_cells, electric_grid, magnetic_grid = create_grid(domain_length, spatial_step)

    # Initialize electromagnetic fields
    electric_field, magnetic_field = initialize_fields(num_cells)

    # Initialize data storage
    field_snapshots = []
    magnetic_snapshots = []

    snapshot_times = []
    magnetic_snapshot_times = []

    electric_energy = []
    magnetic_energy = []
    total_energy = []

    # FDTD time-stepping loop
    for time_index in range(num_time_steps):
        # Evaluate source at the half-time step
        source_time = (time_index + 0.5) * time_step

        # Store previous electric field for Mur boundary conditions
        previous_electric_field = electric_field.copy()

        # Update magnetic field: H^(n+1/2)
        magnetic_field = update_magnetic_field(
            electric_field,
            magnetic_field,
            time_step,
            spatial_step,
            permeability,
        )

        magnetic_snapshots.append(magnetic_field.copy())
        magnetic_snapshot_times.append((time_index + 0.5) * time_step)

        # Update electric field: E^(n+1)
        electric_field = update_electric_field(
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
        )

        # Apply Mur absorbing boundary conditions
        electric_field = apply_mur_boundaries(
            electric_field,
            previous_electric_field,
            cfl_number,
        )

        field_snapshots.append(electric_field.copy())
        snapshot_times.append((time_index + 1) * time_step)

        # Calculate electric energy
        electric_energy.append(
            0.5
            * permittivity
            * spatial_step
            * (
                0.5 * electric_field[0] ** 2
                + np.sum(electric_field[1:-1] ** 2)
                + 0.5 * electric_field[-1] ** 2
            )
        )

        # Calculate magnetic energy
        magnetic_energy.append(
            0.5 * permeability * spatial_step * np.sum(magnetic_field**2)
        )

        # Calculate total electromagnetic energy
        total_energy.append(electric_energy[-1] + magnetic_energy[-1])

    # Convert stored data to NumPy arrays
    return {
        "wave_speed": wave_speed,
        "time_step": time_step,
        "num_cells": num_cells,
        "electric_grid": electric_grid,
        "magnetic_grid": magnetic_grid,
        "field_snapshots": np.array(field_snapshots),
        "magnetic_snapshots": np.array(magnetic_snapshots),
        "snapshot_times": np.array(snapshot_times),
        "magnetic_snapshot_times": np.array(magnetic_snapshot_times),
        "electric_energy": np.array(electric_energy),
        "magnetic_energy": np.array(magnetic_energy),
        "total_energy": np.array(total_energy),
        "final_electric_field": electric_field,
        "final_magnetic_field": magnetic_field,
    }
