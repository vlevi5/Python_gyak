SELECT AVG(jegyek.osztalyzat) AS atlag, diakok.evfolyam, diakok.osztaly, COUNT(DISTINCT jegyek.diakid) AS diakok_szama
FROM diakok INNER JOIN jegyek on diakok.id = jegyek.diakid
GROUP by diakok.evfolyam, diakok.osztaly
ORDER BY atlag DESC LIMIT 1;