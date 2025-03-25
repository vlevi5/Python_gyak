SELECT nev, LENGTH(nev)-1 AS karakterek_szama
FROM tanarok
ORDER BY LENGTH(nev) DESC
LIMIT 1;