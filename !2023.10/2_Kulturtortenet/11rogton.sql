SELECT kovetkezo.nevado, kovetkezo.kituzes
FROM feladatsor AS elozo, feladatsor AS kovetkezo
WHERE DATEDIFF(kovetkezo.kituzes, elozo.hatarido) = 1;