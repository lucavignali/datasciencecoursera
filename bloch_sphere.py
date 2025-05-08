#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bloch Sphere Visualization Module

This module provides functionality to visualize quantum states on a Bloch sphere
using the angles theta and phi in radians.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot_bloch_sphere(theta, phi, show_angles=True, show_vector_components=True, figsize=(10, 10)):
    """
    Plot a Bloch sphere with a state vector defined by angles theta and phi.
    
    Parameters:
    -----------
    theta : float
        The polar angle from the z-axis (0 to π radians)
    phi : float
        The azimuthal angle in the x-y plane (0 to 2π radians)
    show_angles : bool, optional
        Whether to display the angle values on the plot (default is True)
    show_vector_components : bool, optional
        Whether to display the vector components (default is True)
    figsize : tuple, optional
        Figure size as (width, height) in inches (default is (10, 10))
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure object containing the plot
    
    Notes:
    ------
    The quantum state represented is:
    |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
    
    Examples:
    ---------
    >>> plot_bloch_sphere(np.pi/4, np.pi/2)  # 45° from z-axis, 90° in x-y plane
    """
    # Create figure and 3D axis
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    # Draw the Bloch sphere (wireframe)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot the Bloch sphere with slight transparency
    ax.plot_surface(x, y, z, color='b', alpha=0.1)
    
    # Add wireframe for better visibility
    ax.plot_wireframe(x, y, z, color='b', alpha=0.1, rstride=10, cstride=10)
    
    # Draw the main axes
    axes_length = 1.3
    ax.quiver(0, 0, 0, axes_length, 0, 0, color='r', arrow_length_ratio=0.1, label='X')
    ax.quiver(0, 0, 0, 0, axes_length, 0, color='g', arrow_length_ratio=0.1, label='Y')
    ax.quiver(0, 0, 0, 0, 0, axes_length, color='b', arrow_length_ratio=0.1, label='Z')
    
    # Add axis labels
    ax.text(axes_length + 0.1, 0, 0, "X", color='r')
    ax.text(0, axes_length + 0.1, 0, "Y", color='g')
    ax.text(0, 0, axes_length + 0.1, "Z", color='b')
    
    # Add |0⟩ and |1⟩ state labels
    ax.text(0, 0, 1.1, "$|0\\rangle$", fontsize=15)
    ax.text(0, 0, -1.1, "$|1\\rangle$", fontsize=15)
    
    # Calculate the Cartesian coordinates of the state vector
    x_vec = np.sin(theta) * np.cos(phi)
    y_vec = np.sin(theta) * np.sin(phi)
    z_vec = np.cos(theta)
    
    # Draw the state vector
    ax.quiver(0, 0, 0, x_vec, y_vec, z_vec, color='purple', arrow_length_ratio=0.15, linewidth=3)
    
    # Draw projection lines to the axes (optional)
    ax.plot([0, x_vec], [0, 0], [0, 0], 'r--', alpha=0.5)  # x-projection
    ax.plot([x_vec, x_vec], [0, y_vec], [0, 0], 'g--', alpha=0.5)  # y-projection
    ax.plot([x_vec, x_vec], [y_vec, y_vec], [0, z_vec], 'b--', alpha=0.5)  # z-projection
    
    # Calculate quantum state components
    alpha = np.cos(theta/2)
    beta = np.exp(1j * phi) * np.sin(theta/2)
    
    # Display angle values
    if show_angles:
        ax.text(1.5, 0, 0, f"θ = {theta:.2f} rad ({np.degrees(theta):.1f}°)", fontsize=12)
        ax.text(1.5, 0, -0.2, f"φ = {phi:.2f} rad ({np.degrees(phi):.1f}°)", fontsize=12)
    
    # Display vector components
    if show_vector_components:
        state_text = f"$|\\psi\\rangle = {alpha:.3f}|0\\rangle + {beta:.3f}|1\\rangle$"
        state_text = state_text.replace('+-', '-')  # Fix negative sign display
        ax.text(1.5, 0, -0.4, state_text, fontsize=12)
        ax.text(1.5, 0, -0.6, f"$|\\alpha|^2 = {np.abs(alpha)**2:.3f}, |\\beta|^2 = {np.abs(beta)**2:.3f}$", fontsize=12)
    
    # Set plot limits and labels
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    
    ax.set_title("Bloch Sphere Representation", fontsize=16)
    
    # Remove background grid and pane for cleaner look
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Hide axes ticks for cleaner visualization
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    plt.tight_layout()
    
    return fig

# Example usage in a Jupyter notebook:
# ```python
# import numpy as np
# from bloch_sphere import plot_bloch_sphere
# 
# # Example: Plot state |+⟩ (theta=π/2, phi=0)
# plot_bloch_sphere(np.pi/2, 0)
# plt.show()
# ```