SELECT diakok.nev, diakok.nem
FROM diakok 
WHERE diakok.evfolyam = (
    SELECT diakok.evfolyam
    FROM diakok
    GROUP BY diakok.evfolyam, diakok.osztaly
    ORDER BY COUNT(*) DESC LIMIT 1
)
AND osztaly = ( 
    SELECT diakok.osztaly
    FROM diakok
    GROUP BY diakok.evfolyam, diakok.osztaly
    ORDER BY COUNT(*) DESC LIMIT 1
);