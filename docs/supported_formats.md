# Supported Formats

Many data formats can be converted to PyArrow tables.

## CSV

[pyarrow.csv.read_csv](https://arrow.apache.org/docs/python/generated/pyarrow.csv.read_csv.html)

```python
from pyarrow import csv

table = csv.read_csv("/path/to/file")
```

## Daft

[daft.DataFrame.to_arrow](https://www.getdaft.io/projects/docs/en/stable/api_docs/doc_gen/dataframe_methods/daft.DataFrame.to_arrow.html)

```python
table = df.to_arrow()
```

## DataFusion

[pyarrow.table](https://arrow.apache.org/docs/python/generated/pyarrow.table.html)

```python
import pyarrow as pa

table = pa.table(df)
```

## Delta

[deltalake.table.DeltaTable.to_pyarrow_table](https://delta-io.github.io/delta-rs/python/api_reference.html#deltalake.table.DeltaTable.to_pyarrow_table)

```python
table = delta_table.to_pyarrow_table()
```

## DuckDB

[duckdb.DuckDBPyConnection.arrow](https://duckdb.org/docs/stable/clients/python/reference/#duckdb.DuckDBPyConnection.arrow)

```python
import duckdb

table = duckdb.sql("SELECT * FROM my_table").arrow()
```

## Feather

[pyarrow.feather.read_table](https://arrow.apache.org/docs/python/generated/pyarrow.feather.read_table.html)

```python
import pyarrow.feather as feather

table = feather.read_table("/path/to/file")
```

## Iceberg

[pyiceberg.table.DataScan.to_arrow](https://py.iceberg.apache.org/reference/pyiceberg/table/#pyiceberg.table.DataScan.to_arrow)

```python
table = iceberg_table.scan().to_arrow()
```

## JSON

[pyarrow.json.read_json](https://arrow.apache.org/docs/python/generated/pyarrow.json.read_json.html)

```python
from pyarrow import json

table = json.read_json("/path/to/file")
```

## Lance

[lance.LanceDataset.to_table](https://lancedb.github.io/lance/api/python/LanceDataset.to_table.html)

```python
table = dataset.to_table()
```

## Pandas

[pyarrow.Table.from_pandas](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table.from_pandas)

```python
import pyarrow as pa

table = pa.Table.from_pandas(df)
```

## Parquet

[pyarrow.parquet.read_table](https://arrow.apache.org/docs/python/generated/pyarrow.parquet.read_table.html)

```python
import pyarrow.parquet as pq

table = pq.read_table("/path/to/file")
```

## Polars

[polars.DataFrame.to_arrow](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.to_arrow.html)

```python
table = df.to_arrow()
```

## Vaex

[vaex.dataframe.DataFrame.to_arrow_table](https://vaex.io/docs/api.html#vaex.dataframe.DataFrame.to_arrow_table)

```python
table = df.to_arrow_table()
```
