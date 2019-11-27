-- createS table with two pks
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = cities.state_id;
