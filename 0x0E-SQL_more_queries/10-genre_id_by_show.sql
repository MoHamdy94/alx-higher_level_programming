-- This query retrieves the title of TV shows and their associated genre IDs
--FROM the 'tv_shows' table and the 'tv_show_genres' table, respectively.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- A LEFT JOIN is used to return all records from the 'tv_shows' table,
--  and any matching records from the 'tv_show_genres' table.
-- If there is no match, the result is NULL on the right side.
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
-- This WHERE clause filters out the rows where the genre_id is NULL,
--  which means that only the rows with a matching genre_id are returned.
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
-- The ORDER BY clause sorts the result set first by title, and then by genre_id.
