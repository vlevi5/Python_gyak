SELECT YEAR(jegyek.beirva) AS ev, MONTH(jegyek.beirva) AS honap, DAY(jegyek.beirva) AS nap
FROM jegyek
GROUP BY YEAR(jegyek.beirva), MONTH(jegyek.beirva), DAY(jegyek.beirva)
HAVING COUNT(*) > (
    SELECT AVG(darab)
    FROM (
        SELECT COUNT(*) AS darab
        FROM jegyek
        GROUP BY YEAR(jegyek.beirva), MONTH(jegyek.beirva), DAY(jegyek.beirva)
    ) AS napi_darabszamok
);