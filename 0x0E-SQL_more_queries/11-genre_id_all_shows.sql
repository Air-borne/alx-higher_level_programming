-- This script lists all shows in a database

-- List all shows
SELECT a.title AS title, b.genre_id AS genre_id
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
ORDER BY title ASC, genre_id ASC;
