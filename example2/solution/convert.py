#!/usr/bin/env python2

import json
import csv

with open('input.json') as f:
    data = json.load(f)

with open('output.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'value'])
    writer.writeheader()

    # converting only top level of children
    for row in data['children']:

        # create id for visualization
        id_ = 'flare.other.' + row['name'].replace(' ', '')

        # remove dollar sign and comma from budget
        budget = row['data']['budget'].replace('$', '').replace(',', '')

        writer.writerow({'id': id_, 'value': budget})
