SELECT kepesites, ROUND(AVG(fizetes),2) AS fizetes_atlag, ROUND(AVG(DATEDIFF(NOW(),szuletett)/365),2) AS atlag_eletkor
FROM tanarok, fizetesek
WHERE fizetesek.tanarid = tanarok.id
GROUP BY kepesites;