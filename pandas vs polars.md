| No |                  Pandas                     |                    Polars                       |
| :- | :------------------------------------------ | :---------------------------------------------- |
| 1  | `duplicated(keep='first')`                  | `~is_first_distinct()`                          |
| 2  | `duplicated(keep='last')`                   | `~is_last_distinct()`                           |
| 3  | `apply(func, include_groups=False)`         | `map_groups(function, schema=None)`             |
| 4  | `assign(conditions_separated_by_comma)`     | `with_columns(expressions_separated_by_comma)`  |
| 5  | `merge(right, on, left_on, right_on, how)`  | `join(other, on, left_on, right_on, how)`       |
| 6  |  `nlargest(n)`                              |  `top_k(k)`                                     |
| 7  |  `nsmallest(n)`                             |  `bottom_k(k)`                                  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |

Note : polars `LazyFrame.select(col('x').value_counts())` returns a single column with struct values, e.g. `{23, 5}`. To seperate these values into Two Different Columns, first do `collect()` and then `unnest(column_names_to_unnest)`.