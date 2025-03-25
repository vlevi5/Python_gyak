SELECT tanarok.nev, oktatott.targy, COUNT(oktatott.diakid) AS db
FROM tanarok INNER JOIN oktatott ON tanarok.id = oktatott.tanarid
GROUP BY tanarok.nev, oktatott.targy
ORDER BY db DESC
LIMIT 1;