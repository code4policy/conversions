#!/usr/bin/env python2

import re
import json
import requests
import execjs

response = requests.get("https://obamawhitehouse.archives.gov//interactive-budget")
m = re.search(r"//init data(.*)//init TreeMap", response.text, re.S)
js = m.groups()[0].replace('var json = ', '').replace(';', '')
data = execjs.eval(js)

with open('input.json', 'w') as f:
    json.dump(data, f, indent=4)
