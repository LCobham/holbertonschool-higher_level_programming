-- List all records in second_table with a name
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
