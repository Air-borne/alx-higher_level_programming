-- This script lists all the cities of California in the database

-- List all cities in California
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
);
