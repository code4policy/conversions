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

cost_by_category = defaultdict(list)
for row in filtered_rows:
    category = row['CATEGORY']
    amount = float(row['AMOUNT'])
    cost_by_category[category].append(amount)

# sum each group

outputs = []
for category, amounts in grouped_rows.items():
    outputs.append({
        "id": "flare.other." + category,
        "value": sum(amounts)
        })

with open('output.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'value'])
    writer.writeheader()
    writer.writerows(outputs)
