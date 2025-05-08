#!/usr/bin/env python3
"""
Generate an HTML report for Amazon Q connectivity status.
"""

import os
import sys
import json
import datetime
from test_amazon_q import test_amazon_q_connection, load_config

def generate_html_report(is_connected, config, output_path="amazon_q_report.html"):
    """
    Generate an HTML report showing the Amazon Q connection status.
    
    Args:
        is_connected (bool): Whether Amazon Q is connected
        config (dict): Configuration settings
        output_path (str): Path to save the HTML report
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get system info
    import platform
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
    }
    
    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amazon Q Connection Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .status {{
            text-align: center;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            font-size: 24px;
            font-weight: bold;
        }}
        .connected {{
            background-color: #d4edda;
            color: #155724;
        }}
        .disconnected {{
            background-color: #f8d7da;
            color: #721c24;
        }}
        .section {{
            margin-bottom: 30px;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
        }}
        h2 {{
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            font-size: 12px;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Amazon Q Connection Report</h1>
        <p>Generated on: {timestamp}</p>
    </div>
    
    <div class="status {'connected' if is_connected else 'disconnected'}">
        {'✅ CONNECTED' if is_connected else '❌ DISCONNECTED'}
    </div>
    
    <div class="section">
        <h2>Configuration</h2>
        <table>
            <tr>
                <th>Setting</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Region</td>
                <td>{config.get('region', 'us-east-1')}</td>
            </tr>
            <tr>
                <td>Connection Timeout</td>
                <td>{config.get('connection_timeout', 30)} seconds</td>
            </tr>
            <tr>
                <td>Retry Attempts</td>
                <td>{config.get('retry_attempts', 3)}</td>
            </tr>
            <tr>
                <td>Log Level</td>
                <td>{config.get('log_level', 'INFO')}</td>
            </tr>
        </table>
    </div>
    
    <div class="section">
        <h2>Features</h2>
        <table>
            <tr>
                <th>Feature</th>
                <th>Status</th>
            </tr>
"""
    
    # Add features from config if available
    features = config.get('features', {})
    if features:
        for feature, enabled in features.items():
            feature_name = feature.replace('_', ' ').title()
            html_content += f"""
            <tr>
                <td>{feature_name}</td>
                <td>{'Enabled' if enabled else 'Disabled'}</td>
            </tr>"""
    else:
        html_content += """
            <tr>
                <td colspan="2">No feature information available</td>
            </tr>"""
    
    # Continue with system info
    html_content += f"""
        </table>
    </div>
    
    <div class="section">
        <h2>System Information</h2>
        <table>
            <tr>
                <th>Item</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Operating System</td>
                <td>{system_info['os']}</td>
            </tr>
            <tr>
                <td>OS Version</td>
                <td>{system_info['os_version']}</td>
            </tr>
            <tr>
                <td>Python Version</td>
                <td>{system_info['python_version']}</td>
            </tr>
        </table>
    </div>
    
    <div class="footer">
        <p>This report was automatically generated by the Amazon Q Connection Test Tool.</p>
    </div>
</body>
</html>
"""
    
    # Write the HTML file
    with open(output_path, 'w') as f:
        f.write(html_content)
    
    print(f"Report generated at: {os.path.abspath(output_path)}")
    return os.path.abspath(output_path)

if __name__ == "__main__":
    print("Testing Amazon Q connectivity...")
    config = load_config()
    is_connected = test_amazon_q_connection()
    
    output_path = "amazon_q_report.html"
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    
    report_path = generate_html_report(is_connected, config, output_path)
    
    print(f"Connection status: {'Connected' if is_connected else 'Disconnected'}")
    print(f"Report available at: {report_path}")
    
    sys.exit(0 if is_connected else 1)