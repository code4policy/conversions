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

# prepend 'flare.other' to each row
df['CATEGORY'] = 'flare.other.' + df['CATEGORY']

# rename columns to id and value
df.columns = ['id', 'value']

# output csv
df.to_csv('output.csv', index=False)

