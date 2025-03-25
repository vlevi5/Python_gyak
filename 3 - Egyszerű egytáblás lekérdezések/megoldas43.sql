SELECT nev
FROM tanarok
WHERE POSITION(',' IN targyak) > 0
ORDER BY nev ASC;

/*  saját megoldás ↓

SELECT nev
FROM tanarok
WHERE targyak LIKE "%,%"
ORDER BY nev ASC;

*/
