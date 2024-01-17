-- Create a new database named 'hbtn_0d_usa' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a new table named 'cities' if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    -- Assign a unique ID for each city record
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,

    -- Assign a state ID for each city record to establish a relationship with the 'states' table
    state_id INT NOT NULL,

    -- Store the name of the city
    name VARCHAR(255) NOT NULL,

    -- Establish a foreign key constraint between 'state_id' and 'id' column of 'states' table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
