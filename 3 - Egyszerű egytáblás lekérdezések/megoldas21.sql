SELECT nev, targyak, felveve
FROM tanarok
WHERE szuletett < "1980-01-01"
ORDER BY nev DESC;