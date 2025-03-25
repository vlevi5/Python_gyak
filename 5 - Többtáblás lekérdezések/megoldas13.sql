SELECT DISTINCT tanarok.nev
FROM tanarok INNER JOIN oktatott ON tanarok.id = oktatott.tanarid
INNER JOIN diakok ON oktatott.diakid = diakok.id
WHERE diakok.evfolyam = "11" AND diakok.osztaly = "B";