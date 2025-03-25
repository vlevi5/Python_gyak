SELECT DAY(beirva) AS nap, COUNT(osztalyzat) AS osztalyzatok_szama
FROM jegyek
WHERE MONTH(beirva) = "3"
GROUP BY DAY(beirva)
HAVING COUNT(osztalyzat) > "5"
ORDER BY osztalyzatok_szama DESC;