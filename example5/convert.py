#!/usr/bin/env python3

import json
import datetime

# load input.json using json.load into a variable called 'legislators'

# loop through the legislators and calculate the total number of days each
# legislator has been in congress

# to parse dates, use datetime.datetime.strptime, see http://strftime.org/
# hint: datetime.datetime.strptime(term['start'], "%Y-%m-%d")

# to get number of days, subtract two datetime objects and then put `.days` at the end
# hint: (date2-date1).days

# for each legislator output an object that looks like
# {"name": ..., "value": ....}
# where value is the number of days they have been in congress

# write to output.json using json.dump
