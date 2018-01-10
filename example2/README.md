# example2

1. Look at the original visualization https://obamawhitehouse.archives.gov/interactive-budget.

2. Look at the target visualization: https://bl.ocks.org/mbostock/4063269

3. Extract the data from the original viz.

    ```
    pip2 install PyExecJS
    ./extract.py
    ```

4. Look at the original data format.

    ```
    cat input.json
    ```

5. Look at the output data format: https://bl.ocks.org/mbostock/4063269#flare.csv

6. Run `./convert.py` to convert `input.json` to `output.csv`.

7. Run the interactive to see that the conversion worked properly.

    ```
    python2 -m SimpleHTTPServer
    ```

Sources:
- Data: https://obamawhitehouse.archives.gov/interactive-budget
- Visualizaton: https://bl.ocks.org/mbostock/4063269
