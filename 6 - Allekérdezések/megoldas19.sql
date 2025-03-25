SELECT ROUND(AVG(db), 1) AS atlag
FROM (
    SELECT COUNT(oktatott.diakid) AS db
    FROM oktatott
    GROUP BY oktatott.tanarid, oktatott.targy
) AS diakok_tantargyankent;