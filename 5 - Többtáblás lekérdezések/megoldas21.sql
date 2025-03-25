SELECT diakok.nev, diakok.nem, diakok.evfolyam, diakok.osztaly, AVG(jegyek.osztalyzat) AS atlag
FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
GROUP BY diakok.id
ORDER BY atlag DESC LIMIT 1;