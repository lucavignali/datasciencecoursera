# Makefile for Amazon Q connectivity testing

.PHONY: test check report clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  test    - Run all unit tests"
	@echo "  check   - Run Amazon Q connectivity check"
	@echo "  report  - Generate HTML report"
	@echo "  clean   - Remove generated files"
	@echo "  help    - Show this help message"

# Run all tests
test:
	@echo "Running all unit tests..."
	python -m unittest discover -p "test_*.py"

# Run connectivity check
check:
	@echo "Checking Amazon Q connectivity..."
	./check_amazon_q.sh

# Generate HTML report
report:
	@echo "Generating Amazon Q connectivity report..."
	./check_amazon_q.sh --report

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	rm -f amazon_q_report.html
	@echo "Done."