# example2: bubble chart

1. Look at the original data format.

    ```
    cat input.json
    ```

2. Look at the output data format.

	```
	cat dummy.csv
	```

3. Create a script, `convert.py` that will transform `input.json` into `output.csv`.

4. Run the interactive to see that the conversion worked properly.

    ```
    python2 -m SimpleHTTPServer
    ```

Sources:
- Data: [ObamaWhiteHouse Interactive Budget](https://obamawhitehouse.archives.gov/interactive-budget) | [Extract Script](https://gist.github.com/AlJohri/0ff2570ecf2e3316ec7c9dead6d78ee7)
- Visualizaton: [Bubble Chart](https://bl.ocks.org/mbostock/4063269)
