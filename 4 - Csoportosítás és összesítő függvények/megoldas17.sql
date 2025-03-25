SELECT MONTH(beirva) AS honapok
FROM jegyek
WHERE osztalyzat = "1" 
GROUP BY MONTH(beirva)
HAVING COUNT(osztalyzat) > 15;