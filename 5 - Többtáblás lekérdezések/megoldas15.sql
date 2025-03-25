SELECT diakok.nev, diakok.evfolyam, diakok.osztaly, SUM(oktatott.heti) AS heti_orak_szama
FROM diakok INNER JOIN oktatott ON diakok.id = oktatott.diakid 
WHERE diakok.nev LIKE "Fekete János"
GROUP BY diakok.id;