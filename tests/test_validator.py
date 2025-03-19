import pyarrow as pa

from arrowquality.validator import Validator

pylist = [
    {"n_legs": 2, "species": "Flamingo", "name": "Alice", "sex": "male"},
    {"n_legs": 4, "species": "Dog", "name": "Tom", "sex": "female"},
    {"n_legs": 0, "species": "Snake", "name": None, "sex": "female"},
    {"n_legs": 2, "species": "Human", "name": "Steve", "sex": "male"},
]
table = pa.Table.from_pylist(pylist)
validator = Validator(table)


def test_values_of_type() -> None:
    assert validator.values_of_type("n_legs", "int64")
    assert validator.values_of_type("species", "string")
    assert not validator.values_of_type("species", "double")


def test_values_unique() -> None:
    assert validator.values_unique("species")
    assert not validator.values_unique("n_legs")


def test_values_between() -> None:
    assert validator.values_between("n_legs", 0, 4)
    assert not validator.values_between("n_legs", 1, 2)


def test_values_greater_than() -> None:
    assert validator.values_greater_than("n_legs", -1)
    assert not validator.values_greater_than("n_legs", 5)


def test_values_less_than() -> None:
    assert validator.values_less_than("n_legs", 10)
    assert not validator.values_less_than("n_legs", 3)


def test_values_not_greater_than() -> None:
    assert validator.values_not_greater_than("n_legs", 8)
    assert not validator.values_not_greater_than("n_legs", 2)


def test_values_not_less_than() -> None:
    assert validator.values_not_less_than("n_legs", 0)
    assert not validator.values_not_less_than("n_legs", 4)


def test_values_in_set() -> None:
    assert validator.values_in_set("sex", {"male", "female"})
    assert not validator.values_in_set("species", {"Apple"})


def test_values_not_null() -> None:
    assert validator.values_not_null("species")
    assert not validator.values_not_null("name")


def test_values_stddev_greater_than() -> None:
    assert validator.values_stddev_greater_than("n_legs", 0)
    assert not validator.values_stddev_greater_than("n_legs", 2)


def test_values_stddev_less_than() -> None:
    assert validator.values_stddev_less_than("n_legs", 2)
    assert not validator.values_stddev_less_than("n_legs", 0)


def test_values_stddev_between() -> None:
    assert validator.values_stddev_between("n_legs", 1, 2)
    assert not validator.values_stddev_between("n_legs", 2, 3)


def test_values_mean_between() -> None:
    assert validator.values_mean_between("n_legs", 1, 4)
    assert not validator.values_mean_between("n_legs", 0, 1)


def test_values_mode_between() -> None:
    assert validator.values_mode_between("n_legs", 1, 4)
    assert not validator.values_mode_between("n_legs", 0, 1)


def test_values_median_between() -> None:
    assert validator.values_median_between("n_legs", 1, 4)
    assert not validator.values_median_between("n_legs", 0, 1)
