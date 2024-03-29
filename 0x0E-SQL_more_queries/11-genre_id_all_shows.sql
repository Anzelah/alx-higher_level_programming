-- list all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT s.title, IFNULL(g.genre_id, 'NULL') AS genre_id
FROM tv_shows AS s LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
