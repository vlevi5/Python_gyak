SELECT AVG(osztalyzat) AS atlag
FROM jegyek
WHERE YEAR(beirva) = "2023" AND MONTH(beirva) = "2";