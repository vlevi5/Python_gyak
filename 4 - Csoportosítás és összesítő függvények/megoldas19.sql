SELECT diakid, COUNT(osztalyzat) AS otosok_szama
FROM jegyek
WHERE MONTH(beirva) BETWEEN "1" AND "3" AND osztalyzat = "5" 
GROUP BY diakid
ORDER BY otosok_szama DESC
LIMIT 1;