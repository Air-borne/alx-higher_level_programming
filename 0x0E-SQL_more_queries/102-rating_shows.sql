--

--
SELECT a.title, SUM(b.rate) AS rating
FROM tv_shows a
RIGHT JOIN tv_show_ratings b
ON a.id = b.show_id
GROUP BY a.title
ORDER BY rating DESC;
