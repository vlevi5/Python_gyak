SELECT AVG(jegyek.osztalyzat) - (
	SELECT AVG(jegyek.osztalyzat)    
    FROM jegyek
) AS elteres
FROM jegyek
GROUP BY jegyek.diakid;