SELECT jatekos.nev
FROM jatekos, egyesulet, bajnok
WHERE jatekos.id = bajnok.jatekos_id
	AND bajnok.egyesulet_id = egyesulet.id
	AND egyesulet.nev LIKE "MTK"
GROUP BY jatekos.id
ORDER BY jatekos.neme, jatekos.nev ASC;