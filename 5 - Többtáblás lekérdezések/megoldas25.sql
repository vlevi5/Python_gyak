SELECT diakok.nyelvi, COUNT(tanarok.id) AS db
FROM tanarok INNER JOIN oktatott ON tanarok.id = oktatott.tanarid
INNER JOIN diakok ON oktatott.diakid = diakok.id
GROUP BY nyelvi;