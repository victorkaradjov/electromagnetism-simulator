import numpy as np


def initialize_fields(N):
    # Validate the number of cells
    if not isinstance(N, (int, np.integer)) or isinstance(N, bool) or N <= 0:
        raise ValueError(f"N should be a positive integer, got N = {N}")

    # Initialize electric and magnetic fields
    e_x = np.zeros(N + 1)
    h_y = np.zeros(N)

    return e_x, h_y