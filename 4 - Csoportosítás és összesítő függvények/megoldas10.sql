SELECT DAY(beirva) AS nap, COUNT(*) AS jegyek_szama
FROM jegyek
WHERE MONTH(beirva) = "1"
GROUP BY DAY(beirva)
ORDER BY nap ASC;