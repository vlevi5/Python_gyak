SELECT osztalyzat, DAY(beirva)
FROM jegyek
WHERE YEAR(beirva) = "2023" AND MONTH(beirva) = "2";