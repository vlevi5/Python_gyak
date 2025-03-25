SELECT tanarid, diakid, osztalyzat, beirva
FROM jegyek
WHERE beirva >= "2023-02-01 00:00:00" AND beirva <= "2023-02-28 23:59:59"
ORDER BY beirva ASC;