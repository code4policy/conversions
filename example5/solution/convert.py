#!/usr/bin/env python3

import json
import datetime

with open('input.json') as f:
    legislators = json.load(f)

output = []

for legislator in legislators:
    name = legislator['name']['official_full']
    first_term = legislator['terms'][0]
    last_term = legislator['terms'][-1]
    start = datetime.datetime.strptime(first_term['start'], "%Y-%m-%d")
    end = datetime.datetime.strptime(last_term['end'], "%Y-%m-%d")
    length = (end-start).days
    output.append({"name": name, "value": length})

# sort by "value", descending, take the top 20
output = sorted(output, key=lambda x: x['value'], reverse=True)[:20]

with open('output.json', 'w') as f:
    json.dump(output, f)
