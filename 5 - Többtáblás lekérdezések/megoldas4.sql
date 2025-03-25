SELECT tanarok.nev AS tanar_neve, diakok.nev AS diak_neve, jegyek.osztalyzat, jegyek.beirva
FROM tanarok, diakok, jegyek
WHERE diakok.id = jegyek.diakid AND tanarok.id = jegyek.tanarid AND YEAR(beirva) = "2023" AND MONTH(beirva) BETWEEN 1 AND 3;