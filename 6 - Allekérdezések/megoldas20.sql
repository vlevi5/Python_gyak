SELECT MAX(db) - MIN(db) AS kulonbseg
FROM (
    SELECT COUNT(jegyek.id) AS db
    FROM jegyek
    WHERE MONTH(jegyek.beirva) = "3" AND jegyek.osztalyzat = "5"
    GROUP BY jegyek.tanarid
) AS jegyek_tanaronkent;