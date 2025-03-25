SELECT kepesites, ROUND(AVG(fizetes),-3) AS atlag_fizetes
FROM fizetesek
GROUP BY kepesites;