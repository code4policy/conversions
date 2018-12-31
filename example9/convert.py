#!/usr/bin/env python3

# read input.txt as a text file and skip the first few lines until it reaches the actual data

# use the string `.split()` method on each line to split the two columns. this file is a "fixed width" text file
# so the csv module cannot handle it. there is no consistent delimeter such as a tab character or
# comma, instead there are variable number of spaces in between the two columns

# use the datetime module to convert the dates. see http://strftime.org/
# be wary of the two numbered year and see if that causes any problems in the interactive

# write the output to a file, output.tsv
