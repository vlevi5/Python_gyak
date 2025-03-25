SELECT fizetesek.fizetes, fizetesek.kepesites
FROM fizetesek
WHERE fizetesek.tanarid IN (
    SELECT oktatott.tanarid
    FROM oktatott
    GROUP BY oktatott.tanarid
    HAVING COUNT(DISTINCT oktatott.targy) > 1
);