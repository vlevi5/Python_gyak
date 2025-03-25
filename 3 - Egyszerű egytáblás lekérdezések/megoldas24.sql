SELECT tanarid, diakid, osztalyzat, beirva
FROM jegyek
WHERE beirva BETWEEN "2023-02-01 00:00:00" AND "2023-02-28 23:59:59"
ORDER BY beirva ASC;