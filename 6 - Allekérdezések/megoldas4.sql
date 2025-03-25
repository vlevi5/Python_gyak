SELECT diakok.nev, AVG(jegyek.osztalyzat) AS atlag
FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
GROUP BY diakok.id
HAVING AVG(jegyek.osztalyzat) < (
    SELECT AVG(jegyek.osztalyzat)
    FROM jegyek
);