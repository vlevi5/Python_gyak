SELECT jegyek.osztalyzat, MONTH(jegyek.beirva) AS honap, DAY(jegyek.beirva) AS nap
FROM jegyek
WHERE DATE(beirva) IN (
    SELECT DATE(beirva)
    FROM jegyek
    GROUP BY MONTH(beirva), DAY(beirva)
    HAVING COUNT(*) > 10
)
ORDER BY honap ASC, nap ASC;