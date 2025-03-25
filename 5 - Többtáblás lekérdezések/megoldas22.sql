SELECT tanarok.nev, oktatott.targy, diakok.nev, diakok.nem
FROM tanarok INNER JOIN oktatott ON tanarok.id = oktatott.tanarid
INNER JOIN diakok on oktatott.diakid = diakok.id 
ORDER BY tanarok.nev DESC, oktatott.targy DESC, diakok.nev ASC;