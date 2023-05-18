-- This script lists all genre of a show

-- List all genres of the show Dexter
SELECT name
FROM tv_genres a
INNER JOIN tv_show_genres b
ON a.id = b.genre_id
INNER JOIN tv_shows c
ON b.show_id = c.id
WHERE c.title = "Dexter"
ORDER BY name;
