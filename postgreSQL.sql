-- In postgreSQL you can't say "WHERE product_id == NULL" because 
--     In SQL, NULL is not equal to anything (not even to NULL itself), so you cannot use = to compare NULL values. Instead
--     you should use ISNULL to check for NULL values "WHERE product_id ISNULL"

-- Length of a string : LENGTH('AAAA').

-- How to place all the NULL values at the last/first without sorting the NON NULLS VALUES?
-- -- Read [this](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/solutions/5903096/pandas-polars-postgresql)
-- -- postgreSQL's soltuion at the last and see the image, 'postgresql_1' from 'Drawing For Leetcode' folder in D drive.

--  Why you should avoid SUB-QUEIES :
-- ----------------------------------
-- Actually the time complexity for sub-queries depend on whether it is a scalar subquery (returning only a single value) or a correlated
-- subquery. Time taken is noticeably high for Correlated Sub-queries where each row from the inner sub-query is matched with each row
-- from the outer query thus taking a worst time complexity of O(M*N). Depends from case to case which one is better.
-- Oftentimes, JOINs are faster than sub-queries because sub-queries are evaluated once for each row of the outer query. The query
-- optimizer may transform this nested query into a JOIN only. I guess even though SQL is declarative (and not imperative), one should
-- have some idea of which operations are costly.. Your query may be simpler but try running it on a database containing million rows and
-- watch your SQL client freeze :)

-- WITH variable_name AS (query) :
-- -------------------------------
-- WITH maxx AS(SELECT MAX(visit_id) FROM visits) => returns A SCALER VALUE but in a Table Form (a single row and a single column).
-- So if you ever think that instead of writing SUBQUERY you will create a TEMPORARY VARIABLE and then use that TMEPORARY VARAIBLE
-- instead of that SUBQUERY, YOU ARE STUPID AND WRONG. See "PostgreSQL_WITH_AS.png" in this Data Science Folder. Once you've to write a
-- subquery, there's no escape from it! Subquery is like NESTED LOOPS, a query inside another query which is like Loop inside another
-- Loop. Unless the subquery returns a SCALER VALUE(1 row, 1 column), avoids using subquery. JOINING is more better in this case.

-- To work with Datetime values, read [https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-timestamp/] and the next pages

-- You can't use CTE reference inside HAVING clause. See [No CTE inside HAVING clause.jpg] inside "Postgresql images" folder.