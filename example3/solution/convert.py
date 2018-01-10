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

costs_by_category = defaultdict(list)
for row in filtered_rows:
    category = row['CATEGORY']
    amount = float(row['AMOUNT'])
    costs_by_category[category].append(amount)

# sum each group and write output

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'value'])

    for category, amounts in costs_by_category.items():
        new_row = ["flare.other." + category, sum(amounts)]
        writer.writerow(new_row)
