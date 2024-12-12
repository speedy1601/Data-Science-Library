| No |                  Pandas                     |                    Polars                       |
| :- | :------------------------------------------ | :---------------------------------------------- |
| 1  | `duplicated(keep='first')`                  | `~is_first_distinct()`                          |
| 2  | `duplicated(keep='last')`                   | `~is_last_distinct()`                           |
| 3  | `apply(func, include_groups=False)`         | `map_groups(function, schema=None)`             |
| 4  | `assign(conditions_separated_by_comma)`     | `with_columns(expressions_separated_by_comma)`  |
| 5  | `merge(right, on, left_on, right_on, how)`  | `join(other, on, left_on, right_on, how)`       |
| 6  | `nlargest(n, columns, keep)`                |  `top_k(k, by, reverse)`                        |
| 7  | `nsmallest(n, columns, keep)`               |  `bottom_k(k, by, reverse)`                     |
| 8  | `query("conditions")`                       |  `filter(expressions)`                          |
| 9  |  `explode(columns)`                         |  `explode(columns)` (from value [1, 2] to TWO vertical rows having 1, 2) |
| 10 |                                             |  `unnest(columns)`                              |
| 11 |  `value_counts(...)`                        |  `value_counts().unnest(..)`                    |
| 12 |  `pivot(index, columns, values)`            |  `pivot(index, on, values)`                     |
| 13 |  `pivot_table(index, columns, values, aggfunc)`|  For LazyFrame = `group_by`, for DataFrame = `pivot(index, on, values, aggregate_function)`|
| 14 |                                                |  `with_row_index(name, offset)`                |
| 15 |  `diff()`                                      |  `diff()`                                      |
| 16 | `to_datetime(column_name, errors='coerce')`    |  `.str.to_datetime(format)`                    |
| 17 | `date_range(start, end, freq)`                 |  `date_range/datetime_range (start, end, interval)`|
| 18 |                                                |  `with_row_index(name, offset)`                    |
| 19 | `group_by(column) [column].transform(function)` | `col(column).aggregate_function().over(partition_by)` |
| 20 |                                                 | `not_()`                                              |
| 21 |                                                 | `.is_not_nan(), is_not_null()`                        |
| 22 | `divide(), truediv()`                           |  `truediv()`                                          |
| 22 | `floordiv()`                                    | `floordiv()`                                          |
| 23 | `pd.concat()`                                   | `pl.concat()`                                         |
| 24 |                 | `pl.concat_list()` --> Horizontally concatenate columns into a single list column.    |
| 25 |                 | `pl.concat_str()`  --> Horizontally concatenate columns into a single string column.  |
| 26 |                                                 | `.str.pad_start(), .str.pad_end()`                    |