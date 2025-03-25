SELECT tanarok.nev, fizetesek.fizetes, COUNT(*)*4*1000 AS bonusz, fizetesek.fizetes + COUNT(*)*4*1000 AS teljes_fizetes
FROM fizetesek INNER JOIN tanarok ON fizetesek.tanarid = tanarok.id
LEFT JOIN oktatott ON tanarok.id = oktatott.tanarid
GROUP BY nev
ORDER BY teljes_fizetes DESC;