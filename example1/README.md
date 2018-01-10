# example1

1. Look at the original CSV data. We will need to convert this data to JSON.

```
cat input.csv
```

2. Look at the target JSON format.

```
cat output.json | jq
```

3. Look at and then run `convert.py` to convert `input.csv` into `output.json`.

```
./convert.py
```

4. Run the interactive to see that the conversion worked properly.

```
python2 -m SimpleHTTPServer
```

5. Navigate to `http://localhost:8000/` in your browser and see the interactive work.

Original Source: https://bl.ocks.org/mbostock/4061961
