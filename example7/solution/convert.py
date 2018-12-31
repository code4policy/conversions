#!/usr/bin/env python3

import csv
import datetime

# see http://strftime.org/
INPUT_DATE_FORMAT = "%m/%d/%Y"
OUTPUT_DATE_FORMAT = "%-d-%b-%y"

with open('input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('output.csv', 'w') as f:
    writer = csv.writer(f)

    # write csv header
    writer.writerow(['date', 'close'])

    for row in rows:
        
        # parse raw date
        parsed_date = datetime.datetime.strptime(row['enddate'], INPUT_DATE_FORMAT)

        # convert to output date format
        output_date = parsed_date.strftime(OUTPUT_DATE_FORMAT)

        # write row: date, approval
        writer.writerow([output_date, row['approve']])
