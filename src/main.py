from fdtd.grid import cell_num
from fdtd.simulation import run_simulation
from fdtd.visualization import plot_energy, plot_fields, show_plots

# Spatial parameters
domain_length = 1.0
spatial_step = 0.001

# Physical properties: vacuum
permittivity = 8.8541878128e-12
permeability = 1.25663706212e-6

# Time-step parameters
cfl_number = 0.99
num_time_steps = 1000

# Source parameters
source_center_time = 0.5e-9
source_width = 0.1e-9
source_amplitude = 1.0

# Calculate the number of cells and source position
num_cells = cell_num(domain_length, spatial_step)
source_position_index = num_cells // 2

# Run the FDTD simulation
results = run_simulation(
    domain_length=domain_length,
    spatial_step=spatial_step,
    permittivity=permittivity,
    permeability=permeability,
    cfl_number=cfl_number,
    num_time_steps=num_time_steps,
    source_center_time=source_center_time,
    source_width=source_width,
    source_amplitude=source_amplitude,
    source_position_index=source_position_index,
)

# Display simulation information
print(f"Wave speed: {results['wave_speed']:.3e} m/s")
print(f"Time step: {results['time_step']:.3e} s")
print(f"Simulation duration: {num_time_steps * results['time_step']:.3e} s")
print(f"Number of spatial cells: {results['num_cells']}")

# Display simulation results
plot_fields(results)
plot_energy(results)
show_plots()
