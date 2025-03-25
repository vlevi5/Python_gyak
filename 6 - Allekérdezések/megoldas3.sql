SELECT nev, fizetes
FROM tanarok INNER JOIN fizetesek ON tanarok.id = fizetesek.tanarid
WHERE fizetesek.fizetes = (
    SELECT MAX(fizetesek.fizetes)
    FROM fizetesek
);