SELECT tanarok.nev AS tanar_neve, diakok.nev AS diak_neve, oktatott.targy, oktatott.heti
FROM tanarok, diakok, oktatott
WHERE oktatott.tanarid = tanarok.id AND oktatott.diakid = diakok.id
ORDER BY tanarok.nev ASC, oktatott.targy ASC;