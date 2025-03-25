SELECT evfolyam, osztaly
FROM diakok
GROUP BY evfolyam, osztaly
HAVING COUNT(nev) < "5";