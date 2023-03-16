-- Show the sum of all ratings per show
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating 
FROM tv_shows, tv_show_ratings
WHERE tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.id
ORDER BY rating DESC;