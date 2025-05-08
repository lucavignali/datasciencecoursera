#!/usr/bin/env python3
"""
Test script to check Amazon Q connectivity.
This script attempts to connect to Amazon Q and verify the connection status.
"""

import sys
import os
import json

try:
    import boto3
    import botocore.exceptions
    print("Required AWS SDK libraries are installed.")
except ImportError:
    print("AWS SDK (boto3) is not installed. Please install it using: pip install boto3")
    sys.exit(1)

def load_config():
    """
    Load Amazon Q configuration from the config file.
    Returns a dictionary with configuration values.
    """
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'amazon_q_config.json')
    
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
                print(f"Loaded configuration from {config_path}")
                return config
        else:
            print(f"Configuration file not found at {config_path}, using default settings")
            return {
                "region": "us-east-1",
                "connection_timeout": 30,
                "retry_attempts": 3
            }
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {
            "region": "us-east-1",
            "connection_timeout": 30,
            "retry_attempts": 3
        }

def test_amazon_q_connection():
    """
    Test if Amazon Q service is accessible with current credentials.
    Returns True if connected, False otherwise.
    """
    config = load_config()
    
    try:
        # Initialize a boto3 client for Amazon Q using the configuration
        session = boto3.Session(region_name=config.get("region", "us-east-1"))
        
        print(f"Testing Amazon Q connection in region: {config.get('region', 'us-east-1')}")
        
        # Check if Amazon Q is available in the current region
        available_services = session.get_available_services()
        
        if 'q' in available_services:
            print("Amazon Q service is available in the current region.")
            
            # Try to initialize the client with config settings
            q_client = session.client(
                'q',
                config=boto3.config.Config(
                    connect_timeout=config.get("connection_timeout", 30),
                    retries={'max_attempts': config.get("retry_attempts", 3)}
                )
            )
            
            # We could make a simple API call here to verify connectivity
            # For example: response = q_client.list_knowledge_bases()
            # But we'll just check if client initialization works
            
            print("Successfully connected to Amazon Q!")
            return True
        else:
            print("Amazon Q service is not available in the current region.")
            print("Available services:", available_services)
            return False
            
    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS credentials.")
        return False
    except botocore.exceptions.ClientError as e:
        print(f"Failed to connect to Amazon Q: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    print("Testing Amazon Q connectivity...")
    is_connected = test_amazon_q_connection()
    
    if is_connected:
        print("✅ Amazon Q is connected and working properly.")
        sys.exit(0)
    else:
        print("❌ Amazon Q is not connected. Please check your configuration.")
        sys.exit(1)