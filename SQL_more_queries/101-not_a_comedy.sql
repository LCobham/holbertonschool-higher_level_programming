-- List all shows which are not Comedy
SELECT DISTINCT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres, tv_genres
    WHERE tv_show_genres.genre_id = tv_genres.id AND
        tv_genres.name = 'Comedy'
)
ORDER BY title;