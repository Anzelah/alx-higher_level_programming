-- list all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
SELECT s.name AS genre, COUNT(g.genre_id) AS number_of_shows
FROM tv_genres AS s LEFT JOIN tv_show_genres AS g
ON s.id = g.genre_id
GROUP BY s.name
ORDER BY number_of_shows DESC;
