#!/usr/bin/env python3

import os
import re
import argparse
import sys

parser = argparse.ArgumentParser(prog="scattergories.py", description="A program to tell you what category a word is in")
parser.add_argument("query", help="The word you want to know the category of", type=str)
parser.add_argument("--categorydir", default='categories',help="The directory of category files", type=str)
args = parser.parse_args()
query = args.query

category_data = {}
for file in os.listdir(args.categorydir):
    print(file)
    # add code here to read in files and assign the terms to a category in the dictionary


print(f'What category is {query} in?')
# add code to print out what the query category is in, AND/OR print out "Unknown" for the category"
category = "Unknown"
print(category)
