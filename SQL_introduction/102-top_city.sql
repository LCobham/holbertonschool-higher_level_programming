-- Display the top 3 cities of temperatures
-- during July and August
SELECT city, AVG(value) AS avg_temp
    FROM temperatures
    WHERE month >= 7 AND month < 9
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;
    