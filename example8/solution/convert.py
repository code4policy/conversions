#!/usr/bin/env python3

import csv
import datetime

# see http://strftime.org/
INPUT_DATE_FORMAT = "%m/%d/%Y"
OUTPUT_DATE_FORMAT = "%Y-%m-%d"

with open('input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in rows:
        row['modeldate'] = datetime.datetime.strptime(row['modeldate'], INPUT_DATE_FORMAT)

# sort by date, ascending
rows = sorted(rows, key=lambda x: x['modeldate'])

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['year','variableA','variableB','variableC','variableD', 'variableE', 'variableF'])

    for row in rows:
        writer.writerow([
            row['modeldate'].strftime(OUTPUT_DATE_FORMAT),
            row['approve_estimate'],
            row['disapprove_estimate'],
            row['approve_hi'],
            row['approve_lo'],
            row['disapprove_hi'],
            row['disapprove_lo']
        ])

