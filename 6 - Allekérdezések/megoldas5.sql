SELECT tanarok.nev, fizetesek.fizetes, YEAR(tanarok.szuletett) AS szuletesi_ev
FROM fizetesek INNER JOIN tanarok ON fizetesek.tanarid = tanarok.id
WHERE fizetesek.evek < (
    SELECT AVG(fizetesek.evek)
    FROM fizetesek
)
AND fizetesek.fizetes > (
    SELECT AVG(fizetesek.fizetes)
    FROM fizetesek);
    