-- List all the cities in California in hbtn_0d_usa database
SELECT * FROM cities
    WHERE state_id = (
        SELECT id FROM states
            WHERE name='California'
    );