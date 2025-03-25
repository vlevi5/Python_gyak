SELECT ROUND(DATEDIFF(NOW(), felveve) / 365, 0) AS evek, SUBSTRING(nev, POSITION(' ' IN nev)) AS keresztnev
FROM tanarok
WHERE DATEDIFF(NOW(), szuletett) > 50 * 365;