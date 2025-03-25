SELECT diakok.nev, AVG(jegyek.osztalyzat) AS atlag
FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
GROUP BY diakok.id
HAVING AVG(jegyek.osztalyzat) > ANY(
    SELECT AVG(jegyek.osztalyzat) 
    FROM diakok INNER JOIN jegyek ON diakok.id = jegyek.diakid
    WHERE (diakok.evfolyam = "11" AND diakok.osztaly = "B") OR (diakok.evfolyam = "9" AND diakok.osztaly = "A")
    GROUP BY diakok.evfolyam, diakok.osztaly
);