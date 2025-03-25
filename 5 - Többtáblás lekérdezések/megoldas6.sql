SELECT diakok.nev, COUNT(jegyek.id) AS jegyek_szama
FROM diakok, jegyek
WHERE jegyek.diakid = diakok.id
GROUP BY diakok.id;