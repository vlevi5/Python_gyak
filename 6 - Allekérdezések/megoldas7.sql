SELECT diakok.nev, diakok.nem, diakok.osztaly
FROM diakok
WHERE diakok.evfolyam IN (9, 11, 12)
ORDER BY diakok.evfolyam ASC;