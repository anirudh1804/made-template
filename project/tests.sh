#!/bin/bash

# Exit on error
set -e

# Define paths
OUTPUT_FILE="./main/project/pipeline.py"

# rm -f "$OUTPUT_FILE"

# Validate that the output file exists
if [ -e "$OUTPUT_FILE" ]; then
    echo "Test passed: Output file exists."
else
    echo "Test failed: Output file does not exist."
    exit 1
fi
# rm -f "$OUTPUT_FILE"

# Test passed
echo "All tests passed!"
exit 0
