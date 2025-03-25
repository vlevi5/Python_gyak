SELECT diakok.nev, diakok.evfolyam, diakok.osztaly
FROM diakok
WHERE diakok.evfolyam IN(
	SELECT diakok.evfolyam
    FROM diakok
    GROUP BY diakok.evfolyam
    HAVING COUNT(diakok.id) > 10
);