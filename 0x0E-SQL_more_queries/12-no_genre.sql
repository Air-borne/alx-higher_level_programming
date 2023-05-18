-- This script lists all shows without a genre

-- List all shows without a genre
SELECT a.title AS title, b.genre_id AS genre_id
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
WHERE b.genre_id IS NULL
ORDER BY title ASC, genre_id ASC;
