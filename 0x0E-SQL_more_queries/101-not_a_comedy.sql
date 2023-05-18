-- This script lists all shows without the genre comedy

-- List all shows without the genre comedy
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT title
	FROM tv_shows a
	INNER JOIN tv_show_genres b
	ON a.id = b.show_id
	INNER JOIN tv_genres c
	ON b.genre_id = c.id
	WHERE c.name = "Comedy"
)
ORDER BY title ASC;
