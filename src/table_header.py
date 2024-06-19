"""
This script prints the header of the table file to understand its structure"""

import re, json

# Define the path of the input file
input_file_path = "c:/Users/Paul CoW/Documents/MEVBlocker/Agnostic_relay/table"


# Open the input file in read mode
with open(input_file_path, "r") as input_file:
    # Read all the lines from the input file
    lines = input_file.readlines()

    # Iterate over each line
    i=0
    for line in lines:
        a = re.split(' |\t', line.strip())
        # Check if the line meets the criteria
        if i<=58:
            print(a)
        if i>58:
            break
        i+=1