# Supported Formats

Many data formats can be converted to PyArrow tables.

## CSV

```python
from pyarrow import csv

table = csv.read_csv("/path/to/file")
```

## Daft

```python
table = df.to_arrow()
```

## Dask

```python
table = pa.Table.from_pandas(ddf.compute())
```

## DataFusion

```python
import pyarrow as pa

table = pa.table(df)
```

## Delta

```python
table = delta_table.to_pyarrow_table()
```

## DuckDB

```python
table = duckdb.sql("SELECT * FROM my_table").arrow()
```

## Feather

```python
import pyarrow.feather as feather

table = feather.read_table("/path/to/file")
```

## Iceberg

```python
table = iceberg_table.scan().to_arrow()
```

## Ibis

```python
table = t.to_pyarrow()
```

## JSON

```python
from pyarrow import json

table = json.read_json("/path/to/file")
```

## Lance

```python
table = dataset.to_table()
```

## Modin

```python
import pyarrow as pa
from modin.pandas.io import to_pandas

table = pa.Table.from_pandas(to_pandas(df))
```

## Pandas

```python
import pyarrow as pa

table = pa.Table.from_pandas(df)
```

## Parquet

```python
import pyarrow.parquet as pq

table = pq.read_table("/path/to/file")
```

## Polars

```python
table = df.to_arrow()
```

## PySpark

```python
import pyarrow as pa

table = pa.Table.from_pandas(df.toPandas())
```

## Vaex

```python
table = df.to_arrow_table()
```
