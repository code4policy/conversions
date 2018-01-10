# example3: bubble chart 2

**Dependency**: Run `pip2 install pandas`.

1. Look at the original data format.

    ```
    cat input.csv
    ```

2. Look at the output data format.

	```
	cat dummy.csv
	```

3. Create a script, `convert.py` that will transform `input.csv` into `output.csv`.

4. Run the interactive to see that the conversion worked properly.

    ```
    python2 -m SimpleHTTPServer
    ```

Sources:
- Data: [House Office Expenditure](https://projects.propublica.org/represent/expenditures)
	- input.csv is [2017Q1-house-disburse-detail.csv](https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv)
- Visualization: [Bubble Chart](https://bl.ocks.org/mbostock/4063269)
