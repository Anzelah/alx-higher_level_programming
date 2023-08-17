-- list all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
SELECT DISTINCT s.title FROM tv_shows AS s
WHERE s.title NOT IN (
	SELECT s.title FROM tv_shows AS s
	INNER JOIN tv_show_genres AS sg
	ON s.id = sg.show_id

	INNER JOIN tv_genres AS g
	ON g.id = sg.genre_id
	WHERE g.name = 'Comedy')
ORDER BY s.title;
