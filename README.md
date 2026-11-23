# Electromagnetism Simulator

A Python-based numerical simulator for studying and visualizing electromagnetic wave propagation using the Finite-Difference Time-Domain (FDTD) method.

## Overview

This project implements a one-dimensional (1D) electromagnetic simulator based on Maxwell's equations. It uses the Finite-Difference Time-Domain (FDTD) method to calculate the time evolution of electric and magnetic fields in space.

The current implementation models electromagnetic wave propagation in a homogeneous, isotropic, linear, and lossless medium.

## Numerical Method

The simulator uses the Yee scheme to discretize Maxwell's equations in both space and time.

Key features include:
- One-dimensional electromagnetic wave propagation.
- Staggered spatial and temporal grids for electric and magnetic fields.
- Gaussian current-density source.
- First-order Mur absorbing boundary conditions.
- Monitoring of electric, magnetic, and total field energy.
- Field propagation and energy visualization.

The time step is constrained by the Courant-Friedrichs-Lewy (CFL) stability condition.

## Project Structure

```text
electromagnetism-simulator/
├── docs/
│   ├── theory/               # Theoretical foundations
│   └── numerical_methods/    # FDTD numerical methods
├── src/
│   ├── fdtd/
│   │   ├── fields.py         # Field initialization
│   │   ├── grid.py            # Spatial grid generation
│   │   ├── source.py          # Gaussian source
│   │   ├── update.py          # Field updates and boundary conditions
│   │   ├── simulation.py      # Main simulation loop
│   │   └── visualization.py   # Field and energy plots
│   ├── tests/                 # Unit tests
│   └── main.py                # Simulation entry point
└── README.md
```

## Technologies

- Python
- NumPy
- Matplotlib
- pytest
- Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/victorkaradjov/electromagnetism-simulator.git
cd electromagnetism-simulator
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install numpy matplotlib pytest
```

## Running the Simulation

From the project root, set the source directory in the Python path:

```powershell
$env:PYTHONPATH = "$PWD\src"
python .\src\main.py
```

The simulation will run and display plots of electromagnetic field propagation and field energy over time.

## Running the Tests

From the project root:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m pytest src/tests/ -v
```

## Current Status

The first working version of the 1D FDTD solver has been implemented.

The current focus is on:
- Reviewing and validating the theoretical and numerical foundations.
- Improving the implementation and its test coverage.
- Refining the simulation and visualization tools.

## Future Goals

- Extend the solver to two-dimensional (2D) electromagnetic simulations.
- Explore different material properties and electromagnetic configurations.
- Implement additional absorbing boundary conditions.
- Investigate more advanced electromagnetic phenomena and numerical methods.

## Author

**Victor Karadjov**  
Physical Engineering Student — Polytechnique Montréal

[GitHub Profile](https://github.com/victorkaradjov)