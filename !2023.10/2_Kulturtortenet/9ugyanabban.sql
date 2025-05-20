SELECT feladatsor.nevado
FROM feladatsor
WHERE MONTH(feladatsor.kituzes) = MONTH(feladatsor.hatarido)
	AND feladatsor.ag = "irodalom";