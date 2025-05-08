#!/bin/bash
# Script to check Amazon Q connectivity and generate reports

# Default values
GENERATE_REPORT=false
REPORT_PATH="amazon_q_report.html"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -r|--report)
            GENERATE_REPORT=true
            shift
            ;;
        -o|--output)
            REPORT_PATH="$2"
            shift
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  -r, --report    Generate HTML report"
            echo "  -o, --output    Specify output path for report (default: amazon_q_report.html)"
            echo "  -h, --help      Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

echo "Checking Amazon Q connectivity..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 to run this test."
    exit 1
fi

# Check if boto3 is installed
python3 -c "import boto3" &> /dev/null
if [ $? -ne 0 ]; then
    echo "AWS SDK (boto3) is not installed. Installing now..."
    pip install boto3 || pip3 install boto3
    if [ $? -ne 0 ]; then
        echo "Failed to install boto3. Please install it manually: pip install boto3"
        exit 1
    fi
fi

# Generate report if requested
if [ "$GENERATE_REPORT" = true ]; then
    echo "Generating HTML report at: $REPORT_PATH"
    python3 generate_report.py "$REPORT_PATH"
    exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        echo "✅ Test completed successfully. Amazon Q is connected."
        echo "Report generated at: $REPORT_PATH"
    else
        echo "❌ Test failed. Amazon Q is not connected."
        echo "Report generated at: $REPORT_PATH"
    fi
else
    # Run the Amazon Q connectivity test without report
    python3 test_amazon_q.py
    exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        echo "✅ Test completed successfully. Amazon Q is connected."
    else
        echo "❌ Test failed. Amazon Q is not connected."
    fi
fi

exit $exit_code