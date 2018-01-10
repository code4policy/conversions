# example3: bubble chart 2

1. Look at the original data format.

    ```
    cat input.csv
    ```

2. Look at the output data format.

	```
	cat dummy.csv
	```

3. Create a script, `convert.py` that will transform `input.csv` into `output.csv`.

4. Navigate to `http://localhost:8000/example3` in your browser and see the interactive work.

5. **Try It** Change `convert.py` to filter down to a single representative and look at the resulting chart.

Sources:
- Data: [House Office Expenditure](https://projects.propublica.org/represent/expenditures)
	- input.csv is [2017Q1-house-disburse-detail.csv](https://projects.propublica.org/congress/assets/staffers/2017Q1-house-disburse-detail.csv)
- Visualization: [Bubble Chart](https://bl.ocks.org/mbostock/4063269)
