SELECT DISTINCT fiuk.evfolyam, fiuk.osztaly
FROM diakok AS fiuk, diakok AS lanyok
WHERE fiuk.nem = "F" AND lanyok.nem = "N"
AND fiuk.evfolyam = lanyok.evfolyam
AND fiuk.osztaly = lanyok.osztaly
ORDER BY fiuk.evfolyam DESC, fiuk.osztaly DESC;