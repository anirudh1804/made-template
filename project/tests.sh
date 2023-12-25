#!/bin/bash

# Exit on error
set -e

# Define paths
data="C:\\Users\\zucky\\OneDrive\\Desktop\\made-template\\project\\pipeline.py"

# Validate that the Python script exists
if [ -e "$data" ]; then
    echo "Test passed, Python script exists."
else
    echo "Test failed, Python script does not exist."
    exit 1
fi

SQLITE_FILE="C:\Users\zucky\OneDrive\Desktop\made-template\project\merged_data.sqlite"
if [ -e "$SQLITE_FILE" ]; then
    echo "Test passed: SQLite file exists."
else
    echo "Test failed: SQLite file does not exist."
    exit 1
fi

# Test passed
echo "All tests passed!"
exit 0
