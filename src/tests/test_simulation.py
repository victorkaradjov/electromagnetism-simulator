from fdtd.simulation import run_simulation


def test_run_simulation_shapes():
    results = run_simulation(
        domain_length=1.0,
        spatial_step=0.1,
        permittivity=8.8541878128e-12,
        permeability=1.25663706212e-6,
        cfl_number=0.99,
        num_time_steps=5,
        source_center_time=1e-9,
        source_width=0.1e-9,
        source_amplitude=1.0,
        source_position_index=5,
    )

    assert results["num_cells"] == 10
    assert results["field_snapshots"].shape == (5, 11)
    assert results["magnetic_snapshots"].shape == (5, 10)
    assert results["snapshot_times"].shape == (5,)
    assert results["magnetic_snapshot_times"].shape == (5,)
    assert results["electric_energy"].shape == (5,)
    assert results["magnetic_energy"].shape == (5,)
    assert results["total_energy"].shape == (5,)