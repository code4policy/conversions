#!/usr/bin/env python3

import csv
import json

# use csv.DictReader to load input.csv
# create a variable 'rows' with all of the rows in the csv

# loop through each row of the input which is in the format

# {
#   'title': ..., 
#   'subtitle': ..., 
#   'range_min': ..., 
#   'range_mid': ..., 
#   'range_max': ..., 
#   'measure_min': ..., 
#   'measure_max': ...
# }

# and transform it into the format

# {
#  'title': ...,
#  'subtitle': ...,
#  'ranges': [...],
#  'measures': [...],
#  'markers': [...],
# }

# use json.dump to output, 'output.json'
