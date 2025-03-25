SELECT fizetesek.fizetes
FROM fizetesek
WHERE fizetesek.fizetes > (
    SELECT AVG(fizetesek.fizetes)
    FROM fizetesek
);