-- This scripts lists all cities in the database, 

-- Lists all cities and show the name of their state
SELECT a.id, a.name, b.name
FROM cities a
INNER JOIN states b
ON a.state_id = b.id
ORDER BY a.id ASC;
