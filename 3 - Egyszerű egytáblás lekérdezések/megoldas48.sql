SELECT
    tanarid,
    fizetes,
    ROUND(fizetes * 0.65, -1) AS havinetto,
    ROUND(fizetes * 0.65 / 22, 0) AS napinetto,
    ROUND(fizetes * 0.65 / 22 / 8, 0) AS oradij,
    ROUND(fizetes * 0.65, -1) * 12 AS evesnetto
FROM fizetesek
WHERE kepesites IS NOT NULL
ORDER BY evesnetto DESC;



/*  saját megoldás ↓

SELECT tanarid, fizetes, ROUND(fizetes*0.65, -1) AS havinetto, ROUND((fizetes*0.65)/22, 0) AS napinetto, ROUND(((fizetes*0.65)/22)/8, 0) AS oradij, ROUND((fizetes*0.65*12),0 ) AS evesnetto
FROM fizetesek
WHERE kepesites IS NOT NULL
ORDER BY evesnetto DESC;

*/