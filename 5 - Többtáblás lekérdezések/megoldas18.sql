SELECT tanarok.nev, AVG(jegyek.osztalyzat) AS jegyek_atlaga
FROM tanarok LEFT JOIN jegyek ON tanarok.id = jegyek.tanarid
GROUP BY tanarok.id
ORDER BY jegyek_atlaga DESC;