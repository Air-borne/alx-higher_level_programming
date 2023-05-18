-- This script lists all genres and displays the number of shows for each

-- List all genres
SELECT a.name AS genre, COUNT(b.genre_id) AS number_of_shows
FROM tv_genres a
INNER JOIN tv_show_genres b
ON a.id = b.genre_id
GROUP BY a.name
ORDER BY number_of_shows DESC;
