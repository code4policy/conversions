#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable called `polls`

# 2. write a new file called output.csv and write a row with two headers: "date" and "close"

# Loop through each row of `polls` and within that loop

    # 3. convert the fromat of `enddate` from "1/22/2017" to "22-Jan-17"
    # hint: to read the date you will need to use
    #       datetime.datetime.strptime(myrawstring, "insert input format here")
    #
    #       and to write th date you will need to use
    #       mydateobject.strftime("insert output format here")
    # 
    #       dateformats can be found at https://strftime.org/
    
    # 4. write a new row of data with the transformed date and value for "approve" 
