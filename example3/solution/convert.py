#!/usr/bin/env python2

import csv
from collections import defaultdict

with open('input.csv') as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)

# filter rows

filtered_rows = []
for row in all_rows:
    if not row['BIOGUIDE_ID']:
        continue
    filtered_rows.append(row)

# group by category

grouped_rows = defaultdict(list)
for row in filtered_rows:
    category = row['CATEGORY']
    grouped_rows[category].append(row)

# sum each group

category_sum = []
for category, rows in grouped_rows.items():

    row_sum = 0
    for row in rows:
        row_sum += float(row['AMOUNT'])

    category_sum.append({
        "id": "flare.other." + category,
        "value": row_sum
        })

with open('output.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'value'])
    writer.writeheader()
    writer.writerows(category_sum)
