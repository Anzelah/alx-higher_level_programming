-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in my MySQL server.
SELECT COUNT(score) AS number
FROM second_table
HAVING COUNT(score) > 1
ORDER BY number DESC;
