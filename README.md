datasciencecoursera
===================

Data Science Course Repo

## Amazon Q Integration

This repository includes tools to test Amazon Q connectivity:

### Quick Start

The repository includes a Makefile for common operations:

```bash
# Show available commands
make help

# Run all unit tests
make test

# Check Amazon Q connectivity
make check

# Generate HTML report
make report

# Clean up generated files
make clean
```

### Configuration

The Amazon Q connection settings can be configured in the `amazon_q_config.json` file:

```json
{
    "region": "us-east-1",
    "connection_timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO",
    "features": {
        "code_suggestions": true,
        "documentation_search": true,
        "security_scanning": true
    }
}
```

You can modify these settings to match your AWS environment.

### Testing Amazon Q Connection

To test if Amazon Q is properly connected, you can use either:

#### Option 1: Using the shell script (recommended)

```bash
chmod +x check_amazon_q.sh
./check_amazon_q.sh
```

The shell script supports the following options:

```
Usage: ./check_amazon_q.sh [options]
Options:
  -r, --report    Generate HTML report
  -o, --output    Specify output path for report (default: amazon_q_report.html)
  -h, --help      Show this help message
```

Examples:
```bash
# Run basic connectivity test
./check_amazon_q.sh

# Generate HTML report with default filename
./check_amazon_q.sh --report

# Generate HTML report with custom filename
./check_amazon_q.sh --report --output custom_report.html
```

This script will automatically check for dependencies and run the test.

#### Option 2: Running the Python script directly

```bash
python test_amazon_q.py
```

This script will verify if:
1. AWS SDK (boto3) is installed
2. Amazon Q service is available in your region
3. Your AWS credentials are properly configured
4. You can successfully connect to Amazon Q

### Running Unit Tests

To run the unit tests for Amazon Q connectivity:

```bash
python test_amazon_q_unittest.py
```

To test the HTML report generator:

```bash
python test_report_generator.py
```

To run all tests:

```bash
python -m unittest discover -p "test_*.py"
```

### Generating HTML Reports

You can generate a detailed HTML report of the Amazon Q connection status:

```bash
python generate_report.py [output_path]
```

The report includes:
- Connection status
- Configuration settings
- Enabled features
- System information

By default, the report is saved as `amazon_q_report.html` in the current directory.

### Prerequisites

- Python 3.6+
- AWS SDK for Python (boto3): `pip install boto3`
- Configured AWS credentials with appropriate permissions for Amazon Q
