-- Query to combine author and book Information using Inner Join
SELECT *
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;