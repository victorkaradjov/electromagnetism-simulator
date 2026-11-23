import matplotlib.pyplot as plt


def plot_fields(results):
    # Extract simulation results
    electric_grid = results["electric_grid"]
    magnetic_grid = results["magnetic_grid"]

    snapshot_times = results["snapshot_times"]
    magnetic_snapshot_times = results["magnetic_snapshot_times"]

    field_snapshots = results["field_snapshots"]
    magnetic_snapshots = results["magnetic_snapshots"]

    # Plot electric field
    plt.figure(figsize=(10, 5))
    plt.pcolormesh(
        electric_grid,
        snapshot_times,
        field_snapshots,
        shading="auto",
        cmap="RdBu_r",
    )
    plt.colorbar(label="Electric field Ex (V/m)")
    plt.xlabel("Position z (m)")
    plt.ylabel("Time (s)")
    plt.title("Electric field propagation")
    plt.tight_layout()

    # Plot magnetic field
    plt.figure(figsize=(10, 5))
    plt.pcolormesh(
        magnetic_grid,
        magnetic_snapshot_times,
        magnetic_snapshots,
        shading="auto",
        cmap="RdBu_r",
    )
    plt.colorbar(label="Magnetic field Hy (A/m)")
    plt.xlabel("Position z (m)")
    plt.ylabel("Time (s)")
    plt.title("Magnetic field propagation")
    plt.tight_layout()


def plot_energy(results):
    # Extract energy data
    snapshot_times = results["snapshot_times"]

    electric_energy = results["electric_energy"]
    magnetic_energy = results["magnetic_energy"]
    total_energy = results["total_energy"]

    # Plot electromagnetic energy
    plt.figure(figsize=(10, 5))
    plt.plot(snapshot_times, electric_energy, label="Electric energy")
    plt.plot(snapshot_times, magnetic_energy, label="Magnetic energy")
    plt.plot(snapshot_times, total_energy, label="Total energy")

    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.title("Electromagnetic energy")
    plt.legend()
    plt.grid()
    plt.tight_layout()


def show_plots():
    plt.show()
