SELECT tanarok.nev, tanarok.felveve
FROM tanarok INNER JOIN jegyek ON tanarok.id = jegyek.tanarid
WHERE YEAR(jegyek.beirva) = "2023"
AND MONTH(jegyek.beirva) = "1"
AND jegyek.osztalyzat = "1"
GROUP BY tanarok.nev
HAVING COUNT(osztalyzat)  > (
    SELECT COUNT(*) / 8
    FROM jegyek
    WHERE YEAR(jegyek.beirva) = "2023"
	AND MONTH(jegyek.beirva) = "1"
	AND jegyek.osztalyzat = "1"
    GROUP BY YEAR(jegyek.beirva), MONTH(jegyek.beirva)
);