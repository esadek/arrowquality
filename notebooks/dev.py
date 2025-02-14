import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pyarrow as pa
    import pyarrow.compute as pc
    from pyarrow import csv

    return csv, mo, pa, pc


@app.cell
def _(csv):
    table = csv.read_csv("input.csv")
    return (table,)


@app.cell
def _(table):
    table
    return


@app.cell
def _(pa, pc):
    class Validator:
        def __init__(self, table: pa.lib.Table):
            self.table = table

        def values_of_type(self, column_name: str, type):
            return type == self.table.column(column_name).type

        def values_unique(self, column_name: str):
            column = self.table.column(column_name)
            return column.length() == len(pc.unique(column))

        def values_between(self, column_name: str, min, max):
            column = self.table.column(column_name)
            result = pc.min_max(column).as_py()
            actual_min, actual_max = result.get("min"), result.get("max")
            return min <= actual_min and max >= actual_max

        def values_in_set(self, column_name: str, set_: set):
            column = self.table.column(column_name)
            return set(pc.unique(column).to_pylist()).issubset(set_)

    return (Validator,)


@app.cell
def _(Validator, table):
    validator = Validator(table)
    return (validator,)


@app.cell
def _(validator):
    validator.values_of_type("Age", "double")
    return


@app.cell
def _(validator):
    validator.values_between("Age", 0, 100)
    return


@app.cell
def _(validator):
    validator.values_in_set("Sex", {"male", "female"})
    return


@app.cell
def _(validator):
    validator.values_unique("Name")
    return


@app.cell
def _(datetime, pa):
    pylist = [
        {
            "created_at": datetime.now().date(),
            "n_legs": 2,
            "species": "Flamingo",
            "name": "Alice",
            "sex": "male",
        },
        {"n_legs": 4, "species": "Dog", "name": "Tom", "sex": "female"},
        {"n_legs": 0, "species": "Snake", "name": None, "sex": "female"},
        {"n_legs": 2, "species": "Human", "name": "Steve", "sex": "male"},
    ]
    tbl = pa.Table.from_pylist(pylist)
    tbl
    return pylist, tbl


@app.cell
def _(tbl):
    column = tbl.column("n_legs")
    return (column,)


@app.cell
def _():
    from datetime import datetime

    datetime.now()
    return (datetime,)


if __name__ == "__main__":
    app.run()
