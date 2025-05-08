# Quantum Computing Visualization Tools

This repository contains tools for quantum computing visualizations, including a Bloch sphere representation tool.

## Bloch Sphere Visualization

The `bloch_sphere.py` module provides functionality to visualize quantum states on a Bloch sphere using the angles theta and phi in radians.

### Installation

This tool requires the following Python packages:
- numpy
- matplotlib

You can install them using pip:
```bash
pip install numpy matplotlib
```

### Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from bloch_sphere import plot_bloch_sphere

# Example: Plot state |+⟩ (theta=π/2, phi=0)
plot_bloch_sphere(np.pi/2, 0)
plt.show()
```

### Examples

Check out the `bloch_sphere_examples.ipynb` Jupyter notebook for more examples and interactive visualizations.

### Function Parameters

- `theta`: The polar angle from the z-axis (0 to π radians)
- `phi`: The azimuthal angle in the x-y plane (0 to 2π radians)
- `show_angles`: Whether to display the angle values on the plot (default is True)
- `show_vector_components`: Whether to display the vector components (default is True)
- `figsize`: Figure size as (width, height) in inches (default is (10, 10))

### Testing

Run the tests using:
```bash
python -m unittest test_bloch_sphere.py
```
