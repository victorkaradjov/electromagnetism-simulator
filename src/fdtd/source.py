import numpy as np


def gaussian_source(t, t0, tau, j0, N, source_index):
    # Validate numerical parameters
    parameters = {
        "t": t,
        "t0": t0,
        "tau": tau,
        "j0": j0,
    }

    for name, value in parameters.items():
        if not isinstance(value, (int, float, np.number)):
            raise TypeError(f"{name} must be a numeric scalar")

    # Validate the number of cells
    if not isinstance(N, (int, np.integer)) or isinstance(N, bool) or N <= 0:
        raise ValueError(f"N should be a positive integer, got N = {N}")

    # Validate the source width
    if not np.isfinite(tau) or tau <= 0:
        raise ValueError(f"tau should be positive and finite, got tau = {tau}")

    # Validate the source index
    if not isinstance(source_index, (int, np.integer)) or isinstance(
        source_index, bool
    ):
        raise ValueError(
            f"source_index should be an integer, got source_index = {source_index}"
        )

    if source_index < 0 or source_index > N:
        raise ValueError(
            f"source_index is out of range, got source_index = {source_index}"
        )

    # Validate time and source amplitude
    if not np.isfinite(t) or not np.isfinite(t0) or not np.isfinite(j0):
        raise ValueError("t, t0 and j0 must be finite")

    # Calculate the Gaussian current density
    current_density = j0 * np.exp(-(((t - t0) / tau) ** 2))

    # Create the source array at electric field positions
    source = np.zeros(N + 1)
    source[source_index] = current_density

    return source
