SELECT diakok.nev
FROM diakok LEFT JOIN oktatott ON diakok.id = oktatott.diakid
WHERE oktatott.targy IS NULL;