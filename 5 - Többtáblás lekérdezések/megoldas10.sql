FROM diakok, jegyek
WHERE diakok.id = jegyek.diakid AND jegyek.osztalyzat = "1" AND MONTH(jegyek.beirva) = "1" AND DAY(jegyek.beirva) BETWEEN "1" AND "7"
GROUP BY diakok.id
ORDER BY diakok.nev ASC;

/* hivatalos megoldás [ugyanaz az eredmény]

SELECT DISTINCT nev
FROM diakok, jegyek
WHERE diakok.id = jegyek.diakid
AND osztalyzat = 1
AND MONTH(beirva) = 1
AND DAY(beirva) BETWEEN 1 AND 7
ORDER BY nev ASC;

*/