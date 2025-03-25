SELECT tanarok.nev, fizetesek.fizetes, fizetesek.kepesites
FROM fizetesek INNER JOIN tanarok ON fizetesek.tanarid = tanarok.id
WHERE fizetesek.evek < (
    SELECT AVG(fizetesek.evek)
    FROM fizetesek
);