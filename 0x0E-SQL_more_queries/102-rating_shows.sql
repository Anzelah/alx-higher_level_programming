-- list all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
SELECT s.title, SUM(rate) AS rating
FROM tv_shows AS s

INNER JOIN tv_show_ratings AS r
ON r.show_id = s.id
GROUP BY s.title
ORDER BY rating DESC;
