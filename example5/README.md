# example5: horizontal bar

1. Look at the original data format.

    ```
    cat input.json
    ```

2. Look at the output data format.

    ```
    cat dummy.json | jq
    ```

3. Create a script, `convert.py` that will transform `input.csv` into `output.json`.

4. Navigate to `http://localhost:8000/example5` in your browser and see the interactive work.

Sources:
- Data: [unitedstates/congress-legislators](https://github.com/unitedstates/congress-legislators)
	- [legislators-current.json](https://theunitedstates.io/congress-legislators/legislators-current.json)
- Visualization: [Horizontal Bar Chart](https://bl.ocks.org/hrecht/f84012ee860cb4da66331f18d588eee3)
