SELECT feladatsor.nevado
FROM feladatsor
ORDER BY DATEDIFF(feladatsor.hatarido, feladatsor.kituzes) ASC LIMIT 1;