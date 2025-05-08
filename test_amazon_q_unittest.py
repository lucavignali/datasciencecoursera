#!/usr/bin/env python3
"""
Unit tests for Amazon Q connectivity testing.
"""

import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import io
import json
from test_amazon_q import test_amazon_q_connection, load_config

class TestAmazonQConnection(unittest.TestCase):
    """Test cases for Amazon Q connectivity."""
    
    @patch('test_amazon_q.load_config')
    @patch('test_amazon_q.boto3.Session')
    def test_amazon_q_available(self, mock_session, mock_load_config):
        """Test when Amazon Q is available and connection succeeds."""
        # Setup mock config
        mock_load_config.return_value = {
            "region": "us-east-1",
            "connection_timeout": 30,
            "retry_attempts": 3
        }
        
        # Setup mock session
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        mock_session_instance.get_available_services.return_value = ['q', 's3', 'ec2']
        mock_client = MagicMock()
        mock_session_instance.client.return_value = mock_client
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the test
        result = test_amazon_q_connection()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Assertions
        self.assertTrue(result)
        self.assertIn("Successfully connected to Amazon Q!", captured_output.getvalue())
        mock_session_instance.client.assert_called_once()
    
    @patch('test_amazon_q.load_config')
    @patch('test_amazon_q.boto3.Session')
    def test_amazon_q_not_available(self, mock_session, mock_load_config):
        """Test when Amazon Q is not available in the region."""
        # Setup mock config
        mock_load_config.return_value = {
            "region": "us-west-1",
            "connection_timeout": 30,
            "retry_attempts": 3
        }
        
        # Setup mock session
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        mock_session_instance.get_available_services.return_value = ['s3', 'ec2']
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the test
        result = test_amazon_q_connection()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Assertions
        self.assertFalse(result)
        self.assertIn("Amazon Q service is not available in the current region", captured_output.getvalue())
    
    @patch('test_amazon_q.load_config')
    @patch('test_amazon_q.boto3.Session')
    def test_credentials_error(self, mock_session, mock_load_config):
        """Test when AWS credentials are not found."""
        # Setup mock config
        mock_load_config.return_value = {
            "region": "us-east-1",
            "connection_timeout": 30,
            "retry_attempts": 3
        }
        
        # Setup mock to raise NoCredentialsError
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        mock_session_instance.get_available_services.side_effect = botocore.exceptions.NoCredentialsError()
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the test
        result = test_amazon_q_connection()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Assertions
        self.assertFalse(result)
        self.assertIn("AWS credentials not found", captured_output.getvalue())
    
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"region": "eu-west-1", "connection_timeout": 60}')
    def test_load_config_file_exists(self, mock_file, mock_exists):
        """Test loading configuration when file exists."""
        mock_exists.return_value = True
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        config = load_config()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        self.assertEqual(config["region"], "eu-west-1")
        self.assertEqual(config["connection_timeout"], 60)
        self.assertIn("Loaded configuration", captured_output.getvalue())
    
    @patch('os.path.exists')
    def test_load_config_file_not_exists(self, mock_exists):
        """Test loading configuration when file doesn't exist."""
        mock_exists.return_value = False
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        config = load_config()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        self.assertEqual(config["region"], "us-east-1")
        self.assertEqual(config["connection_timeout"], 30)
        self.assertEqual(config["retry_attempts"], 3)
        self.assertIn("Configuration file not found", captured_output.getvalue())

if __name__ == '__main__':
    try:
        import botocore.exceptions
        unittest.main()
    except ImportError:
        print("AWS SDK (boto3) is not installed. Please install it using: pip install boto3")
        sys.exit(1)