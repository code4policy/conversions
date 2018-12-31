#!/usr/bin/env python3

import json
import csv

# use json.load to load input.json. load it into a variable called 'data'

# use open to open 'output.csv' in write mode
# use csv.writer to create writer using the opened file
# write the header of the csv

# loop through the top level children data['children']
# use writer.writerow to write one row at a time with the name and budget
# - prepend 'flare.other.' to each name
# - remove any spaces in the name
