-- This script lists all genres in the database by their ratings

-- List all genres by their summed ratings
SELECT a.name, SUM(c.rate) AS rating
FROM tv_genres a
RIGHT JOIN tv_show_genres b
ON a.id = b.genre_id
RIGHT JOIN tv_show_ratings c
ON b.show_id = c.show_id
WHERE a.name IS NOT NULL
GROUP BY a.name
ORDER BY rating DESC;
