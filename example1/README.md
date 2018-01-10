# example1: bullet chart

1. Look at the original data format.

    ```
    cat input.csv
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
- Visualization: [Bullet Chart](https://bl.ocks.org/mbostock/4061961)
