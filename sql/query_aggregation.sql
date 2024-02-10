--average year published & earliest published book
SELECT
    AVG(year_published),
    MIN(year_published)
    FROM books;