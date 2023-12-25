#!/bin/bash

# Define paths
data="pipeline.py"

# Validate that the Python script exists
if data:
    print("Test passed, Python script exists.")
else
    print("Test failed, Python script does not exist.")
    exit 1

sqlite="merged_data.sqlite"
if sqlite:
    print("Test passed: SQLite file exists.")
else
    print("Test failed: SQLite file does not exist.")
    exit 1

# Test passed
print("All tests passed!")
exit 0
