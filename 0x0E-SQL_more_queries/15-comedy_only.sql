-- This script lists all comedy shows in given database

-- List all shows with comedy genre
SELECT title
FROM tv_shows a
INNER JOIN tv_show_genres b
ON a.id = b.show_id
INNER JOIN tv_genres c
ON b.genre_id = c.id
WHERE c.name = "Comedy"
ORDER BY title ASC;
