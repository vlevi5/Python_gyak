SELECT tanarok.nev AS tanar_neve, COUNT(jegyek.beirva) AS beirt_jegyek
FROM tanarok, jegyek
WHERE jegyek.tanarid = tanarok.id
GROUP BY tanarok.nev;