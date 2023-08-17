-- use the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
SELECT g.name FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id

INNER JOIN tv_shows as s
ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name;
