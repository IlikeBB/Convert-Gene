# Convert-Gene

## Env Preparing
```
python setup.py
```

## Data Preparing
> * input data must csv type.
```
LOC, Gene
1231, C
4513, G
21432, G
.
.
.
```

## Start Convert
```
python convert.py --input *.csv --output {file_name}
```
```
python convert.py --input ./demo/feature.csv --output conver_result
```


