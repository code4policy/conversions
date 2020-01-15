#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable called `polls`

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"

# 3. Loop through each row of `polls` 

    # 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
    # hint: to read the date you will need to use
    #       date = datetime.datetime.strptime(myrawstring, "insert input format here")
    #
    #       and to write the date you will need to use something like 
    #       new_date = date.strftime("insert output format here")
    # 
    #       date formats can be found at https://strftime.org/
    
    # 5. write a new row of data with the transformed date and value for "approve" 
