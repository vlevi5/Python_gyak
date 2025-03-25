SELECT tanarid, CONCAT(fizetes, " Ft") AS fizetes, CONCAT(ROUND(fizetes*0.65, -1), " Ft") AS havinetto, CONCAT(ROUND((fizetes*0.65)/22, 0), " Ft") AS napinetto, CONCAT(ROUND(((fizetes*0.65)/22)/8, 0), " Ft") AS oradij, CONCAT(ROUND((fizetes*0.65*12),0), " Ft") AS evesnetto
FROM fizetesek
WHERE kepesites IS NOT NULL
ORDER BY evesnetto DESC;

/* Az előző feladatból a saját megoldásomat vittem ide tovább, csak hozzáfűztem a CONCAT-et*/
