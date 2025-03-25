SELECT tanarok.nev, oktatott.targy, COUNT(*) AS diakok_szama
FROM tanarok INNER JOIN oktatott ON tanarok.id = oktatott.tanarid
WHERE tanarok.szuletett = (
    SELECT MIN(tanarok.szuletett)
    FROM tanarok)
GROUP BY tanarok.nev, oktatott.targy
ORDER BY diakok_szama DESC;