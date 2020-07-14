-- 13. Number of shows by genre
-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name 'genre', COUNT(*) 'number_of_shows'
FROM tv_genres, tv_show_genres 
WHERE tv_show_genres.genre_id = tv_genres.id 
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
