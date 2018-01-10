#!/usr/bin/env python2

import pandas as pd

# read input.csv into a pandas dataframe (df for short)
df = pd.read_csv('input.csv')

# filter to just reprentatives (i.e. bioguide_id is not null)
df = df[
    (df.BIOGUIDE_ID.notnull())
]

# group by purpose, sum amount
df = df.groupby(by='CATEGORY', as_index=False)['AMOUNT'].sum()

# remove spaces in purpose and replace with _
df['CATEGORY'] = df['CATEGORY'].str.replace(' ', '_')

# prepend 'root/' to each row and append '.txt'
df['CATEGORY'] = 'root/' + df['CATEGORY'] + '.txt'

# rename columns to id and value
df.columns = ['path', 'size']

# create a blank row
blank_row = pd.DataFrame({"path": ["root"], "size": [None]})

# prepend the blank row to the top of the df
df = pd.concat([blank_row, df])

# output csv
df.to_csv('output.csv', index=False)
