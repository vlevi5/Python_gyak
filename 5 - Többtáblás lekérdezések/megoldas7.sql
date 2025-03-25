SELECT diakok.nev, COUNT(*) AS elofordulasok_szama
FROM diakok
GROUP BY diakok.nev
HAVING COUNT(diakok.nev) > 1;