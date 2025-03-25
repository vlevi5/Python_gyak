SELECT nev, AVG(jegyek.osztalyzat) AS atlag
FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
GROUP BY diakok.id
HAVING atlag > ALL (
    SELECT AVG(jegyek.osztalyzat)
    FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
    GROUP BY diakok.nem
)   
ORDER BY atlag DESC;