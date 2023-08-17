-- list all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
SELECT g.name, SUM(rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id

INNER JOIN tv_show_ratings AS r
ON sg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
