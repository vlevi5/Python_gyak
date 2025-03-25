SELECT diakok.nev, oktatott.targy, oktatott.heti
FROM diakok INNER JOIN oktatott ON diakok.id = oktatott.diakid 
WHERE diakok.nev LIKE "Tóth%";