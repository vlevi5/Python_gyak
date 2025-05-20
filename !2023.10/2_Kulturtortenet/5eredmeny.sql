SELECT csapat.nev, SUM(megoldas.pontszam) AS elert_pontszam
FROM csapat, megoldas
WHERE megoldas.csapatid = csapat.id
GROUP BY megoldas.csapatid
ORDER BY elert_pontszam DESC;