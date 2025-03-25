SELECT YEAR(beirva) AS ev, MONTH(beirva) AS honap, DAY(beirva) AS nap, COUNT(*) AS jegyek_szama
FROM jegyek
GROUP BY YEAR(beirva), MONTH(beirva), DAY(beirva)
ORDER BY ev ASC, honap ASC, nap ASC;