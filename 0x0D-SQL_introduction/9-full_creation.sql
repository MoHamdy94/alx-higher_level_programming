-- Create table 'second_table' in db 'hbtn_0c_0'
-- Addprops  (id INT), (name VARCHAR(256)), (score INT)
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name varchar(256),
    score int
);
INSERT INTO 'second_table' VALUES(1, 'john', 10);
INSERT INTO 'second_table' VALUES(2, 'alex', 3);
INSERT INTO 'second_table' VALUES(3, 'Bob', 14);
INSERT INTO 'second_table' VALUES(4, 'George', 8);
