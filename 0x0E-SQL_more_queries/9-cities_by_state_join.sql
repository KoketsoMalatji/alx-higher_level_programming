--  lists all cities contained
SELECT cities.id, cities.name, states.name FROM cities, states WHERE states.id = cities.state_id
ORDER BY cities.id ASC;
