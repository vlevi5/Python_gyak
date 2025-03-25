SELECT ROUND(AVG(DATEDIFF(NOW(),szuletett)/365),2) AS atlag_eletkor
FROM tanarok
WHERE targyak LIKE "%,%";