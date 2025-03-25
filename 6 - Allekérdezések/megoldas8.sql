SELECT tanarok.nev, tanarok.szuletett
FROM tanarok
WHERE id IN(
	SELECT oktatott.tanarid
    FROM oktatott
    GROUP BY oktatott.tanarid, oktatott.targy
    HAVING COUNT(oktatott.diakid) > 20
);