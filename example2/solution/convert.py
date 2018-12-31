#!/usr/bin/env python3

import json
import csv

with open('input.json') as f:
    data = json.load(f)

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'value'])

    # converting only top level of children
    for row in data['children']:

        # create id for visualization
        id_ = 'flare.other.' + row['name'].replace(' ', '')

        # remove dollar sign and comma from budget
        budget = row['data']['budget'].replace('$', '').replace(',', '')

        writer.writerow([id_, budget])
