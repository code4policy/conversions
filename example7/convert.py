#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable `rows`

# 2. open output.csv and create a `csv.writer`

# 3. write csv header with columns: "date" and "close"

# (use https://strftime.org/ to create the input/output date formats for the next two steps)

# for each row

    # 4. parse raw `enddate`: you can parse the `enddate` column using the datetime.datetime.strptime function
    # hint: datetime.datetime.strptime(myrawstring, "insert input format here")

    # 5. convert the `enddate` datetime to the desired output date format by looking at dummy.csv
    # hint: mydateobject.strftime("insert output format here")

    # 6. write the transformed date and "approve" value to the csv
