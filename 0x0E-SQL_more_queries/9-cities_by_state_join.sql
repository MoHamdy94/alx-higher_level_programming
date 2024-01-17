-- This query retrieves the ID and name of each city, along with the name of the state that the city is located in.
-- The results are sorted in ascending order by the city ID.

SELECT  -- select the columns to retrieve
    cities.id,  -- retrieve the city ID
    cities.name,  -- retrieve the city name
    states.name  -- retrieve the state name
FROM cities,  -- start with the cities table
    states  -- also include the states table in the query
WHERE cities.state_id = states.id  -- join the two tables on the state_id column
ORDER BY cities.id ASC;  -- sort the results by city ID in ascending order
