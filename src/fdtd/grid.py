import math

import numpy as np


def cell_num(length, dz):
    # Validate spatial parameter types
    if not isinstance(length, (int, float)) or isinstance(length, bool):
        raise TypeError("length must be a numeric scalar")

    if not isinstance(dz, (int, float)) or isinstance(dz, bool):
        raise TypeError("dz must be a numeric scalar")

    # Validate spatial parameters
    if not math.isfinite(length) or length <= 0:
        raise ValueError(f"length should be positive and finite, got length = {length}")

    if not math.isfinite(dz) or dz <= 0:
        raise ValueError(f"dz should be positive and finite, got dz = {dz}")

    # Calculate the number of cells
    N_float = length / dz
    N = round(N_float)

    # Check whether the domain length is divisible by the spatial step
    limit = math.isclose(N_float, N, rel_tol=0, abs_tol=1e-9)

    if N < 1:
        raise ValueError(f"N should be at least 1, got N = {N}")

    if not limit:
        raise ValueError(
            f"length should be divisible by dz, got length / dz = {N_float}"
        )

    return N


def create_grid(length, dz):
    # Calculate the number of cells
    N = cell_num(length, dz)

    # Create the electric and magnetic field grids
    z_e = np.linspace(0, length, N + 1)
    z_h = np.linspace(dz / 2, length - dz / 2, N)

    return N, z_e, z_h
