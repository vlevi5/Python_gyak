SELECT feladatsor.nevado, COUNT(*) AS be_nem_adott_feladatok_szama
FROM feladatsor, feladat
WHERE feladatsor.id = feladat.feladatsorid
	AND feladat.id NOT IN (
    	SELECT megoldas.feladatid
        FROM megoldas, csapat
        WHERE megoldas.csapatid = csapat.id
        	AND csapat.nev = "#win"
)
GROUP BY feladatsor.nevado;