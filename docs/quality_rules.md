# Quality Rules

| Rule | Description | Arguments |
| --- | --- | --- |
| values_of_type | Check if values are of the proveded type | `column_name`: column name to check<br>`type`: data type |
| values_unique | Check if values are unique | `column_name`: column name to check |
| values_between | Check if values are within the provided range (inclusive of both boundaries) | `column_name`: column name to check<br>`min`<br>`max` |
| values_not_greater_than | Check if values are not greater than the provided limit | `column_name`: column name to check<br>`limit`: limit value |
| values_not_less_than | Check if values are not less than the provided limit | `column_name`: column name to check<br>`limit`: limit value |
| values_in_set | Check if values are in the provided set | `column_name`: column name to check<br>`set_`: set of allowed values |
| values_not_null | Check if values are are not null | `column_name`: column name to check |
