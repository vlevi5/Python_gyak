SELECT osztalyzat, beirva
FROM jegyek
WHERE HOUR(beirva) >= 20
ORDER BY beirva ASC;