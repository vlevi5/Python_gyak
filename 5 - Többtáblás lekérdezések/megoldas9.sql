SELECT diakok.nev, COUNT(jegyek.id) AS otosok_szama
FROM diakok, jegyek
WHERE diakok.id = jegyek.diakid AND jegyek.osztalyzat = "5" AND MONTH(jegyek.beirva) BETWEEN "3" AND "4"
GROUP BY diakok.id
ORDER BY otosok_szama DESC;