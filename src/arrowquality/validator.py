from typing import Set, Union

import pyarrow as pa
import pyarrow.compute as pc


class Validator:
    def __init__(self, table: pa.lib.Table) -> None:
        self.table = table

    def values_of_type(self, column_name: str, type: str) -> bool:
        """Check if values are of the provided type

        Arguments:
            column_name: Name of column to check
            type: Data type

        Returns:
            True or False
        """
        if type == self.table.column(column_name).type:
            return True
        return False

    def values_unique(self, column_name: str) -> bool:
        """Check if values are unique

        Arguments:
            column_name: Name of column to check

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        if column.length() == len(pc.unique(column)):
            return True
        return False

    def values_between(self, column_name: str, min: int, max: int) -> bool:
        """Check if values are within the provided range (inclusive of both boundaries)

        Arguments:
            column_name: Name of column to check
            min: Minimum limit
            max: Maximum limit

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        result = pc.min_max(column).as_py()
        actual_min, actual_max = result.get("min"), result.get("max")
        if min <= actual_min and max >= actual_max:
            return True
        return False

    def values_greater_than(self, column_name: str, limit: int) -> bool:
        """Check if values are greater than the provided limit

        Arguments:
            column_name: Name of column to check
            limit: Limit value

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        if limit < pc.max(column).as_py():
            return True
        return False

    def values_less_than(self, column_name: str, limit: int) -> bool:
        """Check if values are less than the provided limit

        Arguments:
            column_name: Name of column to check
            limit: Limit value

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        if limit > pc.max(column).as_py():
            return True
        return False

    def values_not_greater_than(self, column_name: str, limit: int) -> bool:
        """Check if values are not greater than the provided limit

        Arguments:
            column_name: Name of column to check
            limit: Limit value

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        if limit >= pc.max(column).as_py():
            return True
        return False

    def values_not_less_than(self, column_name: str, limit: int) -> bool:
        """Check if values are not less than the provided limit

        Arguments:
            column_name: Name of column to check
            limit: Limit value

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        if limit <= pc.min(column).as_py():
            return True
        return False

    def values_in_set(
        self, column_name: str, set_: Set[Union[str, int, float]]
    ) -> bool:
        """Check if values are in the provided set

        Arguments:
            column_name: Name of column to check
            set_: Set of allowed values

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        return set(pc.unique(column).to_pylist()).issubset(set_)

    def values_not_null(self, column_name: str) -> bool:
        """Check if values are are not null

        Arguments:
            column_name: Name of column to check

        Returns:
            True or False
        """
        column = self.table.column(column_name)
        return not pc.any(column.is_null()).as_py()
