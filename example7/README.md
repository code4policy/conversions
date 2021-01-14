# example7: scatter plot

**Note**: This example may be possible without Python using just Excel or Sublime Text.

### Step 1: Run the example visuzalization

1. Run a simple python server in this folder

    ```
    python3 -m http.server 8000
    ```
    
2. Navigate to `http://localhost:8000/`

### Step 2: Change out the data

1. Look at the original data format.

    ```
    head input.csv
    ```

2. Look at the dummy data that the visualization takes in.

    ```
    head dummy.csv
    ```

3. Create a script, `convert.py` that will transform `input.csv` into `output.csv`. The output should be in the same format as the dummy data. (check the `solution/` folder if you get stuck)

### Step 3: Change the visualization to read the new data

1. Update the visualization to read the new column headers. For example
	- currently `dummy.csv` has the columns `date` and `close`
	- however, `output.csv` has the columns `date` and `approve`
	
	You will need to modify the javascript to read the new column `approve` instead of looking for a column named `close`

2. Navigate to `http://localhost:8000/` in your browser and see the interactive work.

3. Split out the HTML, CSS, and JS into separate files and make sure the visualization still works.

Sources
- Data: [FiveThirtyEight Trump Approval Ratings](https://projects.fivethirtyeight.com/trump-approval-ratings/)
	- [Raw Polls](https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv)
- Visualzation: [Scatter Plot](https://bl.ocks.org/d3noob/6f082f0e3b820b6bf68b78f2f7786084)
