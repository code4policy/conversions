#!/usr/bin/env python3

import csv
import datetime

# see http://strftime.org/
INPUT_DATE_FORMAT = "%m/%d/%Y"
OUTPUT_DATE_FORMAT = "%-d-%b-%y"

# 1. load input.csv into a variable called `polls`
with open('input.csv') as f:
    reader = csv.DictReader(f)
    polls = list(reader)

# 2a. write a new file called output.csv
with open('output.csv', 'w') as f:
    writer = csv.writer(f)

    # 2b. write a row with two headers: "date" and "approve"
    writer.writerow(['date', 'approve'])

    # 3. Loop through each row of `polls`
    for row in polls:

        # 4a. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
        date = datetime.datetime.strptime(row['enddate'], INPUT_DATE_FORMAT)

        # 4b. convert to output date format
        new_date = date.strftime(OUTPUT_DATE_FORMAT)

        # 5. write a new row of data with the transformed date and value for "approve" 
        writer.writerow([new_date, row['approve']])
