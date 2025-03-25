SELECT targy, COUNT(diakid) AS diakok_szama
FROM oktatott
GROUP BY tanarid, targy
HAVING COUNT(diakid) >= 10 AND COUNT(diakid) <= 20
ORDER BY diakok_szama DESC;