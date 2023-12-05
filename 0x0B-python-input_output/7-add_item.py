#!/usr/bin/python3
""" module """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Get all arguments passed to the script
arguments = sys.argv[1:]

# Check if the file exists, load data if it does
existing_data = []
try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

# Combine existing data with new arguments
combined_data = existing_data + arguments

# Save the combined data to the file
save_to_json_file("add_item.json", combined_data)
