-- list all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
SELECT g.name, SUM(rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_ratings AS r
ON g.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
