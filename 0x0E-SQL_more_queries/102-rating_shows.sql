-- list all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
SELECT name, SUM(rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON sg.genre_id = g.id

INNER JOIN tv_show_ratings AS r
ON r.show_id = sg.show_id
GROUP BY name
ORDER BY rating DESC;
