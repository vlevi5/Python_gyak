SELECT DISTINCT nyelvi.evfolyam, nyelvi.osztaly
FROM diakok AS nyelvi, diakok AS nemnyelvi
WHERE nyelvi.evfolyam = nemnyelvi.evfolyam
AND nyelvi.osztaly = nemnyelvi.osztaly
AND nyelvi.nyelvi
AND NOT nemnyelvi.nyelvi
ORDER BY nyelvi.evfolyam ASC, nyelvi.osztaly ASC;