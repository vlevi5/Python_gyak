SELECT diakok.evfolyam, diakok.osztaly
FROM diakok
GROUP BY evfolyam, osztaly
HAVING COUNT(DISTINCT nem) = 1;