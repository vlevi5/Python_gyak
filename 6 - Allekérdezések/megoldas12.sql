SELECT tanarok.nev, fizetesek.fizetes, fizetesek.kepesites, tanarok.felveve
FROM tanarok INNER JOIN fizetesek ON tanarok.id = fizetesek.tanarid
WHERE kepesites NOT IN (
    SELECT fizetesek.kepesites
    FROM fizetesek
    GROUP BY fizetesek.kepesites
    HAVING COUNT(*) > (
        SELECT COUNT(*) / 3
        FROM fizetesek
    )
);