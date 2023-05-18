-- This script lists all show in a database

-- List all shows whith a genre
SELECT a.title AS title, b.genre_id AS genre_id
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
WHERE b.genre_id IS NOT NULL
ORDER BY title ASC, genre_id ASC;
