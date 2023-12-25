#!/bin/bash

# Define paths
import os
data="pipeline.py"

# Validate that the Python script exists
if os.path.exists(data):
    print("Test passed, Python script exists.")
else:
    print("Test failed, Python script does not exist.")
    exit()

sqlite="merged_data.sqlite"
if os.path.exists(sqlite):
    print("Test passed: SQLite file exists.")
else:
    print("Test failed: SQLite file does not exist.")
    exit()

# Test passed
print("All tests passed!")
exit()
