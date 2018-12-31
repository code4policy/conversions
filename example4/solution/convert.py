#!/usr/bin/env python3

import csv

with open('input.csv') as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)

# remove rows without BIOGUIDE_ID

filtered_rows = []
for row in all_rows:
    if row['BIOGUIDE_ID']:
        filtered_rows.append(row)

# sum cost by category

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
    writer.writerow(['path', 'size'])

    # write empty row for root
    writer.writerow(['root', ''])

    for category, total_cost in costs_by_category.items():
        path = "root/" + category + ".txt"
        size = total_cost
        new_row = [path, size]
        writer.writerow(new_row)
