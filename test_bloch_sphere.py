#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for the Bloch sphere visualization functionality.
"""

import unittest
import numpy as np
import matplotlib.pyplot as plt
from bloch_sphere import plot_bloch_sphere

class TestBlochSphere(unittest.TestCase):
    """Test cases for the Bloch sphere visualization function."""
    
    def test_plot_creation(self):
        """Test that the plot is created successfully."""
        fig = plot_bloch_sphere(np.pi/2, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
    
    def test_invalid_theta(self):
        """Test handling of invalid theta values."""
        # Theta should be between 0 and pi
        # The function should still work but might not give expected results
        fig = plot_bloch_sphere(-0.5, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        fig = plot_bloch_sphere(3*np.pi, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
    
    def test_common_states(self):
        """Test visualization of common quantum states."""
        # |0⟩ state
        fig = plot_bloch_sphere(0, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        # |1⟩ state
        fig = plot_bloch_sphere(np.pi, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        # |+⟩ state
        fig = plot_bloch_sphere(np.pi/2, 0)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        # |-⟩ state
        fig = plot_bloch_sphere(np.pi/2, np.pi)
        self.assertIsNotNone(fig)
        plt.close(fig)
    
    def test_optional_parameters(self):
        """Test the optional parameters of the function."""
        # Test with show_angles=False
        fig = plot_bloch_sphere(np.pi/4, np.pi/4, show_angles=False)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        # Test with show_vector_components=False
        fig = plot_bloch_sphere(np.pi/4, np.pi/4, show_vector_components=False)
        self.assertIsNotNone(fig)
        plt.close(fig)
        
        # Test with custom figsize
        fig = plot_bloch_sphere(np.pi/4, np.pi/4, figsize=(8, 8))
        self.assertIsNotNone(fig)
        plt.close(fig)

if __name__ == '__main__':
    unittest.main()