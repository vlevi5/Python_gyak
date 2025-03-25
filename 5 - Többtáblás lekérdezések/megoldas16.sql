SELECT tanarok.nev, oktatott.targy
FROM tanarok LEFT JOIN oktatott ON tanarok.id = oktatott.tanarid
GROUP BY oktatott.targy
ORDER BY tanarok.nev ASC;