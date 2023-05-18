-- This script list all shows, and all genres linked to each show

-- List all shows, and all genres linked to each show
SELECT b.title, c.name
FROM tv_shows b
LEFT JOIN tv_show_genres a
ON a.show_id = b.id
LEFT JOIN tv_genres c
ON a.genre_id = c.id
ORDER BY b.title, c.name;
