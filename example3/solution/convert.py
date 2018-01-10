#!/usr/bin/env python2

import csv

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

costs_by_category = {}
for row in filtered_rows:
    category = row['CATEGORY']
    amount = float(row['AMOUNT'])
    if category in costs_by_category:
        costs_by_category[category] += amount
    else:
        costs_by_category[category] = amount

# write output

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'value'])

    for category, total_cost in costs_by_category.items():
        new_row = ["flare.other." + category, total_cost]
        writer.writerow(new_row)
