# example5: horizontal stacked bar

1. Look at the original data format.

    ```
    cat input.json
    ```

2. Look at the output data format.

    ```
    cat dummy.json | jq
    ```

3. Create a script, `convert.py` that will transform `input.csv` into `output.json`.

4. Run the interactive to see that the conversion worked properly.

    ```
    python2 -m SimpleHTTPServer
    ```

5. Navigate to `http://localhost:8000/` in your browser and see the interactive work.

Sources:
- Data: [unitedstates/congress-legislators](https://github.com/unitedstates/congress-legislators)
	- [legislators-current.json](https://theunitedstates.io/congress-legislators/legislators-current.json)
- Visualization: [Bar Chart](http://bl.ocks.org/juan-cb/faf62e91e3c70a99a306)
