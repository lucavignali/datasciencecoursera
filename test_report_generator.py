#!/usr/bin/env python3
"""
Unit tests for the HTML report generator.
"""

import unittest
import os
import tempfile
from unittest.mock import patch, MagicMock
import sys
from generate_report import generate_html_report

class TestReportGenerator(unittest.TestCase):
    """Test cases for the HTML report generator."""
    
    def test_report_generation(self):
        """Test that the report is generated correctly."""
        # Create a temporary file for the report
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            # Test data
            is_connected = True
            config = {
                "region": "us-west-2",
                "connection_timeout": 45,
                "retry_attempts": 5,
                "log_level": "DEBUG",
                "features": {
                    "code_suggestions": True,
                    "documentation_search": False
                }
            }
            
            # Generate the report
            report_path = generate_html_report(is_connected, config, temp_path)
            
            # Check that the file exists
            self.assertTrue(os.path.exists(report_path))
            
            # Check the content of the report
            with open(report_path, 'r') as f:
                content = f.read()
                
                # Check for key elements
                self.assertIn("Amazon Q Connection Report", content)
                self.assertIn("CONNECTED", content)
                self.assertIn("us-west-2", content)
                self.assertIn("45", content)
                self.assertIn("Code Suggestions", content)
                self.assertIn("Enabled", content)
                self.assertIn("Documentation Search", content)
                self.assertIn("Disabled", content)
        
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_report_disconnected_status(self):
        """Test that the report shows disconnected status correctly."""
        # Create a temporary file for the report
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            # Test data for disconnected status
            is_connected = False
            config = {
                "region": "eu-central-1",
                "connection_timeout": 30
            }
            
            # Generate the report
            report_path = generate_html_report(is_connected, config, temp_path)
            
            # Check the content of the report
            with open(report_path, 'r') as f:
                content = f.read()
                
                # Check for disconnected status
                self.assertIn("DISCONNECTED", content)
                self.assertIn("eu-central-1", content)
        
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)

if __name__ == '__main__':
    unittest.main()