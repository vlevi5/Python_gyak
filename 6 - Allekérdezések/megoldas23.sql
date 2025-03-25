SELECT tanarok.nev, fizetesek.kepesites, fizetesek.fizetes
FROM tanarok INNER JOIN fizetesek ON tanarok.id = fizetesek.tanarid
WHERE tanarok.id IN (
    SELECT oktatott.tanarid
    FROM oktatott
    GROUP BY oktatott.tanarid
    HAVING AVG(oktatott.heti) > 4
);