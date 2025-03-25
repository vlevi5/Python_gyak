SELECT diakok.nev, jegyek.osztalyzat, jegyek.beirva
FROM diakok, jegyek
WHERE diakok.id = jegyek.diakid
ORDER BY diakok.nev ASC, jegyek.beirva DESC;