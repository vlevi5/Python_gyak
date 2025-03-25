SELECT tanarok.nev, fizetesek.fizetes
FROM tanarok, fizetesek
WHERE tanarok.id = fizetesek.tanarid;