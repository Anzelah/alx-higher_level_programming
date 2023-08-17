-- list all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_genres.name
-- If a show doesn’t have a genre, display NULL in the genre column
SELECT s.title, IFNULL(g.name, 'NULL') AS name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg
ON s.id = sg.show_id

LEFT JOIN tv_genres AS g
ON g.id = sg.genre_id
ORDER BY s.title, g.name;
