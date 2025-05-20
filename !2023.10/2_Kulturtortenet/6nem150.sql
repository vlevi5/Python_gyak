SELECT feladatsor.nevado, feladatsor.ag, SUM(feladat.pontszam) AS elerheto_pontszam
FROM feladatsor, feladat
WHERE feladatsor.id = feladat.feladatsorid	
GROUP BY feladat.feladatsorid
HAVING SUM(feladat.pontszam) != 150;