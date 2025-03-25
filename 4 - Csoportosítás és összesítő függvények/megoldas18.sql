SELECT tanarid, COUNT(osztalyzat) AS beirt_egyesek_szama
FROM jegyek
WHERE osztalyzat = "1" 
GROUP BY tanarid
ORDER BY beirt_egyesek_szama DESC
LIMIT 2,1;